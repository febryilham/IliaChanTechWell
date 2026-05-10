"""
IliaChan TechWell — RAG Retrieval Module
Searches health data by text similarity, image similarity, or SQL.
"""

import sqlite3
import numpy as np
from PIL import Image
from config import DATABASE_PATH
from rag.clip_engine import encode_text, encode_image, compute_similarity


def search_by_text(query: str, top_k: int = 3) -> list:
    """Search health topics by text relevance using CLIP text embeddings."""
    conn = sqlite3.connect(str(DATABASE_PATH))
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Get all topics
    cursor.execute("SELECT * FROM health_topics")
    topics = [dict(row) for row in cursor.fetchall()]
    conn.close()

    if not topics:
        return []

    # Compute query embedding
    query_emb = encode_text(query)
    if np.all(query_emb == 0):
        # Fallback: keyword search
        return _keyword_search(query, topics, top_k)

    # Score each topic by similarity to query
    scored = []
    for topic in topics:
        combined_text = f"{topic['topic_name']} {topic['description']} {topic['symptoms']}"
        topic_emb = encode_text(combined_text)
        sim = compute_similarity(query_emb, topic_emb)
        scored.append((sim, topic))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [item[1] for item in scored[:top_k]]


def search_by_image(image: Image.Image, top_k: int = 3) -> list:
    """Search similar health images using CLIP image embeddings."""
    conn = sqlite3.connect(str(DATABASE_PATH))
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT hi.*, ht.topic_name, ht.description, ht.solutions
        FROM health_images hi
        JOIN health_topics ht ON hi.topic_id = ht.id
        WHERE hi.clip_embedding IS NOT NULL
    """)
    images = [dict(row) for row in cursor.fetchall()]
    conn.close()

    if not images:
        # No stored embeddings; fall back to topic-level text search
        return search_by_text("postur duduk kesehatan", top_k)

    query_emb = encode_image(image)
    scored = []
    for img in images:
        stored_emb = np.frombuffer(img["clip_embedding"], dtype=np.float32)
        sim = compute_similarity(query_emb, stored_emb)
        scored.append((sim, img))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [item[1] for item in scored[:top_k]]


def get_topic_with_details(topic_id: int) -> dict:
    """Get a topic with its journals and recommendations."""
    conn = sqlite3.connect(str(DATABASE_PATH))
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM health_topics WHERE id = ?", (topic_id,))
    topic = dict(cursor.fetchone()) if cursor.fetchone() else {}

    # Re-query since fetchone consumed it
    cursor.execute("SELECT * FROM health_topics WHERE id = ?", (topic_id,))
    row = cursor.fetchone()
    if row:
        topic = dict(row)

    cursor.execute("SELECT * FROM health_journals WHERE topic_id = ?", (topic_id,))
    topic["journals"] = [dict(r) for r in cursor.fetchall()]

    cursor.execute("SELECT * FROM health_recommendations WHERE topic_id = ?", (topic_id,))
    topic["recommendations"] = [dict(r) for r in cursor.fetchall()]

    conn.close()
    return topic


def get_all_topics() -> list:
    """Get all health topics."""
    conn = sqlite3.connect(str(DATABASE_PATH))
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM health_topics ORDER BY id")
    topics = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return topics


def get_journals_for_topic(topic_id: int) -> list:
    """Get journal references for a specific topic."""
    conn = sqlite3.connect(str(DATABASE_PATH))
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM health_journals WHERE topic_id = ?", (topic_id,))
    journals = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return journals


def _keyword_search(query: str, topics: list, top_k: int) -> list:
    """Simple keyword-based search fallback."""
    query_lower = query.lower()
    scored = []
    for topic in topics:
        score = 0
        searchable = (
            f"{topic['topic_name']} {topic['description']} "
            f"{topic['symptoms']} {topic['solutions']}"
        ).lower()
        for word in query_lower.split():
            if len(word) > 2 and word in searchable:
                score += 1
        scored.append((score, topic))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [item[1] for item in scored[:top_k]]

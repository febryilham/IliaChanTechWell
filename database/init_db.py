"""
IliaChan TechWell — Database Initialization
Creates SQLite tables and seeds health education data.
"""

import sqlite3
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))
from config import DATABASE_PATH
from database.seed_data import HEALTH_TOPICS, HEALTH_JOURNALS, HEALTH_RECOMMENDATIONS

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS health_topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_name TEXT NOT NULL,
    category TEXT NOT NULL,
    description TEXT NOT NULL,
    risks TEXT NOT NULL,
    symptoms TEXT NOT NULL,
    solutions TEXT NOT NULL,
    prevention_tips TEXT,
    risk_level TEXT CHECK(risk_level IN ('LOW', 'MEDIUM', 'HIGH')),
    image_filename TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS health_images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id INTEGER NOT NULL,
    image_path TEXT NOT NULL,
    description TEXT,
    clip_embedding BLOB,
    FOREIGN KEY (topic_id) REFERENCES health_topics(id)
);

CREATE TABLE IF NOT EXISTS health_journals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    authors TEXT,
    year INTEGER,
    source TEXT NOT NULL,
    source_type TEXT CHECK(source_type IN ('journal', 'news', 'social_media', 'who', 'government')),
    summary TEXT,
    url TEXT,
    FOREIGN KEY (topic_id) REFERENCES health_topics(id)
);

CREATE TABLE IF NOT EXISTS health_recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id INTEGER NOT NULL,
    recommendation TEXT NOT NULL,
    difficulty TEXT CHECK(difficulty IN ('easy', 'medium', 'hard')),
    time_required TEXT,
    equipment_needed TEXT,
    FOREIGN KEY (topic_id) REFERENCES health_topics(id)
);

CREATE TABLE IF NOT EXISTS chat_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    chat_type TEXT CHECK(chat_type IN ('agent', 'assistant')),
    role TEXT NOT NULL,
    message TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""


def init_database():
    """Create database tables and seed initial data."""
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DATABASE_PATH))
    cursor = conn.cursor()

    # Create tables
    cursor.executescript(SCHEMA_SQL)
    print("[OK] Tables created.")

    # Check if data already exists
    cursor.execute("SELECT COUNT(*) FROM health_topics")
    if cursor.fetchone()[0] > 0:
        print("[SKIP] Data already seeded.")
        conn.close()
        return

    # Seed health topics
    for i, topic in enumerate(HEALTH_TOPICS):
        img_name = f"topic_{i + 1}.png"
        cursor.execute(
            """INSERT INTO health_topics 
               (topic_name, category, description, risks, symptoms, solutions, prevention_tips, risk_level, image_filename)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                topic["topic_name"], topic["category"], topic["description"],
                topic["risks"], topic["symptoms"], topic["solutions"],
                topic["prevention_tips"], topic["risk_level"], img_name,
            ),
        )
    print(f"[OK] Seeded {len(HEALTH_TOPICS)} health topics.")

    # Seed journals
    for j in HEALTH_JOURNALS:
        topic_id = j["topic_idx"] + 1  # 1-indexed
        cursor.execute(
            """INSERT INTO health_journals 
               (topic_id, title, authors, year, source, source_type, summary, url)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (topic_id, j["title"], j["authors"], j["year"], j["source"],
             j["source_type"], j["summary"], j["url"]),
        )
    print(f"[OK] Seeded {len(HEALTH_JOURNALS)} journal references.")

    # Seed recommendations
    for r in HEALTH_RECOMMENDATIONS:
        topic_id = r["topic_idx"] + 1
        cursor.execute(
            """INSERT INTO health_recommendations 
               (topic_id, recommendation, difficulty, time_required, equipment_needed)
               VALUES (?, ?, ?, ?, ?)""",
            (topic_id, r["recommendation"], r["difficulty"],
             r["time_required"], r["equipment_needed"]),
        )
    print(f"[OK] Seeded {len(HEALTH_RECOMMENDATIONS)} recommendations.")

    conn.commit()
    conn.close()
    print(f"[DONE] Database ready at: {DATABASE_PATH}")


def get_connection():
    """Get a database connection."""
    return sqlite3.connect(str(DATABASE_PATH))


def execute_query(query: str, params: tuple = ()):
    """Execute a read query and return results with column names."""
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    except Exception as e:
        return [{"error": str(e)}]
    finally:
        conn.close()


def list_tables():
    """List all tables in the database."""
    return execute_query("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")


def describe_table(table_name: str):
    """Get column info for a table."""
    return execute_query(f"PRAGMA table_info({table_name})")


if __name__ == "__main__":
    init_database()

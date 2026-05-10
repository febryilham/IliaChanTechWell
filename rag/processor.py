"""
IliaChan TechWell — RAG Context Processor
Builds augmented context from retrieved data for LLM responses.
"""

from config import get_groq_client, GROQ_MODEL
from rag.retrieval import search_by_text, get_journals_for_topic


def build_rag_context(query: str, retrieved_topics: list = None, image_analysis: str = None) -> str:
    """Build RAG context string from retrieved data."""
    context_parts = []

    # Auto-retrieve if not provided
    if retrieved_topics is None:
        retrieved_topics = search_by_text(query, top_k=3)

    for topic in retrieved_topics:
        tid = topic.get("id", topic.get("topic_id", 0))
        journals = get_journals_for_topic(tid) if tid else []

        part = f"""
### {topic.get('topic_name', 'Unknown Topic')}
**Kategori:** {topic.get('category', 'N/A')}
**Level Risiko:** {topic.get('risk_level', 'N/A')}
**Deskripsi:** {topic.get('description', 'N/A')}
**Risiko:** {topic.get('risks', 'N/A')}
**Gejala:** {topic.get('symptoms', 'N/A')}
**Solusi:** {topic.get('solutions', 'N/A')}
"""
        if journals:
            part += "\n**Referensi:**\n"
            for j in journals:
                part += f"- {j['title']} ({j['authors']}, {j['year']}) — {j['source']}\n"
                part += f"  Ringkasan: {j['summary']}\n"

        context_parts.append(part)

    if image_analysis:
        context_parts.append(f"\n### Analisis Gambar User:\n{image_analysis}")

    return "\n---\n".join(context_parts)


def generate_rag_response(user_message: str, context: str, chat_history: list = None) -> str:
    """Generate a response using Groq LLM with RAG context."""
    groq = get_groq_client()

    system_msg = (
        "Anda adalah asisten konsultan kesehatan digital. "
        "Gunakan konteks berikut untuk menjawab pertanyaan user secara informatif. "
        "Sertakan referensi jurnal jika tersedia. Jawab dalam bahasa Indonesia.\n\n"
        f"KONTEKS:\n{context}"
    )

    messages = [{"role": "system", "content": system_msg}]

    # Add recent history
    if chat_history:
        for msg in chat_history[-6:]:
            role = msg["role"] if msg["role"] == "user" else "assistant"
            messages.append({"role": role, "content": msg["content"]})

    messages.append({"role": "user", "content": user_message})

    try:
        response = groq.chat.completions.create(
            model=GROQ_MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=2000,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error generating response: {str(e)[:100]}"

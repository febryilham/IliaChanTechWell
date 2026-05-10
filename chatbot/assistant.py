"""
IliaChan TechWell — Reactive Assistant Chatbot
Uses Groq for RAG/SQL processing, Gemini for image analysis.
"""

import streamlit as st
from PIL import Image
from config import get_gemini_client, get_groq_client, GEMINI_MODEL, GROQ_MODEL
from chatbot.prompts import ASSISTANT_SYSTEM_PROMPT, IMAGE_ANALYSIS_PROMPT
from database.init_db import execute_query, list_tables, describe_table


class HealthAssistant:
    """Reactive AI Assistant — Health consultation with RAG + SQL + Image analysis."""

    def __init__(self):
        self.groq_client = get_groq_client()
        self.gemini_client = get_gemini_client()
        self._ensure_session_state()

    def _ensure_session_state(self):
        if "assistant_chat_history" not in st.session_state:
            st.session_state.assistant_chat_history = []
        if "assistant_messages" not in st.session_state:
            st.session_state.assistant_messages = []  # For Groq API format
        if "consultation_active" not in st.session_state:
            st.session_state.consultation_active = True
        if "uploaded_images" not in st.session_state:
            st.session_state.uploaded_images = []

    def _get_db_context(self) -> str:
        """Build database context string for the LLM."""
        tables = list_tables()
        table_names = [t["name"] for t in tables if "error" not in t]
        context_parts = []
        for tname in table_names:
            cols = describe_table(tname)
            col_info = ", ".join(
                [f"{c['name']} ({c['type']})" for c in cols if "error" not in c]
            )
            context_parts.append(f"Table `{tname}`: {col_info}")
        return "\n".join(context_parts)

    def _query_database(self, user_message: str) -> str:
        """Use Groq LLM to generate SQL and query the database."""
        db_context = self._get_db_context()

        sql_prompt = (
            f"Berdasarkan pertanyaan user berikut, buatkan SQL query yang tepat.\n"
            f"Database memiliki tabel:\n{db_context}\n\n"
            f"Pertanyaan: {user_message}\n\n"
            f"HANYA berikan SQL query dalam format:\n```sql\nQUERY\n```\n"
            f"Jika pertanyaan tidak memerlukan query database, jawab: NO_QUERY"
        )

        try:
            response = self.groq_client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[{"role": "user", "content": sql_prompt}],
                temperature=0.1,
                max_tokens=500,
            )
            sql_response = response.choices[0].message.content.strip()

            if "NO_QUERY" in sql_response:
                return ""

            # Extract SQL from markdown code block
            if "```sql" in sql_response:
                sql = sql_response.split("```sql")[1].split("```")[0].strip()
            elif "```" in sql_response:
                sql = sql_response.split("```")[1].split("```")[0].strip()
            else:
                sql = sql_response

            # Safety: only allow SELECT queries
            if not sql.upper().strip().startswith("SELECT"):
                return ""

            results = execute_query(sql)
            if results and "error" not in results[0]:
                return f"\n📊 Data dari database:\n{_format_results(results)}\n"
            return ""
        except Exception:
            return ""

    def analyze_image(self, image: Image.Image) -> str:
        """Analyze uploaded image using Gemini Vision."""
        try:
            response = self.gemini_client.models.generate_content(
                model=GEMINI_MODEL,
                contents=[IMAGE_ANALYSIS_PROMPT, image],
            )
            return response.text
        except Exception as e:
            return f"⚠️ Tidak dapat menganalisis gambar: {str(e)[:100]}"

    def send_message(self, user_message: str, image: Image.Image = None) -> str:
        """Process user message with optional image, using RAG pipeline."""
        # Store user message
        st.session_state.assistant_chat_history.append(
            {"role": "user", "content": user_message}
        )

        # Build context
        context_parts = []

        # 1. Query database for relevant data
        db_data = self._query_database(user_message)
        if db_data:
            context_parts.append(db_data)

        # 2. Analyze image if provided
        image_analysis = ""
        if image is not None:
            image_analysis = self.analyze_image(image)
            context_parts.append(f"\n🖼️ Analisis Gambar:\n{image_analysis}")
            st.session_state.uploaded_images.append("uploaded")

        # 3. Build RAG-augmented prompt
        rag_context = "\n".join(context_parts) if context_parts else ""

        augmented_prompt = (
            f"{ASSISTANT_SYSTEM_PROMPT}\n\n"
            f"{'Konteks dari database dan analisis:\n' + rag_context if rag_context else ''}\n\n"
            f"Pertanyaan/pesan user: {user_message}\n\n"
            f"Berikan jawaban yang informatif, sertakan referensi jika ada data dari database."
        )

        # 4. Generate response via Groq
        try:
            # Build messages with recent history
            messages = [{"role": "system", "content": ASSISTANT_SYSTEM_PROMPT}]
            recent = st.session_state.assistant_chat_history[-10:]
            for msg in recent[:-1]:  # Exclude current message
                messages.append({
                    "role": msg["role"] if msg["role"] == "user" else "assistant",
                    "content": msg["content"]
                })
            messages.append({"role": "user", "content": augmented_prompt})

            response = self.groq_client.chat.completions.create(
                model=GROQ_MODEL,
                messages=messages,
                temperature=0.7,
                max_tokens=2000,
            )
            reply = response.choices[0].message.content
        except Exception as e:
            reply = f"⚠️ Maaf, terjadi kesalahan: {str(e)[:100]}"

        # Store response
        st.session_state.assistant_chat_history.append(
            {"role": "assistant", "content": reply}
        )

        # Check for conversation end
        self._check_conversation_end(reply)

        return reply

    def _check_conversation_end(self, response: str):
        """Detect if the consultation has reached a satisfying conclusion."""
        end_keywords = ["selamat tinggal", "terima kasih telah berkonsultasi",
                        "sampai jumpa", "semoga sehat selalu", "jaga kesehatan"]
        for kw in end_keywords:
            if kw in response.lower():
                st.session_state.consultation_active = False
                break

    def get_chat_history(self) -> list:
        return st.session_state.assistant_chat_history

    def clear_history(self):
        st.session_state.assistant_chat_history = []
        st.session_state.assistant_messages = []
        st.session_state.consultation_active = True
        st.session_state.uploaded_images = []


def _format_results(results: list) -> str:
    """Format SQL query results for display."""
    if not results:
        return "Tidak ada data ditemukan."
    formatted = []
    for row in results[:5]:  # Limit to 5 rows
        items = [f"  • **{k}**: {v}" for k, v in row.items() if v]
        formatted.append("\n".join(items))
    return "\n---\n".join(formatted)

"""
IliaChan TechWell — Proactive Agent Chatbot (Iliachan NPC)
Uses Gemini 2.5 Flash Lite for character-driven health education conversations.
"""

import random
import streamlit as st
from config import get_gemini_client, GEMINI_MODEL
from chatbot.prompts import AGENT_SYSTEM_PROMPT, GREETING_TEMPLATES


class IliachanAgent:
    """Proactive AI Agent — Iliachan character from the 30th century."""

    def __init__(self):
        self.client = get_gemini_client()
        self._ensure_session_state()

    def _ensure_session_state(self):
        """Initialize session state keys for agent chat."""
        if "agent_chat_history" not in st.session_state:
            st.session_state.agent_chat_history = []
        if "agent_greeted" not in st.session_state:
            st.session_state.agent_greeted = False
        if "current_topic" not in st.session_state:
            st.session_state.current_topic = None
        if "gemini_agent_chat" not in st.session_state:
            st.session_state.gemini_agent_chat = None

    def _get_chat_session(self):
        """Get or create Gemini chat session."""
        if st.session_state.gemini_agent_chat is None:
            # Build history for Gemini from stored chat
            history = []
            for msg in st.session_state.agent_chat_history:
                role = "user" if msg["role"] == "user" else "model"
                history.append({"role": role, "parts": [{"text": msg["content"]}]})

            st.session_state.gemini_agent_chat = self.client.chats.create(
                model=GEMINI_MODEL,
                config={"system_instruction": AGENT_SYSTEM_PROMPT},
                history=history,
            )
        return st.session_state.gemini_agent_chat

    def get_greeting(self) -> str:
        """Generate initial greeting from Iliachan."""
        if st.session_state.agent_greeted:
            return None

        greeting = random.choice(GREETING_TEMPLATES)

        # Enhance with Gemini
        try:
            chat = self._get_chat_session()
            response = chat.send_message(
                "Berikan sapaan pembuka yang unik dan hangat sebagai Iliachan. "
                "Tanyakan kabar kesehatan user hari ini dan berikan satu fakta "
                "menarik tentang kesehatan dari perspektif masa depan."
            )
            greeting = response.text
        except Exception:
            pass  # Fallback to template greeting

        st.session_state.agent_greeted = True
        st.session_state.agent_chat_history.append(
            {"role": "assistant", "content": greeting}
        )
        return greeting

    def send_message(self, user_message: str) -> str:
        """Send user message and get Iliachan's response."""
        # Store user message
        st.session_state.agent_chat_history.append(
            {"role": "user", "content": user_message}
        )

        try:
            chat = self._get_chat_session()
            response = chat.send_message(user_message)
            reply = response.text
        except Exception as e:
            reply = (
                f"⚠️ Maaf, ada gangguan pada koneksi temporal saya. "
                f"Error: {str(e)[:100]}. Coba lagi ya!"
            )

        # Store bot response
        st.session_state.agent_chat_history.append(
            {"role": "assistant", "content": reply}
        )

        # Detect if topic should redirect to assistant
        self._detect_topic_redirect(reply)

        return reply

    def _detect_topic_redirect(self, response: str):
        """Detect if the conversation should redirect to assistant chat."""
        redirect_keywords = [
            "konsultasi lebih lanjut", "assistant chat", "pembahasan mendalam",
            "konsultasi kesehatan", "analisis lebih detail",
        ]
        for kw in redirect_keywords:
            if kw in response.lower():
                st.session_state.current_topic = "redirect_suggested"
                break

    def get_chat_history(self) -> list:
        """Return current chat history."""
        return st.session_state.agent_chat_history

    def clear_history(self):
        """Reset chat history and session."""
        st.session_state.agent_chat_history = []
        st.session_state.agent_greeted = False
        st.session_state.gemini_agent_chat = None
        st.session_state.current_topic = None

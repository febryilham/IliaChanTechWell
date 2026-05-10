"""
IliaChan TechWell — Agent Chat Page
Proactive conversation with Iliachan NPC character.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
from config import PAGE_TITLE
from components.animations import inject_global_styles
from components.chat_ui import render_chat_message, render_chat_header
from components.sidebar import render_sidebar, render_top_nav
from chatbot.agent import IliachanAgent
from database.init_db import init_database
from i18n import t

st.set_page_config(page_title=f"{PAGE_TITLE} — Agent Chat", page_icon="🤖", layout="wide")
inject_global_styles()
render_sidebar()
render_top_nav()

lang = st.session_state.get("app_lang", "id")

# Ensure database exists
init_database()

# Header
render_chat_header(
    title=t("agent_title", lang),
    subtitle=t("agent_subtitle", lang),
    icon="🤖",
    status_color="#10b981",
)

# Initialize agent
agent = IliachanAgent()

# Auto-greeting
if not st.session_state.get("agent_greeted", False):
    with st.spinner(t("agent_greeting_spinner", lang)):
        greeting = agent.get_greeting()

# Display chat history
chat_container = st.container()
with chat_container:
    for msg in agent.get_chat_history():
        render_chat_message(msg["role"], msg["content"], chat_type="agent")

# Redirect suggestion
if st.session_state.get("current_topic") == "redirect_suggested":
    st.info(t("agent_redirect", lang))
    st.session_state.current_topic = None

# Chat input
user_input = st.chat_input(t("agent_input", lang))
if user_input:
    render_chat_message("user", user_input, chat_type="agent")
    with st.spinner(t("agent_typing", lang)):
        reply = agent.send_message(user_input)
    render_chat_message("assistant", reply, chat_type="agent")
    st.rerun()

# Clear button
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button(t("agent_reset", lang), use_container_width=True):
        agent.clear_history()
        st.rerun()

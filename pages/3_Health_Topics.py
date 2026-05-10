"""
IliaChan TechWell — Health Topics Gallery Page
Browse and explore health education topics.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
from config import PAGE_TITLE
from components.animations import inject_global_styles
from components.sidebar import render_sidebar, render_top_nav
from components.health_cards import render_topic_card, render_topic_detail
from rag.retrieval import get_all_topics, get_journals_for_topic
from database.init_db import init_database, execute_query
from i18n import t

st.set_page_config(page_title=f"{PAGE_TITLE} — Health Topics", page_icon="📊", layout="wide")
inject_global_styles()
render_sidebar()
render_top_nav()

lang = st.session_state.get("app_lang", "id")

# Ensure database exists
init_database()

# Header
st.markdown(f"""
<div style="text-align:center;padding:1rem 0 2rem 0;">
    <h1 style="
        font-family:'Outfit',sans-serif;font-size:2.2rem;
        background:linear-gradient(135deg,#06b6d4,#a855f7,#ec4899);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent;
        margin:0;
    ">{t("topics_title", lang)}</h1>
    <p style="color:#94a3b8;font-size:0.95rem;margin-top:0.5rem;">
        {t("topics_subtitle", lang)}
    </p>
</div>
""", unsafe_allow_html=True)

# Load topics
topics = get_all_topics()

if not topics:
    st.warning(t("topics_no_db", lang))
    st.stop()

# Category filter
categories = list(set(t_item["category"] for t_item in topics))
categories.insert(0, t("topics_all", lang))
selected_cat = st.selectbox(t("topics_filter", lang), categories)

all_label = t("topics_all", lang)
if selected_cat != all_label:
    filtered = [t_item for t_item in topics if t_item["category"] == selected_cat]
else:
    filtered = topics

# Display topic cards
if "selected_topic_id" not in st.session_state:
    st.session_state.selected_topic_id = None

# Grid view
cols = st.columns(2)
for i, topic in enumerate(filtered):
    with cols[i % 2]:
        clicked = render_topic_card(topic)
        if clicked:
            st.session_state.selected_topic_id = topic["id"]
            st.rerun()

# Detail view
if st.session_state.selected_topic_id:
    st.markdown("---")
    topic_id = st.session_state.selected_topic_id

    topic_data = [t_item for t_item in topics if t_item["id"] == topic_id]
    if topic_data:
        topic_data = topic_data[0]
        journals = get_journals_for_topic(topic_id)
        recs = execute_query(
            "SELECT * FROM health_recommendations WHERE topic_id = ?", (topic_id,)
        )

        render_topic_detail(topic_data, journals=journals, recommendations=recs, lang=lang)

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button(t("topics_ask_assist", lang), use_container_width=True):
                st.session_state.current_topic = topic_data["topic_name"]
                st.switch_page("pages/2_Assistant_Chat.py")
        with col2:
            if st.button(t("topics_chat_agent", lang), use_container_width=True):
                st.switch_page("pages/1_Agent_Chat.py")
        with col3:
            if st.button(t("topics_back", lang), use_container_width=True):
                st.session_state.selected_topic_id = None
                st.rerun()

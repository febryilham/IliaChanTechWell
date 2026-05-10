"""
IliaChan TechWell — Sidebar Component
Navigation sidebar with health tips, session info, and language toggle.
"""

import random
import streamlit as st
from i18n import t, get_tips


def _get_lang():
    """Get current language from session state."""
    if "app_lang" not in st.session_state:
        st.session_state.app_lang = "id"
    return st.session_state.app_lang


def render_top_nav():
    """Render a persistent top navigation bar with logo and language toggle."""
    lang = _get_lang()

    # Logo row — separate from navbar
    logo_col, lang_col = st.columns([5, 1])
    with logo_col:
        st.markdown("""
        <div style="display:flex;align-items:center;gap:10px;padding:0.3rem 0 0.2rem 0;">
            <span style="font-size:1.6rem;">🩺</span>
            <span style="
                font-family:'Outfit',sans-serif;font-size:1.1rem;font-weight:700;
                background:linear-gradient(135deg,#06b6d4,#a855f7);
                -webkit-background-clip:text;-webkit-text-fill-color:transparent;
            ">IliaChan TechWell</span>
            <span style="color:#475569;font-size:0.65rem;margin-left:4px;">v1.0</span>
        </div>
        """, unsafe_allow_html=True)
    with lang_col:
        options = {"🇮🇩 Indonesia": "id", "🇬🇧 English": "en"}
        current_label = "🇮🇩 Indonesia" if lang == "id" else "🇬🇧 English"
        selected = st.selectbox(
            t("lang_label", lang),
            list(options.keys()),
            index=list(options.values()).index(lang),
            key="lang_selector",
            label_visibility="collapsed",
        )
        new_lang = options[selected]
        if new_lang != lang:
            st.session_state.app_lang = new_lang
            st.rerun()

    # Navigation bar
    nav_cols = st.columns(5)
    with nav_cols[0]:
        st.page_link("app.py", label=t("nav_home", lang), use_container_width=True)
    with nav_cols[1]:
        st.page_link("pages/1_Agent_Chat.py", label=t("nav_agent", lang), use_container_width=True)
    with nav_cols[2]:
        st.page_link("pages/2_Assistant_Chat.py", label=t("nav_assistant", lang), use_container_width=True)
    with nav_cols[3]:
        st.page_link("pages/3_Health_Topics.py", label=t("nav_topics", lang), use_container_width=True)
    with nav_cols[4]:
        st.page_link("pages/4_About.py", label=t("nav_about", lang), use_container_width=True)

    st.markdown("""
    <hr style="border:none;height:1px;
        background:linear-gradient(90deg,transparent,#06b6d430,#a855f730,transparent);
        margin:0.2rem 0 0.8rem 0;">
    """, unsafe_allow_html=True)


def render_sidebar():
    """Render the navigation sidebar."""
    lang = _get_lang()
    tips = get_tips(lang)

    with st.sidebar:
        st.markdown("""
        <div style="text-align:center;padding:1rem 0;">
            <div style="font-size:3rem;margin-bottom:0.5rem;">🩺</div>
            <h2 style="
                font-family:'Outfit',sans-serif;
                background:linear-gradient(135deg,#06b6d4,#a855f7);
                -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                font-size:1.4rem;margin:0;
            ">IliaChan TechWell</h2>
            <p style="color:#64748b;font-size:0.75rem;margin-top:4px;">
                """ + t("sidebar_tagline", lang) + """
            </p>
        </div>
        <hr style="border-color:rgba(255,255,255,0.06);margin:0.5rem 0 1rem 0;">
        """, unsafe_allow_html=True)

        # Health tip of the moment
        st.markdown(f"""
        <p style="color:#94a3b8;font-size:0.7rem;font-weight:600;
           text-transform:uppercase;letter-spacing:1px;">
           {t("sidebar_tip_title", lang)}
        </p>
        """, unsafe_allow_html=True)

        if "current_tip" not in st.session_state:
            st.session_state.current_tip = random.choice(tips)

        st.markdown(f"""
        <div style="
            background:rgba(6,182,212,0.08);
            border:1px solid rgba(6,182,212,0.2);
            border-radius:12px;padding:0.8rem;
            font-size:0.82rem;color:#94a3b8;line-height:1.5;
        ">
            {st.session_state.current_tip}
        </div>
        """, unsafe_allow_html=True)

        if st.button(t("sidebar_tip_btn", lang), use_container_width=True):
            st.session_state.current_tip = random.choice(tips)
            st.rerun()

        # Session info
        st.markdown("<br>", unsafe_allow_html=True)
        agent_count = len(st.session_state.get("agent_chat_history", []))
        assist_count = len(st.session_state.get("assistant_chat_history", []))
        msg_word = t("sidebar_msg", lang)

        st.markdown(f"""
        <div style="
            background:rgba(255,255,255,0.03);border-radius:12px;
            padding:0.8rem;font-size:0.78rem;color:#64748b;
        ">
            <p style="margin:0 0 4px 0;">📊 <strong>{t("sidebar_stats", lang)}</strong></p>
            <p style="margin:2px 0;">{t("sidebar_agent_chat", lang)}: {agent_count} {msg_word}</p>
            <p style="margin:2px 0;">{t("sidebar_assist_chat", lang)}: {assist_count} {msg_word}</p>
        </div>
        """, unsafe_allow_html=True)

        # Credits
        st.markdown("""
        <div style="text-align:center;padding-top:1.5rem;">
            <p style="color:#475569;font-size:0.65rem;">
                Powered by Gemini + Groq + CLIP<br>
                © 2026 IliaChan TechWell
            </p>
        </div>
        """, unsafe_allow_html=True)

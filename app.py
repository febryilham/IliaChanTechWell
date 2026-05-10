"""
IliaChan TechWell — Main Landing Page
Technology × Wellness Education Platform
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import streamlit as st
from config import PAGE_TITLE, PAGE_ICON
from components.animations import (
    inject_global_styles, inject_particle_background,
    inject_typing_effect, inject_glow_card, inject_tips_typewriter,
)
from components.sidebar import render_sidebar, render_top_nav
from database.init_db import init_database
from i18n import t, get_tips

# ── Page Configuration ──────────────────────────────────────────────────
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Initialize ──────────────────────────────────────────────────────────
inject_global_styles()
inject_particle_background()
render_sidebar()
render_top_nav()
init_database()

lang = st.session_state.get("app_lang", "id")

# ── Hero Section ────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:2rem 0 1rem 0;">
    <div style="font-size:4rem;margin-bottom:0.5rem;">🩺</div>
</div>
""", unsafe_allow_html=True)

inject_typing_effect("IliaChan TechWell — Technology × Wellness")

st.markdown(f"""
<div style="text-align:center;max-width:700px;margin:0 auto;">
    <p style="
        color:#94a3b8;font-size:1.05rem;line-height:1.8;
        margin-top:0.5rem;
    ">
        {t("hero_subtitle", lang)}
    </p>
</div>
<br>
""", unsafe_allow_html=True)

# ── Looping Tips Typewriter ─────────────────────────────────────────────
inject_tips_typewriter(get_tips(lang))

# ── Stats Bar ───────────────────────────────────────────────────────────
st.markdown(f"""
<div style="
    display:flex;justify-content:center;gap:2rem;flex-wrap:wrap;
    margin:1rem 0 2rem 0;
">
    <div style="text-align:center;">
        <div style="font-size:1.8rem;font-weight:700;color:#06b6d4;">8+</div>
        <div style="font-size:0.75rem;color:#64748b;">{t("stat_topics", lang)}</div>
    </div>
    <div style="text-align:center;">
        <div style="font-size:1.8rem;font-weight:700;color:#a855f7;">14+</div>
        <div style="font-size:0.75rem;color:#64748b;">{t("stat_refs", lang)}</div>
    </div>
    <div style="text-align:center;">
        <div style="font-size:1.8rem;font-weight:700;color:#ec4899;">2</div>
        <div style="font-size:0.75rem;color:#64748b;">{t("stat_bots", lang)}</div>
    </div>
    <div style="text-align:center;">
        <div style="font-size:1.8rem;font-weight:700;color:#10b981;">RAG</div>
        <div style="font-size:0.75rem;color:#64748b;">CLIP + SQLite</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Navigation Cards ───────────────────────────────────────────────────
st.markdown(f"""
<h3 style="
    text-align:center;color:#e2e8f0;font-family:'Outfit',sans-serif;
    margin-bottom:1rem;font-size:1.2rem;
">{t("explore_title", lang)}</h3>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    inject_glow_card(
        title=t("card_agent_title", lang),
        description=t("card_agent_desc", lang),
        icon="🤖", color="#06b6d4",
    )
    if st.button(t("card_agent_btn", lang), key="goto_agent", use_container_width=True):
        st.switch_page("pages/1_Agent_Chat.py")

with col2:
    inject_glow_card(
        title=t("card_assist_title", lang),
        description=t("card_assist_desc", lang),
        icon="💬", color="#a855f7",
    )
    if st.button(t("card_assist_btn", lang), key="goto_assistant", use_container_width=True):
        st.switch_page("pages/2_Assistant_Chat.py")

with col3:
    inject_glow_card(
        title=t("card_topics_title", lang),
        description=t("card_topics_desc", lang),
        icon="📊", color="#10b981",
    )
    if st.button(t("card_topics_btn", lang), key="goto_topics", use_container_width=True):
        st.switch_page("pages/3_Health_Topics.py")

# ── Target Audience Section ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"""
<div style="
    background:rgba(17,24,39,0.6);backdrop-filter:blur(20px);
    border:1px solid rgba(255,255,255,0.06);border-radius:20px;
    padding:1.5rem;margin-top:1rem;
">
    <h3 style="color:#e2e8f0;font-family:'Outfit',sans-serif;text-align:center;margin-bottom:1rem;">
        {t("audience_title", lang)}
    </h3>
    <div style="display:flex;gap:1rem;flex-wrap:wrap;justify-content:center;">
        <div style="
            background:rgba(6,182,212,0.08);border:1px solid rgba(6,182,212,0.15);
            border-radius:12px;padding:0.8rem 1.2rem;text-align:center;flex:1;min-width:200px;
        ">
            <div style="font-size:1.5rem;margin-bottom:0.3rem;">🏠</div>
            <h4 style="color:#06b6d4;font-size:0.9rem;margin:0;">{t("audience_remote", lang)}</h4>
            <p style="color:#64748b;font-size:0.75rem;margin:0.3rem 0 0 0;">{t("audience_remote_desc", lang)}</p>
        </div>
        <div style="
            background:rgba(168,85,247,0.08);border:1px solid rgba(168,85,247,0.15);
            border-radius:12px;padding:0.8rem 1.2rem;text-align:center;flex:1;min-width:200px;
        ">
            <div style="font-size:1.5rem;margin-bottom:0.3rem;">🏢</div>
            <h4 style="color:#a855f7;font-size:0.9rem;margin:0;">{t("audience_office", lang)}</h4>
            <p style="color:#64748b;font-size:0.75rem;margin:0.3rem 0 0 0;">{t("audience_office_desc", lang)}</p>
        </div>
        <div style="
            background:rgba(236,72,153,0.08);border:1px solid rgba(236,72,153,0.15);
            border-radius:12px;padding:0.8rem 1.2rem;text-align:center;flex:1;min-width:200px;
        ">
            <div style="font-size:1.5rem;margin-bottom:0.3rem;">📱</div>
            <h4 style="color:#ec4899;font-size:0.9rem;margin:0;">{t("audience_native", lang)}</h4>
            <p style="color:#64748b;font-size:0.75rem;margin:0.3rem 0 0 0;">{t("audience_native_desc", lang)}</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Footer ──────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="text-align:center;padding:2rem 0 1rem 0;color:#475569;font-size:0.75rem;">
    <p>{t("footer_powered", lang)}</p>
    <p>{t("footer_copy", lang)}</p>
</div>
""", unsafe_allow_html=True)

"""
IliaChan TechWell — About / Tentang
Final Project information and credits.
Uses st.html() for guaranteed HTML rendering.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
from config import PAGE_TITLE
from components.animations import inject_global_styles
from components.sidebar import render_sidebar, render_top_nav
from i18n import t

st.set_page_config(page_title=f"{PAGE_TITLE} — About", page_icon="ℹ️", layout="wide")
inject_global_styles()
render_sidebar()
render_top_nav()

lang = st.session_state.get("app_lang", "id")

# ── Header ──────────────────────────────────────────────────────────────
st.html(f"""
<div style="text-align:center;padding:1.5rem 0;">
    <div style="font-size:3.5rem;margin-bottom:0.5rem;">🩺</div>
    <h1 style="
        font-family:'Outfit',sans-serif;font-size:2.4rem;
        background:linear-gradient(135deg,#06b6d4,#a855f7,#ec4899);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent;
        margin:0;
    ">IliaChan TechWell</h1>
    <p style="color:#64748b;font-size:0.95rem;margin-top:0.3rem;">
        {t("about_tagline", lang)}
    </p>
</div>
""")

# ── Final Project Info ──────────────────────────────────────────────────
st.html(f"""
<div style="
    background:rgba(17,24,39,0.6);backdrop-filter:blur(20px);
    border:1px solid rgba(6,182,212,0.2);border-radius:20px;
    padding:2rem;margin:1rem auto;max-width:800px;
">
    <div style="text-align:center;margin-bottom:1.5rem;">
        <span style="
            display:inline-block;padding:6px 20px;border-radius:20px;
            background:linear-gradient(135deg,rgba(6,182,212,0.12),rgba(168,85,247,0.12));
            border:1px solid rgba(6,182,212,0.3);
            color:#06b6d4;font-size:0.8rem;font-weight:600;
            text-transform:uppercase;letter-spacing:2px;
        ">{t("about_badge", lang)}</span>
    </div>
    <h2 style="color:#e2e8f0;font-family:'Outfit',sans-serif;text-align:center;
        font-size:1.5rem;margin:0 0 1rem 0;">
        {t("about_fp_title", lang)}
    </h2>
    <p style="color:#cbd5e1;font-size:0.95rem;line-height:1.8;text-align:center;
        max-width:650px;margin:0 auto;">
        {t("about_fp_desc", lang)}
    </p>
    
    <div style="text-align:center; margin-top: 1.5rem;">
        <a href="#" target="_blank" style="
            display: inline-block; padding: 10px 24px; border-radius: 8px;
            background: linear-gradient(135deg, #06b6d4, #a855f7);
            color: white; font-weight: 600; text-decoration: none;
            font-family: 'Inter', sans-serif; box-shadow: 0 4px 15px rgba(168,85,247,0.3);
            transition: transform 0.2s ease;
        ">🌐 Kunjungi Live Demo</a>
        <p style="color:#64748b; font-size:0.7rem; margin-top: 8px;">
            *(Link akan aktif setelah deployment ke Streamlit Cloud)*
        </p>
    </div>
</div>
""")

# ── Author ──────────────────────────────────────────────────────────────
st.html(f"""
<div style="
    background:rgba(17,24,39,0.6);backdrop-filter:blur(20px);
    border:1px solid rgba(168,85,247,0.2);border-radius:20px;
    padding:2rem;margin:1rem auto;max-width:800px;
">
    <div style="text-align:center;">
        <div style="
            width:80px;height:80px;border-radius:50%;margin:0 auto 1rem auto;
            background:linear-gradient(135deg,#06b6d4,#a855f7);
            display:flex;align-items:center;justify-content:center;
            font-size:2.2rem;box-shadow:0 0 30px rgba(6,182,212,0.3);
        ">👨‍💻</div>
        <h3 style="color:#e2e8f0;font-family:'Outfit',sans-serif;margin:0;font-size:1.4rem;">
            Ilham Febri Tri Suharno
        </h3>
        <p style="color:#06b6d4;font-size:0.85rem;margin:4px 0 0 0;">{t("about_author_role", lang)}</p>
    </div>
</div>
""")

# ── Tech Stack ──────────────────────────────────────────────────────────
st.html(f"""
<div style="
    background:rgba(17,24,39,0.6);backdrop-filter:blur(20px);
    border:1px solid rgba(255,255,255,0.06);border-radius:20px;
    padding:2rem;margin:1rem auto;max-width:800px;
">
    <h3 style="color:#e2e8f0;font-family:'Outfit',sans-serif;text-align:center;
        margin:0 0 1.2rem 0;">{t("about_tech_title", lang)}</h3>
    <div style="display:flex;flex-wrap:wrap;gap:0.8rem;justify-content:center;">
        <div style="background:rgba(6,182,212,0.1);border:1px solid rgba(6,182,212,0.25);
            border-radius:12px;padding:0.6rem 1rem;text-align:center;min-width:140px;">
            <div style="font-size:1.3rem;">🐍</div>
            <p style="color:#06b6d4;font-size:0.8rem;font-weight:600;margin:4px 0 0 0;">Python</p>
            <p style="color:#64748b;font-size:0.65rem;margin:0;">Backend &amp; Logic</p>
        </div>
        <div style="background:rgba(168,85,247,0.1);border:1px solid rgba(168,85,247,0.25);
            border-radius:12px;padding:0.6rem 1rem;text-align:center;min-width:140px;">
            <div style="font-size:1.3rem;">🌐</div>
            <p style="color:#a855f7;font-size:0.8rem;font-weight:600;margin:4px 0 0 0;">Streamlit</p>
            <p style="color:#64748b;font-size:0.65rem;margin:0;">Web Frontend</p>
        </div>
        <div style="background:rgba(236,72,153,0.1);border:1px solid rgba(236,72,153,0.25);
            border-radius:12px;padding:0.6rem 1rem;text-align:center;min-width:140px;">
            <div style="font-size:1.3rem;">🤖</div>
            <p style="color:#ec4899;font-size:0.8rem;font-weight:600;margin:4px 0 0 0;">Gemini 2.5 Flash</p>
            <p style="color:#64748b;font-size:0.65rem;margin:0;">AI Chat &amp; Vision</p>
        </div>
        <div style="background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.25);
            border-radius:12px;padding:0.6rem 1rem;text-align:center;min-width:140px;">
            <div style="font-size:1.3rem;">⚡</div>
            <p style="color:#10b981;font-size:0.8rem;font-weight:600;margin:4px 0 0 0;">Groq</p>
            <p style="color:#64748b;font-size:0.65rem;margin:0;">RAG Processing</p>
        </div>
        <div style="background:rgba(245,158,11,0.1);border:1px solid rgba(245,158,11,0.25);
            border-radius:12px;padding:0.6rem 1rem;text-align:center;min-width:140px;">
            <div style="font-size:1.3rem;">🖼️</div>
            <p style="color:#f59e0b;font-size:0.8rem;font-weight:600;margin:4px 0 0 0;">CLIP</p>
            <p style="color:#64748b;font-size:0.65rem;margin:0;">Image Embeddings</p>
        </div>
        <div style="background:rgba(99,102,241,0.1);border:1px solid rgba(99,102,241,0.25);
            border-radius:12px;padding:0.6rem 1rem;text-align:center;min-width:140px;">
            <div style="font-size:1.3rem;">🗄️</div>
            <p style="color:#6366f1;font-size:0.8rem;font-weight:600;margin:4px 0 0 0;">SQLite</p>
            <p style="color:#64748b;font-size:0.65rem;margin:0;">Database</p>
        </div>
        <div style="background:rgba(244,63,94,0.1);border:1px solid rgba(244,63,94,0.25);
            border-radius:12px;padding:0.6rem 1rem;text-align:center;min-width:140px;">
            <div style="font-size:1.3rem;">🔗</div>
            <p style="color:#f43f5e;font-size:0.8rem;font-weight:600;margin:4px 0 0 0;">Ngrok</p>
            <p style="color:#64748b;font-size:0.65rem;margin:0;">Tunnel</p>
        </div>
    </div>
</div>
""")

# ── Project Description ─────────────────────────────────────────────────
st.html(f"""
<div style="
    background:rgba(17,24,39,0.6);backdrop-filter:blur(20px);
    border:1px solid rgba(255,255,255,0.06);border-radius:20px;
    padding:2rem;margin:1rem auto;max-width:800px;
">
    <h3 style="color:#e2e8f0;font-family:'Outfit',sans-serif;text-align:center;
        margin:0 0 1rem 0;">{t("about_project_title", lang)}</h3>
    <p style="color:#cbd5e1;font-size:0.9rem;line-height:1.8;">
        {t("about_project_p1", lang)}
    </p>
    <p style="color:#cbd5e1;font-size:0.9rem;line-height:1.8;margin-top:0.8rem;">
        {t("about_project_p2", lang)}
    </p>
    <p style="color:#cbd5e1;font-size:0.9rem;line-height:1.8;margin-top:0.8rem;">
        {t("about_project_p3", lang)}
    </p>
</div>
""")

# ── Footer ──────────────────────────────────────────────────────────────
st.html(f"""
<div style="text-align:center;padding:2rem 0 1rem 0;">
    <p style="color:#475569;font-size:0.75rem;">
        {t("footer_copy", lang)}<br>
        {t("footer_author", lang)}
    </p>
</div>
""")

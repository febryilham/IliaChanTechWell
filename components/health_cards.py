"""
IliaChan TechWell — Health Topic Cards Component
Card gallery for displaying health education topics.
"""

import streamlit as st
from pathlib import Path
from config import IMAGES_DIR


CATEGORY_COLORS = {
    "Ergonomics": "#06b6d4",
    "Posture": "#a855f7",
    "Sedentary": "#ec4899",
    "Eye Health": "#f59e0b",
    "Sleep Hygiene": "#6366f1",
    "Lifestyle": "#10b981",
    "Hearing Health": "#f43f5e",
}

CATEGORY_ICONS = {
    "Ergonomics": "🪑",
    "Posture": "🧍",
    "Sedentary": "🛋️",
    "Eye Health": "👁️",
    "Sleep Hygiene": "🌙",
    "Lifestyle": "🍽️",
    "Hearing Health": "🎧",
}

RISK_BADGES = {
    "HIGH": ("🔴", "#ef4444"),
    "MEDIUM": ("🟡", "#f59e0b"),
    "LOW": ("🟢", "#10b981"),
}


def render_topic_card(topic: dict, show_detail_button: bool = True):
    """Render a single health topic card."""
    color = CATEGORY_COLORS.get(topic["category"], "#06b6d4")
    icon = CATEGORY_ICONS.get(topic["category"], "📋")
    risk_icon, risk_color = RISK_BADGES.get(topic["risk_level"], ("⚪", "#94a3b8"))

    # Check for topic image
    img_path = IMAGES_DIR / topic.get("image_filename", "")
    has_image = img_path.exists()

    st.markdown(f"""
    <div style="
        background:rgba(17,24,39,0.6);
        backdrop-filter:blur(20px);
        border:1px solid rgba(255,255,255,0.08);
        border-radius:16px;padding:1.2rem;
        transition:all 0.3s ease;
        margin-bottom:0.8rem;
    ">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
            <div style="display:flex;gap:0.6rem;align-items:center;">
                <span style="font-size:1.8rem;">{icon}</span>
                <div>
                    <h4 style="margin:0;color:#e2e8f0;font-size:1rem;font-weight:600;">
                        {topic['topic_name']}
                    </h4>
                    <span style="
                        display:inline-block;font-size:0.65rem;padding:2px 8px;
                        border-radius:20px;margin-top:4px;
                        background:{color}20;color:{color};border:1px solid {color}40;
                    ">{topic['category']}</span>
                </div>
            </div>
            <span style="
                font-size:0.7rem;padding:2px 8px;border-radius:12px;
                background:{risk_color}20;color:{risk_color};
                border:1px solid {risk_color}40;
            ">{risk_icon} {topic['risk_level']}</span>
        </div>
        <p style="color:#94a3b8;font-size:0.82rem;line-height:1.5;margin:0.8rem 0 0 0;">
            {topic['description'][:150]}...
        </p>
    </div>
    """, unsafe_allow_html=True)

    if show_detail_button:
        return st.button(
            f"📖 Detail: {topic['topic_name'][:30]}...",
            key=f"detail_{topic['id']}",
            use_container_width=True,
        )
    return False


def render_topic_detail(topic: dict, journals: list = None, recommendations: list = None, lang: str = "id"):
    """Render detailed view of a health topic."""
    from i18n import t
    color = CATEGORY_COLORS.get(topic["category"], "#06b6d4")
    icon = CATEGORY_ICONS.get(topic["category"], "📋")

    st.markdown(f"""
    <div style="
        background:rgba(17,24,39,0.6);backdrop-filter:blur(20px);
        border:1px solid {color}30;border-radius:20px;padding:1.5rem;margin-bottom:1rem;
    ">
        <div style="display:flex;align-items:center;gap:0.8rem;margin-bottom:1rem;">
            <span style="font-size:2.5rem;">{icon}</span>
            <h2 style="margin:0;color:#e2e8f0;font-family:'Outfit',sans-serif;">
                {topic['topic_name']}
            </h2>
        </div>
        <p style="color:#cbd5e1;font-size:0.92rem;line-height:1.7;">
            {topic['description']}
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div style="background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.2);
             border-radius:14px;padding:1rem;">
            <h4 style="color:#ef4444;margin:0 0 0.5rem 0;">{t("topics_risk", lang)}</h4>
            <p style="color:#fca5a5;font-size:0.85rem;line-height:1.6;margin:0;">
                {topic['risks']}
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="background:rgba(245,158,11,0.08);border:1px solid rgba(245,158,11,0.2);
             border-radius:14px;padding:1rem;">
            <h4 style="color:#f59e0b;margin:0 0 0.5rem 0;">{t("topics_symptoms", lang)}</h4>
            <p style="color:#fcd34d;font-size:0.85rem;line-height:1.6;margin:0;">
                {topic['symptoms']}
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.2);
         border-radius:14px;padding:1rem;margin-top:0.8rem;">
        <h4 style="color:#10b981;margin:0 0 0.5rem 0;">{t("topics_solutions", lang)}</h4>
        <p style="color:#6ee7b7;font-size:0.85rem;line-height:1.6;margin:0;">
            {topic['solutions']}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Journals
    if journals:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"### {t('topics_journals', lang)}")
        for j in journals:
            source_badge = {
                "journal": "📄",
                "who": "🏥",
                "government": "🏛️",
                "news": "📰",
                "social_media": "📱",
            }.get(j.get("source_type", ""), "📋")

            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.03);border-radius:10px;
                 padding:0.8rem;margin:0.4rem 0;border-left:3px solid {color};">
                <p style="margin:0;color:#e2e8f0;font-size:0.85rem;font-weight:500;">
                    {source_badge} {j['title']}
                </p>
                <p style="margin:2px 0;color:#94a3b8;font-size:0.75rem;">
                    {j.get('authors','')} ({j.get('year','')}) — {j.get('source','')}
                </p>
                <p style="margin:4px 0 0 0;color:#cbd5e1;font-size:0.8rem;">
                    {j.get('summary','')}
                </p>
            </div>
            """, unsafe_allow_html=True)

    # Recommendations
    if recommendations:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"### {t('topics_recs', lang)}")
        for r in recommendations:
            diff_colors = {"easy": "#10b981", "medium": "#f59e0b", "hard": "#ef4444"}
            dc = diff_colors.get(r.get("difficulty", ""), "#94a3b8")
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.03);border-radius:10px;
                 padding:0.8rem;margin:0.4rem 0;">
                <p style="margin:0;color:#e2e8f0;font-size:0.85rem;">
                    ▸ {r['recommendation']}
                </p>
                <div style="display:flex;gap:1rem;margin-top:4px;">
                    <span style="font-size:0.7rem;color:{dc};
                        background:{dc}15;padding:1px 8px;border-radius:10px;">
                        {r.get('difficulty','').upper()}</span>
                    <span style="font-size:0.7rem;color:#64748b;">
                        ⏱️ {r.get('time_required','')}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

"""
IliaChan TechWell — Assistant Chat Page
Reactive health consultation with RAG + SQL + Image analysis.
Camera only activates when user clicks the button.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
from PIL import Image
from config import PAGE_TITLE
from components.animations import inject_global_styles
from components.chat_ui import render_chat_message, render_chat_header
from components.sidebar import render_sidebar, render_top_nav
from chatbot.assistant import HealthAssistant
from database.init_db import init_database
from i18n import t

st.set_page_config(page_title=f"{PAGE_TITLE} — Konsultasi", page_icon="💬", layout="wide")
inject_global_styles()
render_sidebar()
render_top_nav()

lang = st.session_state.get("app_lang", "id")

# Ensure database exists
init_database()

# Header
render_chat_header(
    title=t("assist_title", lang),
    subtitle=t("assist_subtitle", lang),
    icon="💬",
    status_color="#10b981",
)

# Initialize assistant
assistant = HealthAssistant()

# Preloaded topic from Agent redirect
preloaded = st.session_state.get("current_topic")
if preloaded and preloaded not in ("redirect_suggested", None):
    st.info(f"{t('assist_from_agent', lang)}: **{preloaded}**")

# ── Image upload section (always at top, persistent) ────────────────────
if "assistant_image" not in st.session_state:
    st.session_state.assistant_image = None
if "camera_active" not in st.session_state:
    st.session_state.camera_active = False

with st.expander(t("assist_upload_title", lang), expanded=False):
    st.markdown(f"""
    <p style="color:#94a3b8;font-size:0.85rem;">
        {t("assist_upload_desc", lang)}
    </p>
    """, unsafe_allow_html=True)

    img_tab1, img_tab2 = st.tabs([t("assist_tab_upload", lang), t("assist_tab_camera", lang)])

    with img_tab1:
        uploaded_file = st.file_uploader(
            t("assist_choose_file", lang),
            type=["jpg", "jpeg", "png", "webp"],
            key="assistant_upload",
        )
        if uploaded_file:
            st.session_state.assistant_image = Image.open(uploaded_file)

    with img_tab2:
        # Camera only activates after explicit button click
        if not st.session_state.camera_active:
            st.markdown(f"""
            <p style="color:#94a3b8;font-size:0.85rem;">
                {"Klik tombol di bawah untuk mengaktifkan kamera." if lang == "id"
                 else "Click the button below to activate camera."}
            </p>
            """, unsafe_allow_html=True)
            if st.button(t("assist_camera_btn", lang), use_container_width=True, key="activate_cam"):
                st.session_state.camera_active = True
                st.rerun()
        else:
            camera_photo = st.camera_input(t("assist_camera_label", lang))
            if camera_photo:
                st.session_state.assistant_image = Image.open(camera_photo)
                st.session_state.camera_active = False
            if st.button("❌ Tutup Kamera" if lang == "id" else "❌ Close Camera",
                         use_container_width=True, key="deactivate_cam"):
                st.session_state.camera_active = False
                st.rerun()

    # Show preview of current image
    if st.session_state.assistant_image is not None:
        st.image(
            st.session_state.assistant_image,
            caption=t("assist_photo_caption", lang),
            use_container_width=True,
        )
        if st.button(t("assist_remove_photo", lang), use_container_width=True):
            st.session_state.assistant_image = None
            st.rerun()

# Check consultation status
if not st.session_state.get("consultation_active", True):
    st.success(t("assist_done", lang))
    if st.button(t("assist_new", lang), use_container_width=True):
        assistant.clear_history()
        st.session_state.assistant_image = None
        st.rerun()
else:
    # Display chat history
    chat_container = st.container()
    with chat_container:
        for msg in assistant.get_chat_history():
            render_chat_message(msg["role"], msg["content"], chat_type="assistant")

    # Chat input
    user_input = st.chat_input(t("assist_input", lang))
    if user_input:
        image_to_analyze = st.session_state.assistant_image

        render_chat_message("user", user_input, chat_type="assistant")

        with st.spinner(t("assist_analyzing", lang)):
            reply = assistant.send_message(user_input, image=image_to_analyze)

        render_chat_message("assistant", reply, chat_type="assistant")
        st.rerun()

    # Clear button
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button(t("assist_reset", lang), use_container_width=True):
            assistant.clear_history()
            st.session_state.assistant_image = None
            st.rerun()

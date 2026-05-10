"""
IliaChan TechWell — Internationalization (i18n)
Dual language support: Indonesian (default) and English.
"""

TRANSLATIONS = {
    "id": {
        # ── Top Nav ─────────────────────────────────────────────────
        "nav_home": "🏠 Beranda",
        "nav_agent": "🤖 Agent",
        "nav_assistant": "💬 Konsultasi",
        "nav_topics": "📊 Topik",
        "nav_about": "ℹ️ Tentang",
        "lang_label": "🌐 Bahasa",

        # ── Sidebar ─────────────────────────────────────────────────
        "sidebar_tagline": "Technology × Wellness Education",
        "sidebar_nav": "Navigasi",
        "sidebar_tip_title": "💡 Tips Kesehatan",
        "sidebar_tip_btn": "🔄 Tips Baru",
        "sidebar_stats": "📊 Statistik Sesi",
        "sidebar_agent_chat": "Agent Chat",
        "sidebar_assist_chat": "Assistant Chat",
        "sidebar_msg": "pesan",

        # ── Landing Page ────────────────────────────────────────────
        "hero_subtitle": "Platform edukasi kesehatan interaktif untuk pekerja digital. "
                         "Didukung oleh <strong style='color:#06b6d4;'>AI Iliachan</strong> — entitas bio-organik "
                         "dari abad ke-30 yang hadir untuk membantu Anda memahami dampak "
                         "kebiasaan teknologi terhadap kesehatan tubuh.",
        "stat_topics": "Topik Kesehatan",
        "stat_refs": "Referensi Jurnal",
        "stat_bots": "AI Chatbot",
        "explore_title": "Mulai Jelajahi",
        "card_agent_title": "Agent Chat",
        "card_agent_desc": "Ngobrol dengan Iliachan — AI proaktif yang akan menanyakan kebiasaan teknologi Anda dan memberikan insight kesehatan.",
        "card_agent_btn": "▶ Mulai Chat Agent",
        "card_assist_title": "Konsultasi Kesehatan",
        "card_assist_desc": "Konsultasi mendalam dengan AI Assistant. Upload foto postur, dapatkan analisis dan rekomendasi berbasis jurnal.",
        "card_assist_btn": "▶ Mulai Konsultasi",
        "card_topics_title": "Topik Kesehatan",
        "card_topics_desc": "Jelajahi 8+ topik kesehatan digital lengkap dengan risiko, gejala, solusi, dan referensi jurnal ilmiah.",
        "card_topics_btn": "▶ Lihat Topik",
        "audience_title": "🎯 Siapa yang Membutuhkan Ini?",
        "audience_remote": "Pekerja Remote",
        "audience_remote_desc": "Work from home tanpa setup ergonomis yang tepat",
        "audience_office": "Pekerja Kantor",
        "audience_office_desc": "8+ jam di depan layar setiap hari",
        "audience_native": "Digital Native",
        "audience_native_desc": "Hidup bersandingkan gadget tanpa sadar dampaknya",

        # ── Agent Chat ──────────────────────────────────────────────
        "agent_title": "Iliachan — Health Agent",
        "agent_subtitle": "Online • Entitas bio-organik dari abad ke-30",
        "agent_greeting_spinner": "Iliachan sedang menyapa...",
        "agent_redirect": "💡 Iliachan menyarankan konsultasi mendalam. Klik halaman **Konsultasi** di navbar untuk pembahasan lebih detail!",
        "agent_input": "Ketik pesan Anda ke Iliachan...",
        "agent_typing": "Iliachan sedang mengetik...",
        "agent_reset": "🗑️ Reset Percakapan",

        # ── Assistant Chat ──────────────────────────────────────────
        "assist_title": "Health Assistant — Konsultasi",
        "assist_subtitle": "Online • RAG-powered health consultation",
        "assist_upload_title": "📸 Upload / Ambil Foto untuk Analisis",
        "assist_upload_desc": "Upload foto atau ambil foto langsung dari kamera untuk analisis postur dan rekomendasi personal dari AI.",
        "assist_tab_upload": "📁 Upload File",
        "assist_tab_camera": "📷 Kamera",
        "assist_choose_file": "Pilih gambar",
        "assist_camera_btn": "📷 Aktifkan Kamera",
        "assist_camera_label": "Ambil foto dari kamera",
        "assist_photo_caption": "📌 Foto yang akan dianalisis",
        "assist_remove_photo": "❌ Hapus Foto",
        "assist_done": "✅ Konsultasi selesai! Terima kasih telah menggunakan IliaChan TechWell.",
        "assist_new": "🔄 Mulai Konsultasi Baru",
        "assist_from_agent": "📋 Topik dari Agent Chat",
        "assist_input": "Tanyakan tentang kesehatan digital Anda...",
        "assist_analyzing": "Health Assistant sedang menganalisis...",
        "assist_reset": "🗑️ Reset Konsultasi",

        # ── Health Topics ───────────────────────────────────────────
        "topics_title": "📊 Perpustakaan Topik Kesehatan",
        "topics_subtitle": "Jelajahi topik kesehatan digital dan temukan solusi untuk kebiasaan teknologi Anda",
        "topics_filter": "🔍 Filter Kategori",
        "topics_all": "Semua",
        "topics_no_db": "Database belum diinisialisasi.",
        "topics_risk": "⚠️ Risiko Kesehatan",
        "topics_symptoms": "🔍 Gejala Awal",
        "topics_solutions": "✅ Solusi & Rekomendasi",
        "topics_journals": "📚 Referensi Jurnal",
        "topics_recs": "💡 Rekomendasi Praktis",
        "topics_ask_assist": "💬 Tanyakan ke Assistant",
        "topics_chat_agent": "🤖 Chat dengan Iliachan",
        "topics_back": "⬅️ Kembali ke Gallery",

        # ── About Page ──────────────────────────────────────────────
        "about_tagline": "Technology × Wellness Education Platform",
        "about_badge": "Final Project",
        "about_fp_title": "📋 Tugas Akhir — Final Project",
        "about_fp_desc": "Proyek ini dibuat sebagai pemenuhan <strong style='color:#06b6d4;'>'Final Project'</strong> "
                         "tugas akhir yang bertujuan untuk mengukur pemahaman peserta terhadap keseluruhan materi. "
                         "Peserta diharapkan mampu mengimplementasikan konsep yang telah dipelajari ke dalam sebuah "
                         "proyek yang relevan dan aplikatif.",
        "about_author_role": "Author / Developer",
        "about_tech_title": "🛠️ Technology Stack",
        "about_project_title": "📖 Tentang Proyek",
        "about_project_p1": "<strong style='color:#06b6d4;'>IliaChan TechWell</strong> adalah platform edukasi kesehatan "
                            "digital interaktif yang menargetkan pekerja remote, pekerja kantor, dan individu yang "
                            "rutinitasnya selalu bersandingkan dengan perangkat pintar di sekitarnya tanpa tahu efek "
                            "buruk berlebihan yang tanpa disadari merusak tubuh secara bertahap.",
        "about_project_p2": "Aplikasi ini menggunakan karakter AI bernama <strong style='color:#a855f7;'>\"Iliachan\"</strong> "
                            "— sebuah entitas bio-organik canggih dari peradaban masa depan abad ke-30 — yang bertugas "
                            "memberikan hasil analisa mendalam tentang acuh terhadap gaya hidup teknologi anomali, "
                            "melakukan pengecekan berdasarkan hasil sumber terkait masalah, lalu mencoba untuk memberikan "
                            "perbaikan, rekomendasi, dan solusi yang valid.",
        "about_project_p3": "Fitur utama mencakup: <strong style='color:#10b981;'>Dual AI Chatbot</strong> (proaktif + reaktif), "
                            "<strong style='color:#f59e0b;'>RAG Pipeline</strong> dengan CLIP embeddings, "
                            "<strong style='color:#ec4899;'>analisis foto</strong> via Gemini Vision, "
                            "dan <strong style='color:#6366f1;'>database kesehatan</strong> dengan 8 topik, "
                            "14 referensi jurnal, dan 19 rekomendasi praktis.",

        # ── Footer ──────────────────────────────────────────────────
        "footer_powered": "Powered by Gemini 2.5 Flash Lite • Groq • CLIP • Streamlit",
        "footer_copy": "© 2026 IliaChan TechWell — Technology × Wellness Education",
        "footer_author": "Built with ❤️ by Ilham Febri Tri Suharno",
    },

    "en": {
        # ── Top Nav ─────────────────────────────────────────────────
        "nav_home": "🏠 Home",
        "nav_agent": "🤖 Agent",
        "nav_assistant": "💬 Consult",
        "nav_topics": "📊 Topics",
        "nav_about": "ℹ️ About",
        "lang_label": "🌐 Language",

        # ── Sidebar ─────────────────────────────────────────────────
        "sidebar_tagline": "Technology × Wellness Education",
        "sidebar_nav": "Navigation",
        "sidebar_tip_title": "💡 Health Tip",
        "sidebar_tip_btn": "🔄 New Tip",
        "sidebar_stats": "📊 Session Stats",
        "sidebar_agent_chat": "Agent Chat",
        "sidebar_assist_chat": "Assistant Chat",
        "sidebar_msg": "messages",

        # ── Landing Page ────────────────────────────────────────────
        "hero_subtitle": "Interactive health education platform for digital workers. "
                         "Powered by <strong style='color:#06b6d4;'>AI Iliachan</strong> — a bio-organic entity "
                         "from the 30th century, here to help you understand the impact of "
                         "technology habits on your health.",
        "stat_topics": "Health Topics",
        "stat_refs": "Journal References",
        "stat_bots": "AI Chatbots",
        "explore_title": "Start Exploring",
        "card_agent_title": "Agent Chat",
        "card_agent_desc": "Chat with Iliachan — a proactive AI that asks about your tech habits and gives health insights.",
        "card_agent_btn": "▶ Start Agent Chat",
        "card_assist_title": "Health Consultation",
        "card_assist_desc": "In-depth consultation with AI Assistant. Upload posture photos, get analysis and journal-based recommendations.",
        "card_assist_btn": "▶ Start Consultation",
        "card_topics_title": "Health Topics",
        "card_topics_desc": "Explore 8+ digital health topics with risks, symptoms, solutions, and scientific journal references.",
        "card_topics_btn": "▶ View Topics",
        "audience_title": "🎯 Who Needs This?",
        "audience_remote": "Remote Workers",
        "audience_remote_desc": "Working from home without proper ergonomic setup",
        "audience_office": "Office Workers",
        "audience_office_desc": "8+ hours in front of screens every day",
        "audience_native": "Digital Natives",
        "audience_native_desc": "Living with gadgets without realizing the effects",

        # ── Agent Chat ──────────────────────────────────────────────
        "agent_title": "Iliachan — Health Agent",
        "agent_subtitle": "Online • Bio-organic entity from the 30th century",
        "agent_greeting_spinner": "Iliachan is greeting you...",
        "agent_redirect": "💡 Iliachan recommends a deeper consultation. Click the **Consult** page in navbar for more details!",
        "agent_input": "Type your message to Iliachan...",
        "agent_typing": "Iliachan is typing...",
        "agent_reset": "🗑️ Reset Conversation",

        # ── Assistant Chat ──────────────────────────────────────────
        "assist_title": "Health Assistant — Consultation",
        "assist_subtitle": "Online • RAG-powered health consultation",
        "assist_upload_title": "📸 Upload / Take Photo for Analysis",
        "assist_upload_desc": "Upload a photo or take one directly from your camera for posture analysis and personal AI recommendations.",
        "assist_tab_upload": "📁 Upload File",
        "assist_tab_camera": "📷 Camera",
        "assist_choose_file": "Choose image",
        "assist_camera_btn": "📷 Activate Camera",
        "assist_camera_label": "Take photo from camera",
        "assist_photo_caption": "📌 Photo to be analyzed",
        "assist_remove_photo": "❌ Remove Photo",
        "assist_done": "✅ Consultation complete! Thank you for using IliaChan TechWell.",
        "assist_new": "🔄 Start New Consultation",
        "assist_from_agent": "📋 Topic from Agent Chat",
        "assist_input": "Ask about your digital health...",
        "assist_analyzing": "Health Assistant is analyzing...",
        "assist_reset": "🗑️ Reset Consultation",

        # ── Health Topics ───────────────────────────────────────────
        "topics_title": "📊 Health Topics Library",
        "topics_subtitle": "Explore digital health topics and find solutions for your technology habits",
        "topics_filter": "🔍 Filter Category",
        "topics_all": "All",
        "topics_no_db": "Database not initialized.",
        "topics_risk": "⚠️ Health Risks",
        "topics_symptoms": "🔍 Early Symptoms",
        "topics_solutions": "✅ Solutions & Recommendations",
        "topics_journals": "📚 Journal References",
        "topics_recs": "💡 Practical Recommendations",
        "topics_ask_assist": "💬 Ask Assistant",
        "topics_chat_agent": "🤖 Chat with Iliachan",
        "topics_back": "⬅️ Back to Gallery",

        # ── About Page ──────────────────────────────────────────────
        "about_tagline": "Technology × Wellness Education Platform",
        "about_badge": "Final Project",
        "about_fp_title": "📋 Final Project — Capstone",
        "about_fp_desc": "This project is created as a fulfillment of the <strong style='color:#06b6d4;'>'Final Project'</strong> "
                         "capstone aimed at measuring participants' understanding of all course materials. "
                         "Participants are expected to implement the concepts learned into a "
                         "relevant and applicable project.",
        "about_author_role": "Author / Developer",
        "about_tech_title": "🛠️ Technology Stack",
        "about_project_title": "📖 About the Project",
        "about_project_p1": "<strong style='color:#06b6d4;'>IliaChan TechWell</strong> is an interactive digital health "
                            "education platform targeting remote workers, office workers, and individuals whose "
                            "routines are always accompanied by smart devices without realizing the excessive "
                            "harmful effects that gradually damage the body.",
        "about_project_p2": "This application uses an AI character named <strong style='color:#a855f7;'>\"Iliachan\"</strong> "
                            "— a sophisticated bio-organic entity from the 30th century civilization — tasked with "
                            "providing in-depth analysis about neglecting anomalous technology lifestyle, "
                            "checking based on relevant source results, and providing "
                            "repairs, recommendations, and valid solutions.",
        "about_project_p3": "Key features include: <strong style='color:#10b981;'>Dual AI Chatbot</strong> (proactive + reactive), "
                            "<strong style='color:#f59e0b;'>RAG Pipeline</strong> with CLIP embeddings, "
                            "<strong style='color:#ec4899;'>photo analysis</strong> via Gemini Vision, "
                            "and <strong style='color:#6366f1;'>health database</strong> with 8 topics, "
                            "14 journal references, and 19 practical recommendations.",

        # ── Footer ──────────────────────────────────────────────────
        "footer_powered": "Powered by Gemini 2.5 Flash Lite • Groq • CLIP • Streamlit",
        "footer_copy": "© 2026 IliaChan TechWell — Technology × Wellness Education",
        "footer_author": "Built with ❤️ by Ilham Febri Tri Suharno",
    },
}

HEALTH_TIPS = {
    "id": [
        "💡 Setiap 20 menit, lihat objek sejauh 20 kaki selama 20 detik (aturan 20-20-20).",
        "🧘 Lakukan stretching leher dan bahu setiap 30 menit saat bekerja.",
        "💧 Minum minimal 8 gelas air per hari untuk menjaga hidrasi.",
        "🌙 Matikan gadget 1 jam sebelum tidur untuk kualitas tidur yang lebih baik.",
        "🪑 Pastikan kaki Anda menapak rata di lantai saat duduk.",
        "👁️ Aktifkan mode gelap dan night shift di semua perangkat Anda.",
        "🎧 Gunakan headphone dengan volume maksimal 60% selama maksimal 60 menit.",
        "🚶 Berdiri dan berjalan minimal 5 menit setiap jam.",
        "🍎 Hindari makan di tempat tidur, selalu makan di meja makan.",
        "💡 Pasang bias lighting di belakang monitor untuk mengurangi strain mata.",
    ],
    "en": [
        "💡 Every 20 minutes, look at an object 20 feet away for 20 seconds (20-20-20 rule).",
        "🧘 Stretch your neck and shoulders every 30 minutes while working.",
        "💧 Drink at least 8 glasses of water per day to stay hydrated.",
        "🌙 Turn off gadgets 1 hour before bed for better sleep quality.",
        "🪑 Make sure your feet are flat on the floor when sitting.",
        "👁️ Enable dark mode and night shift on all your devices.",
        "🎧 Use headphones at max 60% volume for no more than 60 minutes.",
        "🚶 Stand up and walk for at least 5 minutes every hour.",
        "🍎 Avoid eating in bed, always eat at a table.",
        "💡 Install bias lighting behind your monitor to reduce eye strain.",
    ],
}


def t(key: str, lang: str = "id") -> str:
    """Get translated text by key."""
    return TRANSLATIONS.get(lang, TRANSLATIONS["id"]).get(key, key)


def get_tips(lang: str = "id") -> list:
    """Get health tips for the current language."""
    return HEALTH_TIPS.get(lang, HEALTH_TIPS["id"])

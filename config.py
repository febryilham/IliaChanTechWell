"""
IliaChan TechWell — Configuration Management
Loads API keys and initializes clients for Gemini, Groq, and CLIP.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# ── Load Environment Variables ──────────────────────────────────────────
load_dotenv(Path(__file__).parent / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
NGROK_AUTH_TOKEN = os.getenv("NGROK_AUTH_TOKEN", "")

# ── Project Paths ───────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).parent
DATABASE_PATH = PROJECT_ROOT / "database" / "health_education.db"
ASSETS_DIR = PROJECT_ROOT / "assets"
IMAGES_DIR = ASSETS_DIR / "images"
CSS_DIR = ASSETS_DIR / "css"
JS_DIR = ASSETS_DIR / "js"

# ── Model Configuration ────────────────────────────────────────────────
GEMINI_MODEL = "gemini-2.5-flash-lite"
GROQ_MODEL = "llama-3.3-70b-versatile"
CLIP_MODEL = "openai/clip-vit-base-patch32"

# ── Streamlit Page Config ──────────────────────────────────────────────
PAGE_TITLE = "IliaChan TechWell"
PAGE_ICON = "🩺"
LAYOUT = "wide"

# ── Client Initialization Helpers ──────────────────────────────────────
_gemini_client = None
_groq_client = None


def get_gemini_client():
    """Get or create Gemini client (singleton)."""
    global _gemini_client
    if _gemini_client is None:
        from google import genai
        _gemini_client = genai.Client(api_key=GEMINI_API_KEY)
    return _gemini_client


def get_groq_client():
    """Get or create Groq client (singleton)."""
    global _groq_client
    if _groq_client is None:
        from groq import Groq
        _groq_client = Groq(api_key=GROQ_API_KEY)
    return _groq_client

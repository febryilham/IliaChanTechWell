"""
IliaChan TechWell — Setup & Run with Ngrok Tunnel
Installs dependencies, initializes database, and creates public tunnel.
"""

import subprocess
import sys
import os
import time
import signal
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent


def install_dependencies():
    """Install Python dependencies from requirements.txt."""
    req_file = PROJECT_ROOT / "requirements.txt"
    print("📦 Installing dependencies...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "-r", str(req_file), "-q"
    ])
    print("✅ Dependencies installed.")


def init_db():
    """Initialize the SQLite database."""
    sys.path.insert(0, str(PROJECT_ROOT))
    from database.init_db import init_database
    print("🗄️ Initializing database...")
    init_database()


def start_streamlit():
    """Start Streamlit server as a subprocess."""
    print("🚀 Starting Streamlit server on port 8501...")
    env = os.environ.copy()
    process = subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", str(PROJECT_ROOT / "app.py"),
         "--server.port", "8501",
         "--server.headless", "true",
         "--theme.base", "dark",
         "--theme.primaryColor", "#06b6d4",
         "--theme.backgroundColor", "#0a0e1a",
         "--theme.secondaryBackgroundColor", "#111827",
         "--theme.textColor", "#e2e8f0",
         "--browser.gatherUsageStats", "false"],
        env=env,
        cwd=str(PROJECT_ROOT),
    )
    return process


def create_ngrok_tunnel():
    """Create Ngrok tunnel to expose Streamlit."""
    from dotenv import load_dotenv
    load_dotenv(PROJECT_ROOT / ".env")

    token = os.getenv("NGROK_AUTH_TOKEN", "")
    if not token:
        print("⚠️ NGROK_AUTH_TOKEN not found in .env file.")
        print("  Streamlit running locally at: http://localhost:8501")
        return None

    try:
        from pyngrok import ngrok
        ngrok.set_auth_token(token)
        tunnel = ngrok.connect(8501)
        public_url = tunnel.public_url
        print(f"\n{'='*60}")
        print(f"🌐 PUBLIC URL: {public_url}")
        print(f"{'='*60}")
        print(f"📋 Share this URL to access the app from anywhere!")
        print(f"🔒 Local:  http://localhost:8501")
        print(f"{'='*60}\n")
        return tunnel
    except Exception as e:
        print(f"⚠️ Ngrok tunnel failed: {e}")
        print("  Streamlit running locally at: http://localhost:8501")
        return None


def main():
    print("""
    ╔══════════════════════════════════════════╗
    ║   🩺 IliaChan TechWell                   ║
    ║   Technology × Wellness Education        ║
    ╚══════════════════════════════════════════╝
    """)

    # Step 1: Install dependencies
    try:
        install_dependencies()
    except Exception as e:
        print(f"❌ Failed to install dependencies: {e}")
        return

    # Step 2: Initialize database
    try:
        init_db()
    except Exception as e:
        print(f"❌ Failed to initialize database: {e}")
        return

    # Step 3: Start Streamlit
    st_process = start_streamlit()
    time.sleep(3)  # Wait for Streamlit to start

    # Step 4: Create Ngrok tunnel
    tunnel = create_ngrok_tunnel()

    # Keep running
    print("Press Ctrl+C to stop the server.\n")
    try:
        st_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")
        st_process.terminate()
        if tunnel:
            from pyngrok import ngrok
            ngrok.disconnect(tunnel.public_url)
            ngrok.kill()
        print("👋 Goodbye!")


if __name__ == "__main__":
    main()

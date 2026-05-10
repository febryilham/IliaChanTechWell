"""
IliaChan TechWell — Animation Components
Injects custom CSS/JS animations into Streamlit via st.html().
"""

import streamlit as st


def inject_global_styles():
    """Inject global dark theme, smooth transitions, custom cursor, animated bg."""
    st.html("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap');

        :root {
            --bg-primary: #0a0e1a;
            --bg-secondary: #111827;
            --bg-card: rgba(17, 24, 39, 0.8);
            --text-primary: #e2e8f0;
            --text-secondary: #94a3b8;
            --accent-cyan: #06b6d4;
            --accent-purple: #a855f7;
            --accent-pink: #ec4899;
            --accent-green: #10b981;
            --accent-amber: #f59e0b;
            --glass-bg: rgba(255, 255, 255, 0.05);
            --glass-border: rgba(255, 255, 255, 0.1);
        }

        /* ── Base ──────────────────────────────── */
        .stApp {
            font-family: 'Inter', sans-serif !important;
        }

        /* ── Hide ALL Streamlit default UI ────── */
        #MainMenu, footer, header,
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        .stDeployButton,
        button[kind="header"],
        div[data-testid="stAppDeployButton"],
        div[data-testid="stMainMenu"] {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            position: fixed !important;
            z-index: -9999 !important;
        }

        /* ── Layout ───────────────────────────── */
        .block-container {
            padding-top: 1rem !important;
            max-width: 1200px !important;
        }

        /* ── Animated gradient background ─────── */
        .stApp > div:first-child {
            background:
                radial-gradient(ellipse at 20% 50%, rgba(6,182,212,0.08) 0%, transparent 50%),
                radial-gradient(ellipse at 80% 20%, rgba(168,85,247,0.06) 0%, transparent 50%),
                radial-gradient(ellipse at 50% 80%, rgba(236,72,153,0.05) 0%, transparent 50%);
            animation: bg-drift 20s ease-in-out infinite alternate;
        }
        @keyframes bg-drift {
            0%   { background-position: 0% 0%, 100% 0%, 50% 100%; }
            50%  { background-position: 30% 60%, 70% 40%, 20% 50%; }
            100% { background-position: 60% 30%, 40% 70%, 80% 20%; }
        }

        /* ── Smooth page transitions ─────────── */
        .stApp [data-testid="stAppViewContainer"] {
            animation: fadeSlideIn 0.4s ease-out;
        }
        @keyframes fadeSlideIn {
            from { opacity: 0; transform: translateY(8px); }
            to   { opacity: 1; transform: translateY(0); }
        }

        /* ── Sidebar smooth toggle ───────────── */
        section[data-testid="stSidebar"] {
            transition: transform 0.4s cubic-bezier(0.4,0,0.2,1),
                        opacity 0.3s ease !important;
        }
        section[data-testid="stSidebar"][aria-expanded="false"] {
            transform: translateX(-100%);
            opacity: 0;
        }

        /* ── Custom scrollbar ────────────────── */
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: var(--bg-primary); }
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, var(--accent-cyan), var(--accent-purple));
            border-radius: 3px;
        }

    </style>
    """)


def inject_particle_background():
    """Inject animated particle background."""
    st.html("""
    <div id="particles-bg" style="position:fixed;top:0;left:0;width:100%;height:100%;z-index:-1;pointer-events:none;overflow:hidden;"></div>
    <script>
    (function(){
        const canvas = document.createElement('canvas');
        canvas.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:-1;pointer-events:none;';
        const container = document.getElementById('particles-bg');
        if(!container) return;
        container.appendChild(canvas);
        const ctx = canvas.getContext('2d');
        let w, h, particles = [];

        function resize(){
            w = canvas.width = window.innerWidth;
            h = canvas.height = window.innerHeight;
        }
        resize();
        window.addEventListener('resize', resize);

        const colors = ['#06b6d4','#a855f7','#ec4899','#10b981','#f59e0b'];
        const icons = ['💊','🩺','❤️','🧬','👁️','🦴','🧠','💪'];

        for(let i=0; i<40; i++){
            particles.push({
                x: Math.random()*w, y: Math.random()*h,
                vx: (Math.random()-0.5)*0.5, vy: (Math.random()-0.5)*0.5,
                size: Math.random()*3+1, alpha: Math.random()*0.5+0.1,
                color: colors[Math.floor(Math.random()*colors.length)]
            });
        }

        function draw(){
            ctx.clearRect(0,0,w,h);
            particles.forEach(p=>{
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.size, 0, Math.PI*2);
                ctx.fillStyle = p.color;
                ctx.globalAlpha = p.alpha;
                ctx.fill();

                p.x += p.vx; p.y += p.vy;
                if(p.x<0||p.x>w) p.vx*=-1;
                if(p.y<0||p.y>h) p.vy*=-1;
            });

            // Draw connections
            ctx.globalAlpha = 0.03;
            ctx.strokeStyle = '#06b6d4';
            for(let i=0;i<particles.length;i++){
                for(let j=i+1;j<particles.length;j++){
                    const dx=particles[i].x-particles[j].x;
                    const dy=particles[i].y-particles[j].y;
                    if(Math.sqrt(dx*dx+dy*dy)<150){
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x,particles[i].y);
                        ctx.lineTo(particles[j].x,particles[j].y);
                        ctx.stroke();
                    }
                }
            }
            ctx.globalAlpha=1;
            requestAnimationFrame(draw);
        }
        draw();
    })();
    </script>
    """)


def inject_typing_effect(text: str, element_id: str = "typing-text"):
    """Inject a static title (no typing, reliable render)."""
    st.markdown(f"""
    <div style="text-align:center;margin:1rem 0;">
        <span style="
            font-family:'Outfit',sans-serif;font-size:2rem;font-weight:700;
            background:linear-gradient(135deg,#06b6d4,#a855f7,#ec4899);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
            background-clip:text;
        ">{text}</span>
    </div>
    """, unsafe_allow_html=True)


def inject_tips_typewriter(tips: list, element_id: str = "tips-typewriter"):
    """Inject a looping typewriter that cycles through health tips.
    Uses st.components.v1.html for proper JS execution.
    """
    import json
    import streamlit.components.v1 as components

    tips_json = json.dumps(tips, ensure_ascii=False)

    html_code = """<!DOCTYPE html>
<html>
<head>
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  body {
    background: transparent;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100%;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  }
  .tw-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
  }
  .tw-icon { font-size: 0.85rem; color: #64748b; }
  .tw-text {
    font-size: 0.95rem;
    color: #94a3b8;
    min-width: 10px;
  }
  .tw-cursor {
    display: inline-block;
    width: 2px;
    height: 1.1rem;
    background: linear-gradient(180deg, #06b6d4, #a855f7);
    animation: twBlink 0.8s step-end infinite;
    vertical-align: middle;
  }
  @keyframes twBlink {
    0%, 50% { opacity: 1; }
    51%, 100% { opacity: 0; }
  }
</style>
</head>
<body>
<div class="tw-container">
  <span class="tw-icon">💡</span>
  <span class="tw-text" id="tw-text"></span>
  <span class="tw-cursor"></span>
</div>
<script>
(function(){
  var tips = """ + tips_json + """;
  var el = document.getElementById("tw-text");
  if(!el || !tips.length) return;
  var tipIdx = 0, charIdx = 0, isDeleting = false;
  function tick(){
    var currentTip = tips[tipIdx];
    if (!isDeleting) {
      el.textContent = currentTip.substring(0, charIdx + 1);
      charIdx++;
      if (charIdx >= currentTip.length) {
        isDeleting = true;
        setTimeout(tick, 3000);
        return;
      }
      setTimeout(tick, 40);
    } else {
      el.textContent = currentTip.substring(0, charIdx - 1);
      charIdx--;
      if (charIdx <= 0) {
        isDeleting = false;
        tipIdx = (tipIdx + 1) % tips.length;
        setTimeout(tick, 500);
        return;
      }
      setTimeout(tick, 25);
    }
  }
  tick();
})();
</script>
</body>
</html>"""

    components.html(html_code, height=45, scrolling=False)


def inject_glow_card(title: str, description: str, icon: str, color: str, link: str = ""):
    """Render a glowing card with hover effect."""
    card_id = title.replace(" ", "-").lower()
    st.html(f"""
    <div id="card-{card_id}" style="
        background: rgba(17,24,39,0.6);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 2rem;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.4,0,0.2,1);
        position: relative;
        overflow: hidden;
    " onmouseover="
        this.style.transform='translateY(-4px)';
        this.style.borderColor='{color}40';
        this.style.boxShadow='0 20px 40px {color}20';
    " onmouseout="
        this.style.transform='translateY(0)';
        this.style.borderColor='rgba(255,255,255,0.08)';
        this.style.boxShadow='none';
    ">
        <div style="font-size:2.5rem;margin-bottom:0.8rem;">{icon}</div>
        <h3 style="
            font-family:'Outfit',sans-serif;font-size:1.3rem;font-weight:600;
            color:#e2e8f0;margin:0 0 0.5rem 0;
        ">{title}</h3>
        <p style="color:#94a3b8;font-size:0.9rem;line-height:1.6;margin:0;">
            {description}
        </p>
        <div style="
            position:absolute;top:-50%;right:-50%;width:100%;height:100%;
            background:radial-gradient(circle,{color}08 0%,transparent 70%);
            pointer-events:none;
        "></div>
    </div>
    """)


def inject_pulse_dot(color: str = "#10b981"):
    """Inject a pulsing online indicator dot."""
    return f"""
    <span style="
        display:inline-block;width:8px;height:8px;border-radius:50%;
        background:{color};margin-right:6px;
        animation:pulse-dot 2s ease-in-out infinite;
    "></span>
    <style>
    @keyframes pulse-dot {{
        0%,100%{{ box-shadow:0 0 0 0 {color}80; }}
        50%{{ box-shadow:0 0 0 8px {color}00; }}
    }}
    </style>
    """

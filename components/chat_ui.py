"""
IliaChan TechWell — Chat UI Components
Custom styled chat bubbles and message rendering.
"""

import streamlit as st
from datetime import datetime


def render_chat_message(role: str, content: str, chat_type: str = "agent"):
    """Render a styled chat bubble."""
    is_user = role == "user"

    if is_user:
        avatar = "👤"
        name = "Anda"
        bg = "linear-gradient(135deg, #7c3aed, #a855f7)"
        align = "flex-end"
        border_color = "#a855f740"
    else:
        if chat_type == "agent":
            avatar = "🤖"
            name = "Iliachan"
            bg = "linear-gradient(135deg, #0e7490, #06b6d4)"
            border_color = "#06b6d440"
        else:
            avatar = "💬"
            name = "Health Assistant"
            bg = "linear-gradient(135deg, #065f46, #10b981)"
            border_color = "#10b98140"
        align = "flex-start"

    timestamp = datetime.now().strftime("%H:%M")

    st.markdown(f"""
    <div style="display:flex;justify-content:{align};margin:0.5rem 0;">
        <div style="
            max-width:80%;
            background:{bg if is_user else 'rgba(17,24,39,0.7)'};
            backdrop-filter:blur(10px);
            border:1px solid {border_color};
            border-radius:{'18px 18px 4px 18px' if is_user else '18px 18px 18px 4px'};
            padding:0.8rem 1.1rem;
            color:#e2e8f0;
            font-size:0.92rem;
            line-height:1.6;
            box-shadow:0 4px 15px rgba(0,0,0,0.2);
        ">
            <div style="display:flex;align-items:center;gap:6px;margin-bottom:4px;">
                <span style="font-size:1.1rem;">{avatar}</span>
                <span style="font-size:0.75rem;font-weight:600;color:#94a3b8;">{name}</span>
                <span style="font-size:0.65rem;color:#64748b;margin-left:auto;">{timestamp}</span>
            </div>
            <div>{_format_content(content)}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_typing_indicator(chat_type: str = "agent"):
    """Render a typing indicator animation."""
    name = "Iliachan" if chat_type == "agent" else "Health Assistant"
    avatar = "🤖" if chat_type == "agent" else "💬"
    st.markdown(f"""
    <div style="display:flex;justify-content:flex-start;margin:0.5rem 0;">
        <div style="
            background:rgba(17,24,39,0.7);
            backdrop-filter:blur(10px);
            border:1px solid rgba(255,255,255,0.08);
            border-radius:18px 18px 18px 4px;
            padding:0.8rem 1.2rem;
            box-shadow:0 4px 15px rgba(0,0,0,0.2);
        ">
            <div style="display:flex;align-items:center;gap:6px;margin-bottom:6px;">
                <span>{avatar}</span>
                <span style="font-size:0.75rem;font-weight:600;color:#94a3b8;">{name}</span>
            </div>
            <div style="display:flex;gap:4px;padding:4px 0;">
                <span class="typing-dot" style="animation-delay:0s"></span>
                <span class="typing-dot" style="animation-delay:0.2s"></span>
                <span class="typing-dot" style="animation-delay:0.4s"></span>
            </div>
        </div>
    </div>
    <style>
    .typing-dot {{
        width:8px;height:8px;border-radius:50%;
        background:#06b6d4;
        animation:typing-bounce 1.4s ease-in-out infinite;
    }}
    @keyframes typing-bounce {{
        0%,60%,100%{{transform:translateY(0);opacity:0.4;}}
        30%{{transform:translateY(-8px);opacity:1;}}
    }}
    </style>
    """, unsafe_allow_html=True)


def render_chat_header(title: str, subtitle: str, icon: str, status_color: str = "#10b981"):
    """Render chat page header."""
    st.markdown(f"""
    <div style="
        background:rgba(17,24,39,0.6);
        backdrop-filter:blur(20px);
        border:1px solid rgba(255,255,255,0.08);
        border-radius:16px;
        padding:1.2rem 1.5rem;
        margin-bottom:1rem;
        display:flex;align-items:center;gap:1rem;
    ">
        <div style="font-size:2.5rem;">{icon}</div>
        <div>
            <h2 style="
                font-family:'Outfit',sans-serif;margin:0;font-size:1.3rem;
                color:#e2e8f0;font-weight:600;
            ">{title}</h2>
            <p style="margin:0;font-size:0.85rem;color:#94a3b8;display:flex;align-items:center;gap:4px;">
                <span style="
                    display:inline-block;width:8px;height:8px;border-radius:50%;
                    background:{status_color};
                    box-shadow:0 0 8px {status_color};
                "></span>
                {subtitle}
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)


def _format_content(content: str) -> str:
    """Format message content with basic markdown support."""
    import re
    # Bold
    content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
    # Bullet points
    content = content.replace('\n- ', '\n<br>• ')
    content = content.replace('\n* ', '\n<br>• ')
    # Numbered lists
    content = re.sub(r'\n(\d+)\. ', r'\n<br>\1. ', content)
    # Line breaks
    content = content.replace('\n', '<br>')
    return content

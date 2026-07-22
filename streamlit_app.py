"""Juego arcade sencillo, inspirado en Geometry Dash, para Streamlit."""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


APP_VERSION = "2.2.0"


st.set_page_config(
    page_title="Neon Dash",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        .stApp { background: #080b1a; }
        header, footer { visibility: hidden; }
        .block-container { padding: 1rem 1rem 0; max-width: 1180px; }
        [data-testid="stToolbar"] { display: none; }
        .build-badge {
            position: fixed;
            z-index: 9999;
            top: .55rem;
            right: .75rem;
            padding: .35rem .65rem;
            border: 1px solid #70f6ff66;
            border-radius: 999px;
            color: #70f6ff;
            background: #080b1ae6;
            font: 700 .72rem/1 sans-serif;
            letter-spacing: .08em;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f'<div class="build-badge">NEON DASH · BUILD {APP_VERSION}</div>',
    unsafe_allow_html=True,
)

game_html = (Path(__file__).parent / "neon_dash_v2.html").read_text(encoding="utf-8")
components.html(game_html, height=760, scrolling=False)

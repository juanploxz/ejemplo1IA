"""Juego arcade sencillo, inspirado en Geometry Dash, para Streamlit."""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


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
    </style>
    """,
    unsafe_allow_html=True,
)

game_html = (Path(__file__).parent / "game.html").read_text(encoding="utf-8")
components.html(game_html, height=760, scrolling=False)

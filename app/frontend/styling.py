import streamlit as st

def apply_custom_styles():
    custom_css = """
    <style>

    /* ---------- PAGE ---------- */
    body {
        background-color: #0e1117;
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }

    /* ---------- TITLES ---------- */
    h1, h2, h3, h4, h5 {
        color: #03dac6;
        font-weight: 700;
    }

    /* ---------- SUBHEADER ---------- */
    .st-emotion-cache-10trblm {
        color: #bb86fc;
    }

    /* ---------- INPUT LABELS ---------- */
    label {
        font-size: 16px !important;
        font-weight: 600 !important;
    }

    /* ---------- BUTTONS ---------- */
    .stButton button {
        background: linear-gradient(90deg, #6200ee, #3700b3);
        color: white;
        padding: 10px 25px;
        border-radius: 10px;
        border: none;
        font-size: 16px;
        font-weight: 600;
        transition: 0.3s;
    }

    .stButton button:hover {
        background: linear-gradient(90deg, #3700b3, #6200ee);
        transform: scale(1.03);
    }

    /* ---------- TEXT AREA ---------- */
    textarea {
        background-color: #1f1f1f !important;
        color: #ffffff !important;
        border-radius: 10px !important;
        border: 1px solid #444 !important;
        font-size: 16px !important;
        padding: 10px !important;
    }

    /* ---------- SELECTBOX ---------- */
    .stSelectbox div {
        background-color: #1f1f1f !important;
        color: white !important;
        border-radius: 8px !important;
    }

    /* ---------- SIDEBAR ---------- */
    section[data-testid="stSidebar"] {
        background-color: #121212 !important;
        border-right: 1px solid #333;
    }

    /* ---------- IMAGE PREVIEWS ---------- */
    img {
        border-radius: 10px;
        border: 1px solid #333;
    }

    </style>
    """

    st.markdown(custom_css, unsafe_allow_html=True)


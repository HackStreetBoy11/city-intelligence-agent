# utils/styles.py

import streamlit as st

def load_css():

    st.markdown("""
    <style>

    /* Main App */
    .stApp {
        background-color: #0E1117;
        color: white;
    }

    /* Title */
    h1 {
        color: #4CAF50;
        font-weight: 700;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #161B22;
    }

    /* Chat Input */
    .stChatInputContainer {
        border-top: 1px solid #333;
    }

    /* User Chat Bubble */
    div[data-testid="stChatMessageContent"] {
        border-radius: 12px;
        padding: 10px;
    }

    /* Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px;
        font-weight: 600;
    }

    .stButton>button:hover {
        background-color: #45a049;
    }

    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-thumb {
        background: #4CAF50;
        border-radius: 10px;
    }

    /* Markdown Text */
    p {
        font-size: 16px;
    }

    </style>
    """, unsafe_allow_html=True)

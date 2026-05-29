# app.py

import streamlit as st
from agent import run_agent
from utils.styles import load_css

st.set_page_config(
    page_title="City Intelligence Agent",
    page_icon="🌍",
    layout="wide"
)

load_css()

st.title("🌍 City Intelligence AI Agent")
st.markdown("Real-time weather + internet search powered by AI")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.header("⚡ Features")

    st.markdown("""
    - 🌦 Weather Information
    - 🌐 Web Search
    - 🤖 AI Agent
    - 🧠 Human-in-the-loop
    """)

    st.divider()

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask anything about cities, weather, news...")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = run_agent(user_input)

            st.markdown(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
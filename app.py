import streamlit as st
import os
from agent import query_agent
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(BASE_DIR, "assets", "img", "design-logo-juice-store.png")

logo = Image.open(logo_path)

st.set_page_config(page_title="Chat Lojinha Sucos & Sanduíches", page_icon="🥪", layout="centered")
st.markdown(
  """
  <style>
    body {
        font-family: 'Roboto', sans-serif;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .st-emotion-cache-8atqhb {
        width: 100%;
        display: flex;
        justify-content: center;
    }
    .title {
    text-align: center;
    color: #D94F00;
    font-size: 36px;
    font-weight: 700;
    margin-bottom: 5px;
    }å
    .subtitle {
      text-align: center;
      color: #6B4C3B;
      font-size: 16px;
      margin-top: 0;
      margin-bottom: 20px;
    }
  </style>
  """,
  unsafe_allow_html=True,
)

st.image(logo, width=400)

st.markdown('<h1 class="title">Lojinha Sucos & Sanduíches</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Converse com nosso assistente virtual!</p>', unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []

for role, message in st.session_state.history:
    with st.chat_message(role):
        st.markdown(message)

if prompt := st.chat_input("Pergunte algo sobre o cardápio ou sobre a nossa loja:"):
    st.session_state.history.append(("user", prompt))

    with st.chat_message("assistant"):
        with st.spinner("Estamos preparando a resposta..."):
            response = query_agent(f"Responda sempre em português: {prompt}")
            st.markdown(response)

    st.session_state.history.append(("assistant", response))

    st.rerun()

import streamlit as st
import os
from agent import query_agent
from PIL import Image

st.set_page_config(page_title="Chat Lojinha Sucos & Sanduíches", layout="centered")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(BASE_DIR, "assets", "img", "design-logo-juice-store.png")

logo = Image.open(logo_path)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
    
    .st-emotion-cache-8atqhb {
        width: 100%;
        display: flex;
        justify-content: center;
    }

    .logo {
      display: block;
      margin-left: auto;
      margin-right: auto;
      width: 450px;
    }
    body, .css-18e3th9 {
        font-family: 'Roboto', sans-serif;
        background-color: #FFF8F0;
    }
    .title {
        text-align: center;
        color: #D94F00;
        font-size: 36px;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .subtitle {
        text-align: center;
        color: #6B4C3B;
        font-size: 16px;
        margin-top: 0;
        margin-bottom: 20px;
    }
    .chat-box {
        background-color: #fff3e0; /* laranja bem claro */
        padding: 20px;
        border-radius: 15px;
        max-height: 420px;
        overflow-y: auto;
        margin-bottom: 20px;
        border: 2px solid #D94F00;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    .user-msg {
        color: #D94F00;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .bot-msg {
      color: #5A3E2B;
      margin-bottom: 10px;
      font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

st.image(logo, use_container_width=False, width=400, caption=None)

st.markdown('<h1 class="title">Lojinha Sucos & Sanduíches</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Converse com nosso assistente virtual!</p>', unsafe_allow_html=True)

if st.button("Limpar conversa"):
  st.session_state.history = []

if "history" not in st.session_state:
  st.session_state.history = []

input_text = st.text_input("Pergunte algo sobre o cardápio ou sobre a nossa loja:")

if input_text:
  response = query_agent(input_text)
  st.session_state.history.append(("Você", input_text))
  st.session_state.history.append(("Lojinha", response))

for speaker, text in st.session_state.history:
  if speaker == "Você":
    st.markdown(f"**{speaker}:** {text}")
  else:
    st.markdown(f"**{speaker}:** {text}")
      


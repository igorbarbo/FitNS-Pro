import streamlit as st
from pages import dashboard, treino, nutricao, progresso

# Configuração da página
st.set_page_config(page_title="FitNS Pro", layout="wide")

# CSS customizado
st.markdown(
    """
    <style>
    body {background-color: #0e1117;}
    h1,h2,h3,h4,h5,h6 {color: #4da6ff;}
    .stButton>button {
        background-color:#1f2937;
        color:white;
        border-radius:10px;
        height:3em;
        width:100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Navegação usando Sidebar
menu = st.sidebar.radio("Menu", ["Dashboard", "Treino", "Nutrição", "Progresso"])

# Mostra a página escolhida
if menu == "Dashboard":
    dashboard.show_dashboard()
elif menu == "Treino":
    treino.show_treino()
elif menu == "Nutrição":
    nutricao.show_nutricao()
elif menu == "Progresso":
    progresso.show_progresso()

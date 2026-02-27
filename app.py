import streamlit as st
import os

from pages import treino, nutricao, progresso

# Função para gerar caminho absoluto para CSVs
def get_data_path(filename):
    return os.path.join(os.path.dirname(__file__), "data", filename)

st.set_page_config(page_title="FitNS Pro", layout="wide")
st.title("FitNS Pro 💪")

menu_options = ["Dashboard", "Treino", "Nutrição", "Progresso"]
menu = st.sidebar.radio("Menu", menu_options)

if menu == "Dashboard":
    st.subheader("🏠 Dashboard")
    st.markdown("Resumo de treinos, nutrição e progresso")

elif menu == "Treino":
    st.subheader("💪 Treino")
    treino.show_treino(get_data_path)

elif menu == "Nutrição":
    st.subheader("🥗 Nutrição")
    nutricao.show_nutricao(get_data_path)

elif menu == "Progresso":
    st.subheader("📊 Progresso")
    progresso.show_progresso(get_data_path)

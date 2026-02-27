import streamlit as st
import os

# Importar páginas
from pages import treino, nutricao, progresso

# --- Função para criar caminho absoluto seguro para CSVs ---
def get_data_path(filename):
    return os.path.join(os.path.dirname(__file__), "data", filename)

# Configuração da página
st.set_page_config(page_title="FitNS Pro", layout="wide")

st.title("FitNS Pro 💪")

# Menu inferior tipo app nativo
menu_options = ["Dashboard", "Treino", "Nutrição", "Progresso"]
menu = st.sidebar.radio("Menu", menu_options)

# --- Dashboard ---
if menu == "Dashboard":
    st.subheader("🏠 Dashboard")
    st.markdown("Aqui vai o resumo de treinos, nutrição e progresso.")

# --- Treino ---
elif menu == "Treino":
    st.subheader("💪 Treino")
    treino.show_treino(get_data_path)

# --- Nutrição ---
elif menu == "Nutrição":
    st.subheader("🥗 Nutrição")
    nutricao.show_nutricao(get_data_path)

# --- Progresso ---
elif menu == "Progresso":
    st.subheader("📊 Progresso")
    progresso.show_progresso(get_data_path)

# app.py
import streamlit as st
from config import Config
from styles import load_css
from utils.services import FitnessService

# Configuração da página
st.set_page_config(
    page_title="FitNS Pro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Carrega o CSS customizado
load_css()

def init_session_state():
    """Inicializa as variáveis de estado da sessão"""
    if 'service' not in st.session_state:
        st.session_state.service = FitnessService()
    if 'user' not in st.session_state:
        st.session_state.user = st.session_state.service.store.get_current_user()
    if 'page' not in st.session_state:
        st.session_state.page = "dashboard"
    if 'show_add_meal' not in st.session_state:
        st.session_state.show_add_meal = False

# Inicializa a sessão ANTES de importar as páginas
init_session_state()

# Importa todas as páginas (com a sessão já pronta)
from pages import (
    login, 
    dashboard, 
    nutrition, 
    workout, 
    progress, 
    profile, 
    meal_plan,
    my_plan  # <-- NOVA PÁGINA ADICIONADA
)

# Roteamento das páginas
if st.session_state.user is None:
    # Se não há usuário logado, mostra a tela de login
    login.show()
else:
    # Usuário logado: navega entre as páginas
    page = st.session_state.page
    
    if page == "dashboard":
        dashboard.show()
    elif page == "nutrition":
        nutrition.show()
    elif page == "workout":
        workout.show()
    elif page == "progress":
        progress.show()
    elif page == "profile":
        profile.show()
    elif page == "meal_plan":
        meal_plan.show()
    elif page == "my_plan":  # <-- NOVA PÁGINA
        my_plan.show()
    else:
        # Página padrão caso algo dê errado
        dashboard.show()

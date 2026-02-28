# app.py
import streamlit as st
from config import Config
from styles import load_css
from utils.services import FitnessService
from pages import login, dashboard, nutrition, workout, progress, profile

# Configuração da página
st.set_page_config(
    page_title="FitNS Pro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

load_css()

def init_session_state():
    if 'service' not in st.session_state:
        st.session_state.service = FitnessService()
    if 'user' not in st.session_state:
        st.session_state.user = st.session_state.service.store.get_current_user()
    if 'page' not in st.session_state:
        st.session_state.page = "dashboard"
    if 'show_add_meal' not in st.session_state:
        st.session_state.show_add_meal = False

init_session_state()

# Roteamento das páginas
if st.session_state.user is None:
    login.show()
else:
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
    else:
        dashboard.show()

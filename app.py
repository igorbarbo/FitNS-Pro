# app.py
import streamlit as st
from config import Config
from styles import load_css
from utils.services import FitnessService
from pages import login, dashboard, nutrition, workout, progress, profile, meal_plan  # <-- adicione meal_plan

# ... (restante igual)

# Roteamento
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
    elif page == "meal_plan":          # <-- novo
        meal_plan.show()
    else:
        dashboard.show()

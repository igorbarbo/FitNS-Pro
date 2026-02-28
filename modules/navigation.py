# modules/navigation.py
import streamlit as st

def render_navigation():
    cols = st.columns(4)
    with cols[0]:
        if st.button("🏠 Início", use_container_width=True, key="nav_dashboard"):
            st.session_state.page = "dashboard"
            st.rerun()
    with cols[1]:
        if st.button("🏋️ Treino", use_container_width=True, key="nav_workout"):
            st.session_state.page = "workout"
            st.rerun()
    with cols[2]:
        if st.button("🥗 Nutrição", use_container_width=True, key="nav_nutrition"):
            st.session_state.page = "nutrition"
            st.rerun()
    with cols[3]:
        if st.button("🍽️ Plano", use_container_width=True, key="nav_meal_plan"):  # Novo
            st.session_state.page = "meal_plan"
            st.rerun()
    st.markdown("<br>", unsafe_allow_html=True)

    # Segunda linha opcional para Progresso e Perfil
    cols2 = st.columns(4)
    with cols2[0]:
        if st.button("📊 Perfil", use_container_width=True, key="nav_profile"):
            st.session_state.page = "profile"
            st.rerun()
    with cols2[1]:
        if st.button("📈 Progresso", use_container_width=True, key="nav_progress"):
            st.session_state.page = "progress"
            st.rerun()
    # as outras colunas ficam vazias (podem ser usadas depois)

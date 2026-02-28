# modules/navigation.py
import streamlit as st

def render_navigation():
    """
    Renderiza o menu de navegação inferior com 4 botões.
    Usa botões nativos do Streamlit para garantir a interatividade.
    """
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
        if st.button("📊 Perfil", use_container_width=True, key="nav_profile"):
            st.session_state.page = "profile"
            st.rerun()
    # Pequeno espaçamento antes do próximo conteúdo
    st.markdown("<br>", unsafe_allow_html=True)

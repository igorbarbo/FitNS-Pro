# modules/navigation.py
import streamlit as st

def render_navigation():
    """
    Renderiza o menu de navegação inferior com todos os botões.
    """
    # Primeira linha do menu (4 botões)
    cols = st.columns(4)
    
    with cols[0]:
        if st.button("🏠 Início", use_container_width=True, key="nav_dashboard"):
            st.session_state.page = "dashboard"
            st.rerun()
    
    with cols[1]:
        if st.button("🎯 Meu Plano", use_container_width=True, key="nav_my_plan"):
            st.session_state.page = "my_plan"
            st.rerun()
    
    with cols[2]:
        if st.button("🥗 Nutrição", use_container_width=True, key="nav_nutrition"):
            st.session_state.page = "nutrition"
            st.rerun()
    
    with cols[3]:
        if st.button("🍽️ Plano", use_container_width=True, key="nav_meal_plan"):
            st.session_state.page = "meal_plan"
            st.rerun()
    
    # Espaço entre as linhas
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Segunda linha do menu (mais 2 botões)
    cols2 = st.columns(4)
    
    with cols2[0]:
        if st.button("📊 Perfil", use_container_width=True, key="nav_profile"):
            st.session_state.page = "profile"
            st.rerun()
    
    with cols2[1]:
        if st.button("📈 Progresso", use_container_width=True, key="nav_progress"):
            st.session_state.page = "progress"
            st.rerun()
    
    # As outras colunas ficam vazias (para manter o layout)
    with cols2[2]:
        st.empty()
    
    with cols2[3]:
        st.empty()

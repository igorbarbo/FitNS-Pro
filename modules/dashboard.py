import streamlit as st
from modules.header import render_header
from modules.navigation import render_navigation
from modules.progress_bars import render_progress_bar

def show():
    # ... (código existente até o card do treino)
    
    # Botão que navega via URL (mais robusto)
    st.markdown("""
    <div style="text-align: center; margin-top: 10px;">
        <a href="/?page=workout" target="_self" class="btn-neon" style="text-decoration: none; padding: 12px 30px; display: inline-block;">
            🏋️ Iniciar Treino
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # ... (resto do código)"""
Dashboard Principal
"""
import streamlit as st
from utils.data_manager import load_json, initialize_data
from utils.calculations import calculate_bmi

def render_dashboard():
    """Renderiza o dashboard principal"""
    # Inicializa dados se necessário
    initialize_data()
    
    user_data = load_json("user_data.json")
    profile = user_data.get('profile', {})
    
    # Header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("🔥 FitNS Pro")
        st.markdown("**Seu completo sistema de fitness e nutrição**")
    with col2:
        if st.button("🔄 Resetar Dados"):
            import os
            from utils.data_manager import get_data_path
            try:
                os.remove(get_data_path("user_data.json"))
                st.success("Dados resetados!")
                st.rerun()
            except:
                pass
    
    st.markdown("---")
    
    if not profile:
        # Primeiro acesso
        st.markdown("""
        ## 👋 Bem-vindo ao FitNS Pro!
        
        Para começar, vá até a aba **⚖️ Balança** e configure seu perfil.
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Exercícios", "50+")
        with col2:
            st.metric("Alimentos", "40+")
        with col3:
            st.metric("Funcionalidades", "5 Módulos")
    else:
        # Dashboard com dados
        st.subheader(f"Olá! Seu objetivo: {profile.get('goal', 'manter').replace('_', ' ').title()}")
        
        # Cards resumo
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric("Peso Atual", f"{profile.get('current_weight', 0)} kg")
        with c2:
            st.metric("Meta", f"{profile.get('target_weight', 0)} kg")
        with c3:
            st.metric("Calorias/Dia", f"{profile.get('target_calories', 0)}")
        with c4:
            bmi = profile.get('bmi', {})
            st.metric("IMC", f"{bmi.get('bmi', 0)}", bmi.get('category', ''))
        
        # Acesso rápido
        st.markdown("### 🚀 Acesso Rápido")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            with st.container():
                st.markdown("**💪 Treino de Hoje**")
                st.write("Veja seu plano personalizado")
                st.button("Ir para Treino", key="btn_workout", use_container_width=True)
        
        with col2:
            with st.container():
                st.markdown("**🥗 Registrar Refeição**")
                st.write("Adicione alimentos ao diário")
                st.button("Ir para Nutrição", key="btn_nutrition", use_container_width=True)
        
        with col3:
            with st.container():
                st.markdown("**📊 Ver Progresso**")
                st.write("Gráficos e evolução")
                st.button("Ir para Progresso", key="btn_progress", use_container_width=True)
        
        # Dica do dia
        st.info("💡 **Dica do dia:** Mantenha consistência nos treinos. Resultados vêm da regularidade, não da perfeição!")
      

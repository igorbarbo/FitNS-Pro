# pages/progress.py
import streamlit as st
from modules.header import render_header
from modules.navigation import render_navigation

def show():
    user = st.session_state.user
    render_header(user)
    render_navigation()
    st.markdown('<div class="slide-in">', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <h2 style="margin:0; font-size: 24px;">📈 Progresso</h2>
        <p style="color: #8b8b9a; font-size: 12px; margin-top: 5px;">Acompanhe sua evolução</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <div style="font-size: 32px; font-weight: 800; color: #10b981;">+2.5kg</div>
            <div style="font-size: 11px; color: #8b8b9a; margin-top: 5px;">Ganho de Massa</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <div style="font-size: 32px; font-weight: 800; color: #00d4ff;">12</div>
            <div style="font-size: 11px; color: #8b8b9a; margin-top: 5px;">Treinos no Mês</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Aqui você pode adicionar mais gráficos e histórico
    st.markdown("""
    <div class="glass-card">
        <h4 style="margin-bottom: 15px;">Histórico de Peso</h4>
        <p style="color: #8b8b9a; text-align: center;">Em breve: gráfico detalhado de evolução</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

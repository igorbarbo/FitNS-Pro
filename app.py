"""
FitNS Pro - Versão Moderna v2.0
Design escuro com glassmorphism
"""
import streamlit as st
import time
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(
    page_title="FitNS Pro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS Customizado - Tema Escuro Moderno
st.markdown("""
<style>
    /* Reset e tema escuro global */
    .stApp {
        background: linear-gradient(135deg, #0a0a0f 0%, #12121a 50%, #1a1a2e 100%);
        color: #ffffff;
    }
    
    /* Esconder menu e footer padrão */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Glassmorphism cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 24px;
        margin: 12px 0;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    .glass-card:hover {
        border: 1px solid rgba(255, 255, 255, 0.15);
        transform: translateY(-2px);
        transition: all 0.3s ease;
    }
    
    /* Títulos */
    .main-title {
        font-size: 28px;
        font-weight: 700;
        background: linear-gradient(90deg, #00d4ff, #7b2cbf);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }
    
    .section-title {
        font-size: 14px;
        color: #8b8b9a;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 16px;
    }
    
    /* Métricas grandes */
    .metric-big {
        font-size: 42px;
        font-weight: 800;
        color: #ffffff;
        line-height: 1;
    }
    
    .metric-unit {
        font-size: 16px;
        color: #8b8b9a;
        font-weight: 400;
    }
    
    .metric-label {
        font-size: 12px;
        color: #6b6b7b;
        margin-top: 8px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Círculo de progresso */
    .progress-ring {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        background: conic-gradient(
            from 0deg,
            #00d4ff 0deg,
            #00d4ff calc(var(--progress) * 3.6deg),
            rgba(255,255,255,0.05) calc(var(--progress) * 3.6deg)
        );
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        margin: 0 auto;
    }
    
    .progress-ring::before {
        content: '';
        width: 90px;
        height: 90px;
        background: #0f0f1a;
        border-radius: 50%;
        position: absolute;
    }
    
    .progress-text {
        position: relative;
        z-index: 1;
        font-size: 24px;
        font-weight: 700;
        color: #00d4ff;
    }
    
    /* Barras de progresso */
    .progress-bar-bg {
        width: 100%;
        height: 8px;
        background: rgba(255,255,255,0.05);
        border-radius: 10px;
        overflow: hidden;
        margin-top: 8px;
    }
    
    .progress-bar-fill {
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
    }
    
    /* Cores de nutrientes */
    .protein { background: linear-gradient(90deg, #3b82f6, #60a5fa); }
    .carbs { background: linear-gradient(90deg, #10b981, #34d399); }
    .fats { background: linear-gradient(90deg, #f59e0b, #fbbf24); }
    .calories { background: linear-gradient(90deg, #ef4444, #f87171); }
    
    /* Timer central */
    .timer-container {
        text-align: center;
        padding: 32px;
    }
    
    .timer-display {
        font-size: 64px;
        font-weight: 200;
        font-family: 'Courier New', monospace;
        color: #ffffff;
        letter-spacing: 4px;
        text-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
    }
    
    .timer-controls {
        display: flex;
        justify-content: center;
        gap: 16px;
        margin-top: 24px;
    }
    
    /* Botões customizados */
    .btn-primary {
        background: linear-gradient(135deg, #00d4ff, #0099cc);
        color: white;
        border: none;
        padding: 12px 32px;
        border-radius: 30px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .btn-primary:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.4);
    }
    
    .btn-danger {
        background: linear-gradient(135deg, #ef4444, #dc2626);
        color: white;
        border: none;
        padding: 12px 32px;
        border-radius: 30px;
        font-weight: 600;
        cursor: pointer;
    }
    
    /* Navegação inferior */
    .nav-bottom {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(10, 10, 15, 0.95);
        backdrop-filter: blur(20px);
        border-top: 1px solid rgba(255,255,255,0.05);
        padding: 16px 0;
        display: flex;
        justify-content: space-around;
        z-index: 1000;
    }
    
    .nav-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        color: #6b6b7b;
        font-size: 11px;
        cursor: pointer;
        transition: all 0.3s;
        text-decoration: none;
    }
    
    .nav-item:hover, .nav-item.active {
        color: #00d4ff;
        transform: translateY(-4px);
    }
    
    .nav-icon {
        font-size: 24px;
        margin-bottom: 4px;
    }
    
    /* Lista de alimentos */
    .food-item {
        display: flex;
        align-items: center;
        padding: 12px;
        background: rgba(255,255,255,0.02);
        border-radius: 16px;
        margin: 8px 0;
        border: 1px solid rgba(255,255,255,0.05);
    }
    
    .food-icon {
        width: 48px;
        height: 48px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        margin-right: 16px;
        background: rgba(255,255,255,0.05);
    }
    
    .food-info {
        flex: 1;
    }
    
    .food-name {
        font-weight: 600;
        color: #ffffff;
        font-size: 14px;
    }
    
    .food-details {
        font-size: 12px;
        color: #8b8b9a;
        margin-top: 2px;
    }
    
    .food-calories {
        text-align: right;
    }
    
    .food-cals {
        font-weight: 700;
        color: #f59e0b;
        font-size: 14px;
    }
    
    /* Gráfico de linha customizado */
    .chart-container {
        height: 200px;
        position: relative;
    }
    
    /* Status online */
    .status-dot {
        width: 8px;
        height: 8px;
        background: #10b981;
        border-radius: 50%;
        display: inline-block;
        margin-right: 6px;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    /* Header do usuário */
    .user-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 16px 0;
        margin-bottom: 24px;
    }
    
    .user-info {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .user-avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        color: white;
    }
    
    .user-details h3 {
        margin: 0;
        font-size: 14px;
        color: #ffffff;
    }
    
    .user-details p {
        margin: 0;
        font-size: 12px;
        color: #10b981;
    }
    
    /* Notificação badge */
    .notification-badge {
        position: relative;
        padding: 8px;
        background: rgba(255,255,255,0.05);
        border-radius: 12px;
    }
    
    .badge {
        position: absolute;
        top: 4px;
        right: 4px;
        width: 18px;
        height: 18px;
        background: #ef4444;
        border-radius: 50%;
        font-size: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
    }
    
    /* Scrollbar customizada */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0a0a0f;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #2a2a3a;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #3a3a4a;
    }
    
    /* Container principal com padding para nav inferior */
    .main-container {
        padding-bottom: 100px;
    }
    
    /* Treino ativo card */
    .active-workout {
        background: linear-gradient(135deg, rgba(0,212,255,0.1), rgba(123,44,191,0.1));
        border: 1px solid rgba(0,212,255,0.2);
    }
    
    .workout-image {
        width: 100%;
        height: 120px;
        background: linear-gradient(135deg, #1a1a2e, #2d2d44);
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 48px;
        margin-bottom: 16px;
    }
    
    /* Stats grid */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
        margin-top: 16px;
    }
    
    .stat-box {
        text-align: center;
        padding: 16px;
        background: rgba(255,255,255,0.02);
        border-radius: 16px;
    }
    
    .stat-icon {
        font-size: 20px;
        margin-bottom: 8px;
    }
    
    .stat-value {
        font-size: 18px;
        font-weight: 700;
        color: #ffffff;
    }
    
    .stat-label {
        font-size: 11px;
        color: #6b6b7b;
        margin-top: 4px;
    }
</style>
""", unsafe_allow_html=True)

# Inicialização do estado da sessão
if 'page' not in st.session_state:
    st.session_state.page = 'inicio'
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
if 'timer_start' not in st.session_state:
    st.session_state.timer_start = None
if 'elapsed_time' not in st.session_state:
    st.session_state.elapsed_time = timedelta(0)

# Header do usuário
st.markdown("""
<div class="user-header">
    <div style="display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 24px;">⚡</span>
        <span style="font-size: 20px; font-weight: 700;">FitNS Pro</span>
    </div>
    <div style="display: flex; align-items: center; gap: 16px;">
        <div class="notification-badge">
            🔔
            <div class="badge">2</div>
        </div>
        <div class="user-info">
            <div class="user-avatar">IS</div>
            <div class="user-details">
                <h3>Igor Silva</h3>
                <p><span class="status-dot"></span>Plano Premium</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Container principal
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Navegação por tabs estilizada (substitui a navegação inferior em desktop)
tab_inicio, tab_treino, tab_nutricao, tab_progresso = st.tabs(["🏠 Início", "💪 Treino", "🥗 Nutrição", "📈 Progresso"])

with tab_inicio:
    # Layout em grid: 3 colunas
    col1, col2, col3 = st.columns([1, 1.5, 1])
    
    with col1:
        # Coluna da esquerda - Métricas
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🔥 Calorias Hoje</div>', unsafe_allow_html=True)
        
        # Círculo de progresso
        progress = 84  # 1850/2200
        st.markdown(f"""
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <div class="progress-ring" style="--progress: {progress};">
                <div class="progress-text">84%</div>
            </div>
        </div>
        <div style="text-align: center;">
            <span class="metric-big" style="font-size: 32px;">1850</span>
            <span class="metric-unit">/ 2200 kcal</span>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Proteína
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">💧 Proteína</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="display: flex; align-items: baseline; gap: 8px;">
            <span class="metric-big" style="font-size: 28px;">110g</span>
            <span class="metric-unit">/ 150g</span>
        </div>
        <div class="progress-bar-bg">
            <div class="progress-bar-fill protein" style="width: 73%;"></div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Água
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">💧 Água</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 12px;">
            <span style="font-size: 32px;">🥤🥤🥤💧</span>
            <div>
                <div class="metric-big" style="font-size: 24px;">2.4 <span class="metric-unit">/ 3.0 L</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Próximo treino
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📅 Próximo Treino</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="workout-image">🏋️</div>
        <h4 style="margin: 0 0 8px 0; color: #fff;">Peito e Tríceps</h4>
        <p style="margin: 0; color: #8b8b9a; font-size: 13px;">Amanhã - 18:00</p>
        <button class="btn-primary" style="width: 100%; margin-top: 16px; padding: 10px;">Ver Treino</button>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Coluna central - Treino Ativo e Timer
        st.markdown('<div class="glass-card active-workout">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">⚡ Treino Ativo</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="workout-image">🦵</div>
        <h3 style="margin: 0 0 8px 0; color: #fff; font-size: 20px;">Pernas - Dia 4</h3>
        <p style="margin: 0 0 16px 0; color: #00d4ff; font-size: 14px;">⏱️ 35:00 min estimado</p>
        <button class="btn-primary" style="width: 100%; padding: 14px; font-size: 16px;">▶ Iniciar Treino</button>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Timer de treino
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">⏱️ Timer de Treino</div>', unsafe_allow_html=True)
        
        # Lógica do timer
        timer_placeholder = st.empty()
        
        if st.session_state.timer_running:
            if st.session_state.timer_start is None:
                st.session_state.timer_start = datetime.now() - st.session_state.elapsed_time
            elapsed = datetime.now() - st.session_state.timer_start
            st.session_state.elapsed_time = elapsed
        else:
            elapsed = st.session_state.elapsed_time
        
        hours, remainder = divmod(int(elapsed.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        
        timer_placeholder.markdown(f"""
        <div class="timer-container">
            <div class="timer-display">{time_str}</div>
        </div>
        """, unsafe_allow_html=True)
        
        col_timer1, col_timer2 = st.columns(2)
        with col_timer1:
            if st.button("⏸ Pausar" if st.session_state.timer_running else "▶ Iniciar", 
                        use_container_width=True, 
                        type="primary" if not st.session_state.timer_running else "secondary"):
                st.session_state.timer_running = not st.session_state.timer_running
                if st.session_state.timer_running:
                    st.session_state.timer_start = datetime.now() - st.session_state.elapsed_time
                else:
                    st.session_state.timer_start = None
                st.rerun()
        
        with col_timer2:
            if st.button("⏹ Finalizar", use_container_width=True, type="secondary"):
                st.session_state.timer_running = False
                st.session_state.timer_start = None
                st.session_state.elapsed_time = timedelta(0)
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Progresso Semanal
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">', unsafe_allow_html=True)
        st.markdown('<div class="section-title" style="margin: 0;">📊 Progresso Semanal</div>', unsafe_allow_html=True)
        st.markdown('<span style="color: #10b981; font-weight: 700;">+5.2 kg ↑</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Gráfico de linha
        import pandas as pd
        import plotly.graph_objects as go
        
        dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
        peso = [73.3, 74.1, 75.2, 76.8, 77.5, 78.1, 78.5]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=dias, 
            y=peso,
            mode='lines+markers',
            line=dict(color='#00d4ff', width=3),
            marker=dict(size=8, color='#00d4ff', line=dict(width=2, color='#0f0f1a')),
            fill='tozeroy',
            fillcolor='rgba(0, 212, 255, 0.1)'
        ))
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis=dict(showgrid=False, showline=False, tickfont=dict(color='#8b8b9a')),
            yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', showline=False, tickfont=dict(color='#8b8b9a')),
            height=180
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Stats grid
        st.markdown("""
        <div class="stats-grid">
            <div class="stat-box">
                <div class="stat-icon">📊</div>
                <div class="stat-value">12/15</div>
                <div class="stat-label">Treinos</div>
            </div>
            <div class="stat-box">
                <div class="stat-icon">🔥</div>
                <div class="stat-value">8,450</div>
                <div class="stat-label">kcal</div>
            </div>
            <div class="stat-box">
                <div class="stat-icon">⚖️</div>
                <div class="stat-value">78.5</div>
                <div class="stat-label">kg</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        # Coluna da direita - Nutrição
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <div class="section-title" style="margin: 0;">🥗 Nutrição Hoje</div>
            <span style="font-size: 20px;">🔄</span>
        </div>
        <button class="btn-primary" style="width: 100%; margin-bottom: 16px; padding: 12px; background: linear-gradient(135deg, #3b82f6, #1d4ed8);">+ Adicionar Alimento</button>
        """, unsafe_allow_html=True)
        
        #

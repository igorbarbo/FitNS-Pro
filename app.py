import streamlit as st
import plotly.graph_objects as go
import time
from datetime import datetime

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="FitNS Pro", layout="wide", initial_sidebar_state="collapsed")

# --- 2. INICIALIZAÇÃO DE ESTADOS (O que faz as funções funcionarem) ---
if 'tempo_segundos' not in st.session_state:
    st.session_state.tempo_segundos = 1725  # Começa em 28:45 como na foto
if 'timer_rodando' not in st.session_state:
    st.session_state.timer_rodando = False
if 'agua_atual' not in st.session_state:
    st.session_state.agua_atual = 2.4
if 'proteina_atual' not in st.session_state:
    st.session_state.proteina_atual = 110

# Lógica do Cronômetro
if st.session_state.timer_rodando:
    time.sleep(1)
    st.session_state.tempo_segundos += 1
    st.rerun()

# --- 3. ESTILO CSS (Glassmorphism & Cores Neon) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    * { font-family: 'Inter', sans-serif; color: white; }
    .stApp { background-color: #08090f; }
    
    /* Remove bordas brancas dos botões do Streamlit */
    div.stButton > button {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px; width: 100%;
    }
    
    /* Card de Vidro */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px; padding: 15px; margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. CABEÇALHO ---
c1, _, c2 = st.columns([2, 1, 2])
with c1:
    st.markdown("## ⚡ FitNS <span style='color:#00d4ff'>Pro</span>", unsafe_allow_html=True)
with c2:
    st.markdown(f"""<div style='text-align:right;'><b>Igor Silva</b><br><span style='color:#10b981; font-size:12px;'>Plano Premium</span></div>""", unsafe_allow_html=True)

# --- 5. LAYOUT PRINCIPAL (3 Colunas como na foto) ---
col_esq, col_meio, col_dir = st.columns([1, 1.6, 1.2])

# COLUNA ESQUERDA: METAS
with col_esq:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.write("Calorias Hoje 🔥")
    st.markdown("### 1850 <span style='font-size:14px; color:#888;'>/ 2200 kcal</span>", unsafe_allow_html=True)
    st.progress(0.84)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.write(f"Água: {st.session_state.agua_atual:.1f}L 💧")
    st.progress(st.session_state.agua_atual / 3.0)
    if st.button("🥤 Beber +250ml"):
        st.session_state.agua_atual = min(3.0, st.session_state.agua_atual + 0.25)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# COLUNA CENTRAL: TREINO E TIMER
with col_meio:
    # Card de Treino Ativo
    st.markdown("""
    <div style="background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=1000'); 
                background-size: cover; border-radius: 20px; padding: 20px; border: 1px solid #10b981;">
        <p style="color:#888; margin:0;">Treino Ativo</p>
        <h2 style="margin:0;">Pernas - Dia 4</h2>
        <h1 style="color:#00d4ff; font-family:monospace; margin:10px 0;">
            {0}
        </h1>
    </div>
    """.format(time.strftime('%H:%M:%S', time.gmtime(st.session_state.tempo_segundos))), unsafe_allow_html=True)
    
    # Controles do Timer
    ts1, ts2, ts3 = st.columns(3)
    with ts1:
        if st.button("▶ Iniciar"):
            st.session_state.timer_rodando = True
            st.rerun()
    with ts2:
        if st.button("⏸ Pausar"):
            st.session_state.timer_rodando = False
            st.rerun()
    with ts3:
        if st.button("⏹ Finalizar"):
            st.session_state.timer_rodando = False
            st.session_state.tempo_segundos = 0
            st.balloons()
            st.rerun()

    # Gráfico de Progresso
    fig = go.Figure(go.Scatter(x=['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'], 
                               y=[75, 76, 75.8, 77.2, 78.5, 78, 78.5], 
                               fill='tozeroy', line_color='#00d4ff'))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
                      height=180, margin=dict(l=0,r=0,t=0,b=0), xaxis=dict(showgrid=False))
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

# COLUNA DIREITA: NUTRIÇÃO
with col_dir:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.write("Nutrição Hoje 🥗")
    if st.button("+ Adicionar Alimento"):
        st.info("Aqui você abriria um formulário de busca!")
    
    alimentos = [("Arroz Branco", "200g - 260kcal"), ("Frango Grelhado", "150g - 248kcal")]
    for nome, info in alimentos:
        st.markdown(f"""<div style='background:rgba(255,255,255,0.03); padding:8px; border-radius:10px; margin-top:5px;'>
                    <b>{nome}</b><br><small style='color:#888'>{info}</small></div>""", unsafe_allow_html=True)
    
    st.markdown("<br><b>Macros</b>", unsafe_allow_html=True)
    st.write(f"Proteína: {st.session_state.proteina_atual}g")
    st.progress(st.session_state.proteina_atual / 150)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 6. NAVEGAÇÃO INFERIOR (Simulada) ---
st.markdown("""
<div style="position: fixed; bottom: 10px; left: 50%; transform: translateX(-50%); 
            background: rgba(15, 17, 26, 0.9); padding: 10px 40px; border-radius: 30px; 
            display: flex; gap: 30px; border: 1px solid rgba(255,255,255,0.1); z-index: 1000;">
    <span style="color:#10b981">🏠 Início</span>
    <span style="opacity:0.5">🏋️ Treino</span>
    <span style="opacity:0.5">🥗 Nutrição</span>
</div>
""", unsafe_allow_html=True)

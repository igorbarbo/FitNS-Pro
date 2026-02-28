import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="FitNS Pro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS CUSTOMIZADO (ESTILO DASHBOARD PREMIUM) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    * { font-family: 'Inter', sans-serif; color: #fff; }
    .stApp { background-color: #08090f; }
    
    /* Remove espaçamentos padrão do Streamlit */
    .block-container { padding-top: 2rem; padding-bottom: 0rem; }
    header { visibility: hidden; }
    
    /* Glassmorphism Card */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 15px;
    }
    
    /* Botão Neon Verde */
    .btn-neon {
        background: #10b981;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 12px;
        font-weight: 800;
        width: 100%;
        cursor: pointer;
        transition: 0.3s;
        text-align: center;
        text-decoration: none;
        display: inline-block;
    }
    .btn-neon:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(16, 185, 129, 0.4); }

    /* Estilo para Macros */
    .macro-bar {
        height: 6px;
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        margin-top: 5px;
    }
    .macro-fill { height: 100%; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
c_logo, c_nav, c_user = st.columns([1, 2, 1.2])
with c_logo:
    st.markdown("<h2 style='margin:0;'>⚡ FitNS <span style='color:#00d4ff'>Pro</span></h2>", unsafe_allow_html=True)
with c_user:
    st.markdown("""
    <div style="display: flex; align-items: center; justify-content: flex-end; gap: 12px;">
        <div style="text-align: right;">
            <div style="font-weight: 700; font-size: 14px;">Igor Silva</div>
            <div style="font-size: 11px; color: #10b981;">Plano Premium</div>
        </div>
        <div style="width: 42px; height: 42px; background: #1a1b26; border: 1px solid #00d4ff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px;">👤</div>
    </div>
    """, unsafe_allow_html=True)

# --- NAVEGAÇÃO SUPERIOR ---
st.markdown("""
<div style="display: flex; gap: 20px; margin: 20px 0; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 10px;">
    <span style="color: #00d4ff; border-bottom: 2px solid #00d4ff; padding-bottom: 10px; cursor: pointer; font-weight: 600;">Dashboard</span>
    <span style="opacity: 0.5; cursor: pointer;">Treino</span>
    <span style="opacity: 0.5; cursor: pointer;">Nutrição</span>
    <span style="opacity: 0.5; cursor: pointer;">Progresso</span>
</div>
""", unsafe_allow_html=True)

# --- CORPO DO APP (LAYOUT 3 COLUNAS) ---
col1, col2, col3 = st.columns([1, 1.6, 1.1])

# COLUNA 1: METAS RÁPIDAS
with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<p style='font-size: 12px; color: #8b8b9a; margin-bottom: 5px;'>Calorias Hoje 🔥</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin:0;'>1850 <span style='font-size: 14px; color: #8b8b9a;'>/ 2200 kcal</span></h2>", unsafe_allow_html=True)
    # Anel de progresso simulado
    st.markdown("<div style='height: 4px; background: linear-gradient(90deg, #ff4b2b, #ff416c); width: 84%; border-radius: 10px; margin-top: 15px;'></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<p style='font-size: 12px; color: #8b8b9a;'>Proteína 💪</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin:0;'>125g <span style='font-size: 14px; opacity: 0.5;'>/ 150g</span></h3>", unsafe_allow_html=True)
    st.markdown('<div class="macro-bar"><div class="macro-fill" style="width: 80%; background: #00d4ff;"></div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<p style='font-size: 12px; color: #8b8b9a;'>Água 💧</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin:0;'>2.4 <span style='font-size: 14px; opacity: 0.5;'>/ 3.0 L</span></h3>", unsafe_allow_html=True)
    st.markdown("<div style='font-size: 24px; margin-top: 10px;'>💧 💧 💧 <span style='opacity:0.2'>💧</span></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# COLUNA 2: TREINO E GRÁFICO (CENTRO)
with col2:
    # Card de Treino Ativo (Recriando a imagem com gradiente)
    st.markdown("""
    <div style="background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.2)), url('https://images.unsplash.com/photo-1517836357463-d25dfeac3438?auto=format&fit=crop&q=80&w=500'); 
                background-size: cover; border-radius: 25px; padding: 30px; border: 1px solid rgba(255,255,255,0.1); position: relative; min-height: 220px;">
        <div style="position: absolute; top: 20px; right: 20px; background: rgba(0,0,0,0.5); padding: 5px 12px; border-radius: 10px; font-size: 12px;">35:00 min</div>
        <p style="color: #8b8b9a; margin-bottom: 5px;">Treino Ativo</p>
        <h1 style="margin: 0; font-size: 32px;">Pernas - Dia 4</h1>
        <div style="margin-top: 25px; width: 160px;">
            <a href="#" class="btn-neon">Iniciar Treino</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Gráfico de Progresso Semanal
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: space-between; align-items: center;'><span>Progresso Semanal</span><span style='color: #10b981; font-weight: bold;'>+5.2 kg</span></div>", unsafe_allow_html=True)
    
    # Mock de dados do gráfico
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'], 
        y=[75, 76, 75.8, 77.2, 78.5, 78, 78.5],
        mode='lines+markers',
        line=dict(color='#00d4ff', width=3),
        fill='tozeroy',
        fillcolor='rgba(0, 212, 255, 0.1)',
        marker=dict(size=8, color='#00d4ff')
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=10, b=0),
        height=180,
        xaxis=dict(showgrid=False, color="#8b8b9a"),
        yaxis=dict(showgrid=False, showticklabels=False)
    )
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    # Rodapé do gráfico (estatísticas)
    c1, c2, c3 = st.columns(3)
    c1.markdown("<div style='text-align:center;'><p style='color:#8b8b9a; font-size:10px;'>TREINOS</p><b>12/15</b></div>", unsafe_allow_html=True)
    c2.markdown("<div style='text-align:center;'><p style='color:#8b8b9a; font-size:10px;'>CALORIAS</p><b>8,480 kcal</b></div>", unsafe_allow_html=True)
    c3.markdown("<div style='text-align:center;'><p style='color:#8b8b9a; font-size:10px;'>PESO</p><b>78.5 kg</b></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# COLUNA 3: NUTRIÇÃO HOJE
with col_right:
    st.markdown('<div class="glass-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;'><span>Nutrição Hoje</span><span style='cursor:pointer'>⚙️</span></div>", unsafe_allow_html=True)
    
    # Botão azul de adicionar
    st.markdown("<div style='background: #00d4ff; color: black; text-align: center; padding: 10px; border-radius: 12px; font-weight: bold; margin-bottom: 20px; cursor: pointer;'>+ Adicionar Alimento</div>", unsafe_allow_html=True)
    
    alimentos = [
        ("Arroz Branco", "200 g - 260 kcal", "🍚", "#00d4ff"),
        ("Frango Grelhado", "150 g - 248 kcal", "🍗", "#10b981"),
        ("Ovos", "2 un - 140 kcal", "🥚", "#ff4b2b"),
        ("Maçã", "1 un - 95 kcal", "🍎", "#ff4b2b")
    ]
    
    for nome, desc, icon, cor in alimentos:
        st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 15px; background: rgba(255,255,255,0.02); padding: 10px; border-radius: 15px;">
            <div style="font-size: 22px; background: rgba(255,255,255,0.05); padding: 8px; border-radius: 12px;">{icon}</div>
            <div style="flex-grow: 1;">
                <div style="font-size: 13px; font-weight: 600;">{nome}</div>
                <div style="font-size: 11px; color: #8b8b9a;">{desc}</div>
            </div>
            <div style="color: {cor}; font-size: 12px;">🔥</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Barra de Macros Final
    st.markdown("<hr style='border: 0; border-top: 1px solid rgba(255,255,255,0.05); margin: 20px 0;'>", unsafe_allow_html=True)
    for macro, atual, meta, cor in [("Proteína", 110, 150, "#00d4ff"), ("Carbo", 220, 250, "#10b981"), ("Gordura", 65, 80, "#ffb800")]:
        pct = (atual/meta)*100
        st.markdown(f"""
        <div style="margin-bottom: 10px;">
            <div style="display: flex; justify-content: space-between; font-size: 11px;"><span>{macro}</span><span>{atual}g</span></div>
            <div class="macro-bar"><div class="macro-fill" style="width: {pct}%; background: {cor};"></div></div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- NAVEGAÇÃO INFERIOR FIXA (MOBILE FEEL) ---
st.markdown("""
<div style="position: fixed; bottom: 15px; left: 50%; transform: translateX(-50%); 
            background: rgba(15, 17, 26, 0.8); backdrop-filter: blur(20px); 
            padding: 12px 30px; border-radius: 30px; border: 1px solid rgba(255,255,255,0.1);
            display: flex; gap: 35px; z-index: 1000; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
    <div style="text-align: center; color: #10b981; cursor: pointer;"><div style="font-size: 18px;">🏠</div><div style="font-size: 9px;">Início</div></div>
    <div style="text-align: center; opacity: 0.5; cursor: pointer;"><div style="font-size: 18px;">🏋️</div><div style="font-size: 9px;">Treino</div></div>
    <div style="text-align: center; opacity: 0.5; cursor: pointer;"><div style="font-size: 18px;">🥗</div><div style="font-size: 9px;">Nutrição</div></div>
    <div style="text-align: center; opacity: 0.5; cursor: pointer;"><div style="font-size: 18px;">📈</div><div style="font-size: 9px;">Progresso</div></div>
</div>
<div style="height: 80px;"></div>
""", unsafe_allow_html=True)

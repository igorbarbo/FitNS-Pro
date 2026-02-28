import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="FitNS Pro", page_icon="⚡", layout="wide")

# --- CSS AVANÇADO (GLASSMORPHISM & NEON) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    * { font-family: 'Inter', sans-serif; color: #fff; }
    .stApp { background: #08090f; } /* Fundo ultra escuro */

    /* Glassmorphism Card */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 15px;
    }

    /* Badge Neon */
    .neon-badge {
        background: rgba(0, 212, 255, 0.1);
        color: #00d4ff;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        border: 1px solid rgba(0, 212, 255, 0.3);
    }

    /* Botão Iniciar (Estilo Imagem) */
    .btn-start {
        background: #10b981;
        border: none;
        padding: 10px 20px;
        border-radius: 12px;
        font-weight: 800;
        cursor: pointer;
        width: 100%;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER (IGUAL À FOTO) ---
col_logo, col_nav, col_user = st.columns([1, 2, 1])
with col_logo:
    st.markdown("### ⚡ FitNS **Pro**")
with col_user:
    st.markdown("""
    <div style="display: flex; align-items: center; justify-content: flex-end; gap: 10px;">
        <div style="text-align: right;">
            <div style="font-size: 14px; font-weight: 600;">Igor Silva</div>
            <div style="font-size: 10px; color: #10b981;">Plano Premium</div>
        </div>
        <div style="width: 40px; height: 40px; background: #333; border-radius: 50%;"></div>
    </div>
    """, unsafe_allow_html=True)

# --- LAYOUT PRINCIPAL (3 COLUNAS) ---
col_left, col_mid, col_right = st.columns([1, 1.5, 1.2])

# COLUNA ESQUERDA: METAS RÁPIDAS
with col_left:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<p style='font-size: 12px; color: #8b8b9a;'>Calorias Hoje 🔥</p>", unsafe_allow_html=True)
    st.markdown("## 1850 <span style='font-size: 14px; color: #8b8b9a;'>/ 2200 kcal</span>", unsafe_allow_html=True)
    st.progress(0.84)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<p style='font-size: 12px; color: #8b8b9a;'>Água 💧</p>", unsafe_allow_html=True)
    st.markdown("### 2.4 <span style='font-size: 14px; color: #8b8b9a;'>/ 3.0 L</span>", unsafe_allow_html=True)
    st.markdown("💧 💧 💧 <span style='opacity: 0.3;'>💧</span>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# COLUNA CENTRAL: TREINO E GRÁFICO
with col_mid:
    # Card de Treino Ativo com Imagem
    st.markdown("""
    <div style="background: linear-gradient(to right, rgba(0,0,0,0.9), rgba(0,0,0,0.2)), url('https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=500'); 
                background-size: cover; border-radius: 20px; padding: 25px; border: 1px solid rgba(255,255,255,0.1); min-height: 200px;">
        <p style="color: #8b8b9a; margin: 0; font-size: 12px;">Treino Ativo</p>
        <h2 style="margin: 5px 0;">Pernas - Dia 4</h2>
        <h3 style="color: #00d4ff;">35:00 <span style="font-size: 14px;">min</span></h3>
        <button class="btn-start">Iniciar Treino</button>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("") # Espaçador
    
    # Gráfico de Progresso Semanal
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: space-between;'><span>Progresso Semanal</span><span style='color: #10b981;'>+5.2 kg</span></div>", unsafe_allow_html=True)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'], y=[75, 76, 75.5, 77, 78.5, 78, 78.5], 
                             line=dict(color='#00d4ff', width=3), mode='lines+markers', fill='tozeroy', fillcolor='rgba(0, 212, 255, 0.1)'))
    fig.update_layout(height=150, margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      xaxis=dict(showgrid=False), yaxis=dict(showgrid=False, showticklabels=False))
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    st.markdown('</div>', unsafe_allow_html=True)

# COLUNA DIREITA: NUTRIÇÃO DIÁRIA
with col_right:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;'><span>Nutrição Hoje</span><button style='background:#00d4ff; border:none; border-radius:8px; padding:5px 10px; color:#000; font-weight:bold; font-size:12px;'>+ Adicionar</button></div>", unsafe_allow_html=True)
    
    alimentos = [("🍚", "Arroz Branco", "200g - 260 kcal"), ("🍗", "Frango Grelhado", "150g - 248 kcal"), ("🥚", "Ovos", "2 un - 140 kcal")]
    for icon, nome, desc in alimentos:
        st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 15px; background: rgba(255,255,255,0.02); padding: 10px; border-radius: 12px; margin-bottom: 8px;">
            <div style="font-size: 20px;">{icon}</div>
            <div style="flex: 1;">
                <div style="font-size: 13px; font-weight: 600;">{nome}</div>
                <div style="font-size: 11px; color: #8b8b9a;">{desc}</div>
            </div>
            <div style="color: #00d4ff;">💧</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- BARRA DE NAVEGAÇÃO INFERIOR (SIMULADA) ---
st.markdown("""
<div style="position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); 
            background: rgba(15, 17, 26, 0.8); backdrop-filter: blur(20px); 
            padding: 15px 40px; border-radius: 30px; border: 1px solid rgba(255,255,255,0.1);
            display: flex; gap: 40px; z-index: 999;">
    <span style="cursor: pointer; color: #10b981;">🏠</span>
    <span style="cursor: pointer; opacity: 0.5;">🏋️</span>
    <span style="cursor: pointer; opacity: 0.5;">🥗</span>
    <span style="cursor: pointer; opacity: 0.5;">📈</span>
</div>
""", unsafe_allow_html=True)


import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import json
import os
import time
from dataclasses import dataclass, asdict

# --- 1. CONFIGURAÇÃO E ESTILO ---
st.set_page_config(page_title="FitNS Pro - Igor Barbosa", layout="wide", initial_sidebar_state="collapsed")

def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
        * { font-family: 'Inter', sans-serif; color: white; }
        .stApp { background-color: #08090f; }
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px; padding: 20px; margin-bottom: 15px;
        }
        .task-done { opacity: 0.4; text-decoration: line-through; border-left: 4px solid #10b981; }
        .task-pending { border-left: 4px solid #00d4ff; }
        div.stButton > button {
            background: linear-gradient(135deg, #00d4ff, #0099cc);
            border: none; border-radius: 12px; font-weight: bold; width: 100%;
        }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BANCO DE DADOS DO PLANNER ---
# Mapeamento do Planner de Igor Barbosa
PLANNER_IGOR = {
    0: [("06:15", "🔵 HIIT Casa", "15min"), ("07:00", "🟢 Café", "3 ovos + café"), ("13:00", "🏋️ Pernas", "Leg Press/Extensora"), ("20:00", "🟢 Jantar", "Pudim Proteico + Chia")],
    1: [("06:15", "🔵 HIIT Casa", "12min"), ("07:00", "🟢 Café", "3 ovos + café"), ("13:00", "🏋️ Peito/Ombro/Tríceps", "Chest/Shoulder Press"), ("20:00", "🟢 Jantar", "Pudim Proteico + Chia")],
    2: [("06:15", "🔵 HIIT Casa", "15min"), ("07:00", "🟢 Café", "3 ovos + café"), ("13:00", "🏋️ Costas/Bíceps", "Lat Pulldown/Remada"), ("20:00", "🟢 Jantar", "Pudim Proteico + Chia")],
    3: [("06:15", "🔵 HIIT Casa", "12min"), ("07:00", "🟢 Café", "3 ovos + café"), ("13:00", "🏋️ Ombros/Core", "Shoulder Press/Vacuum"), ("20:00", "🟢 Jantar", "Pudim Proteico + Chia")],
    4: [("06:15", "🔵 HIIT Casa", "15min"), ("07:00", "🟢 Café", "3 ovos + café"), ("13:00", "🏋️ Full Body", "Leg/Chest/Lat"), ("20:00", "🟢 Jantar", "Pudim Proteico + Chia")],
    5: [("06:15", "🚶 Caminhada", "45-60min"), ("07:00", "🟢 Café", "3 ovos + café"), ("17:00", "🏋️ Circuito Parque", "3 voltas")],
    6: [("06:15", "🚶 Caminhada", "45-60min"), ("07:00", "🟢 Café", "3 ovos + café"), ("17:00", "🏋️ Circuito Leve", "3 voltas")]
}

# --- 3. LÓGICA DE ESTADO ---
if 'check_list' not in st.session_state: st.session_state.check_list = {}
if 'agua' not in st.session_state: st.session_state.agua = 0.0

# --- 4. COMPONENTES DE INTERFACE ---
def render_header():
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown("## ⚡ FitNS <span style='color:#00d4ff'>Pro</span>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div style='text-align:right;'><b>Igor Barbosa</b><br><small style='color:#10b981'>Plano Premium</small></div>", unsafe_allow_html=True)

def render_planner():
    dia_idx = datetime.now().weekday()
    dias_pt = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    
    st.markdown(f"### 🗓️ Planner: {dias_pt[dia_idx]}")
    
    tarefas = PLANNER_IGOR.get(dia_idx, [])
    
    for i, (hora, titulo, desc) in enumerate(tarefas):
        key = f"task_{dia_idx}_{i}"
        is_done = st.session_state.check_list.get(key, False)
        
        status_class = "task-done" if is_done else "task-pending"
        
        # Layout do Card de Tarefa
        with st.container():
            col_check, col_txt = st.columns([0.15, 0.85])
            with col_check:
                # O checkbox real que controla o estado
                st.session_state.check_list[key] = st.checkbox("", value=is_done, key=f"cb_{key}")
            with col_txt:
                st.markdown(f"""
                <div class="glass-card {status_class}" style="padding: 10px 15px; margin-bottom: 5px;">
                    <small style="color:#00d4ff; font-weight:bold;">{hora}</small>
                    <div style="font-size: 14px; font-weight:700;">{titulo}</div>
                    <div style="font-size: 11px; color:#888;">{desc}</div>
                </div>
                """, unsafe_allow_html=True)

# --- 5. DASHBOARD PRINCIPAL ---
def main():
    load_css()
    render_header()
    
    tab1, tab2 = st.tabs(["Dashboard", "Nutrição & Água"])
    
    with tab1:
        col_left, col_right = st.columns([1.2, 1])
        
        with col_left:
            render_planner()
            
        with col_right:
            st.markdown("### 📊 Meta Semanal")
            # Gráfico Simulado de Peso
            fig = go.Figure(go.Scatter(x=['S','T','Q','Q','S','S','D'], y=[78, 77.8, 77.5, 77.2, 77, 76.8, 76.5],
                                     line=dict(color='#00d4ff', width=4), fill='tozeroy'))
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=200, 
                              margin=dict(l=0,r=0,t=0,b=0), xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.write("🔥 Calorias Acumuladas: **12,400 kcal**")
            st.write("🏋️ Treinos Concluídos: **4/5**")
            st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.subheader("💧 Hidratação")
            st.write(f"Total: **{st.session_state.agua:.1f} L** / 4.5 L")
            st.progress(min(st.session_state.agua / 4.5, 1.0))
            if st.button("🥤 Adicionar 500ml"):
                st.session_state.agua += 0.5
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            
        with c2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.subheader("🍮 Jantar Especial")
            st.write("Pudim Proteico + Sementes de Chia")
            st.markdown("<small>Proteína: 35g | Fibras: 8g</small>", unsafe_allow_html=True)
            if st.button("✅ Registrar Jantar"):
                st.toast("Jantar registrado no diário!")
            st.markdown('</div>', unsafe_allow_html=True)

    # Navegação Inferior Estática
    st.markdown("""
    <div style="position: fixed; bottom: 0; left: 0; width: 100%; background: #0a0b12; 
                padding: 10px; display: flex; justify-content: space-around; border-top: 1px solid #222;">
        <span>🏠 Início</span>
        <span style="opacity:0.5">🏋️ Treinos</span>
        <span style="opacity:0.5">🥗 Dieta</span>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    

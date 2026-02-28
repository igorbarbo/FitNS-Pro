import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="FitNS Pro v2.5",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ESTILIZAÇÃO (CSS OTIMIZADO) ---
def local_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    :root {
        --primary: #00d4ff;
        --secondary: #7b2cbf;
        --bg: #0f0f1a;
        --glass: rgba(255, 255, 255, 0.05);
    }

    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: var(--bg); }
    
    /* Glassmorphism Containers */
    .glass-card {
        background: var(--glass);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: transform 0.2s ease;
    }
    .glass-card:hover { transform: translateY(-2px); border-color: var(--primary); }

    /* Custom Progress Bar */
    .progress-bar-bg {
        width: 100%; height: 8px; background: rgba(255,255,255,0.1); 
        border-radius: 10px; overflow: hidden; margin-top: 8px;
    }
    .progress-bar-fill { height: 100%; border-radius: 10px; transition: width 0.5s ease-in-out; }

    /* Botões */
    .stButton>button {
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s;
        border: none;
    }
    
    /* Esconder elementos desnecessários do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

local_css()

# --- GERENCIAMENTO DE ESTADO (SESSION STATE) ---
if 'timer_running' not in st.session_state: st.session_state.timer_running = False
if 'elapsed_time' not in st.session_state: st.session_state.elapsed_time = 0
if 'last_check' not in st.session_state: st.session_state.last_check = None
if 'agua_atual' not in st.session_state: st.session_state.agua_atual = 2.4

# Lógica do Cronômetro
if st.session_state.timer_running:
    now = time.time()
    if st.session_state.last_check:
        st.session_state.elapsed_time += now - st.session_state.last_check
    st.session_state.last_check = now
    time.sleep(0.1)
    st.rerun()

# --- MOCK DATA ---
USER = {"name": "Alexandre", "rank": "Premium", "points": 1250}
MACROS = {
    "Calorias": {"atual": 1850, "meta": 2200, "cor": "linear-gradient(90deg, #ff4b2b, #ff416c)"},
    "Proteína": {"atual": 142, "meta": 180, "cor": "linear-gradient(90deg, #00d4ff, #0072ff)"},
    "Carbos": {"atual": 195, "meta": 250, "cor": "linear-gradient(90deg, #f59e0b, #d97706)"}
}

# --- HEADER ---
col_h1, col_h2 = st.columns([2, 1])
with col_h1:
    st.markdown(f"""
        <h1 style='margin-bottom:0;'>FitNS <span style='color:#00d4ff'>Pro</span></h1>
        <p style='color:#8b8b9a;'>Bem-vindo de volta, <b>{USER['name']}</b>. Seu foco hoje é Pernas!</p>
    """, unsafe_allow_html=True)
with col_h2:
    st.markdown(f"""
        <div style='text-align:right; margin-top:10px;'>
            <span style='background:rgba(0,212,255,0.1); color:#00d4ff; padding:8px 16px; border-radius:30px; font-size:12px; font-weight:bold;'>
                🏆 {USER['rank']} | {USER['points']} pts
            </span>
        </div>
    """, unsafe_allow_html=True)

# --- TABS ---
tab_dash, tab_treino, tab_nutri, tab_evolucao = st.tabs(["📊 Dashboard", "🏋️ Treino", "🥗 Nutrição", "📈 Evolução"])

with tab_dash:
    c1, c2, c3 = st.columns([1, 1.5, 1])
    
    with c1:
        st.markdown("<h4 style='font-size:16px;'>Metas Diárias</h4>", unsafe_allow_html=True)
        for macro, info in MACROS.items():
            pct = min(int((info['atual']/info['meta'])*100), 100)
            st.markdown(f"""
                <div class="glass-card">
                    <div style="display:flex; justify-content:space-between; font-size:12px;">
                        <span>{macro}</span>
                        <span>{info['atual']}/{info['meta']}</span>
                    </div>
                    <div class="progress-bar-bg">
                        <div class="progress-bar-fill" style="width:{pct}%; background:{info['cor']};"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
        # Widget de Água Interativo
        st.markdown("<div class='glass-card' style='text-align:center;'>", unsafe_allow_html=True)
        st.write("💧 Hidratação")
        st.subheader(f"{st.session_state.agua_atual:.1f} / 3.0L")
        if st.button("➕ Beber 250ml", use_container_width=True):
            st.session_state.agua_atual += 0.25
            st.toast("Ótimo trabalho! Mantenha-se hidratado. 💧")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        # Cronômetro Visual
        st.markdown("<div class='glass-card' style='text-align:center; border:1px solid #00d4ff;'>", unsafe_allow_html=True)
        st.markdown("<p style='color:#00d4ff; font-size:12px; font-weight:bold;'>TREINO ATIVO: Pernas - Dia 4</p>", unsafe_allow_html=True)
        td = timedelta(seconds=int(st.session_state.elapsed_time))
        st.markdown(f"<h1 style='font-family:monospace; font-size:60px;'>{str(td)}</h1>", unsafe_allow_html=True)
        
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("▶ Iniciar/Pausar", use_container_width=True, type="primary"):
                st.session_state.timer_running = not st.session_state.timer_running
                st.session_state.last_check = time.time() if st.session_state.timer_running else None
                st.rerun()
        with btn_col2:
            if st.button("⏹ Finalizar", use_container_width=True):
                st.session_state.timer_running = False
                st.session_state.elapsed_time = 0
                st.session_state.last_check = None
                st.balloons()
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Gráfico de Atividade Curto
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        fig = go.Figure(data=go.Scatter(
            x=['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom'],
            y=[65, 80, 45, 90, 100, 20, 0],
            fill='tozeroy', line_color='#00d4ff', mode='lines'
        ))
        fig.update_layout(height=180, margin=dict(l=0, r=0, t=0, b=0), paper_bgcolor='rgba(0,0,0,0)', 
                         plot_bgcolor='rgba(0,0,0,0)', xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        st.markdown("</div>", unsafe_allow_html=True)

    with c3:
        st.markdown("<h4 style='font-size:16px;'>Próximas Refeições</h4>", unsafe_allow_html=True)
        refeicoes = [("Lanche", "15:30", "🍌 Banana + Aveia"), ("Jantar", "20:00", "🍗 Frango + Arroz")]
        for ref, hora, desc in refeicoes:
            st.markdown(f"""
                <div class="glass-card" style="padding:15px;">
                    <div style="color:#00d4ff; font-size:11px; font-weight:bold;">{hora}</div>
                    <div style="font-weight:600; font-size:14px;">{ref}</div>
                    <div style="color:#8b8b9a; font-size:12px;">{desc}</div>
                </div>
            """, unsafe_allow_html=True)

# --- TRATAMENTO DAS OUTRAS ABAS (Resumido para o exemplo) ---
with tab_treino:
    st.info("Selecione os exercícios para registrar suas séries.")
    # Exemplo de interação funcional
    ex = st.multiselect("Exercícios de Hoje", ["Agachamento Livre", "Leg Press", "Extensora", "Panturrilha"])
    if ex:
        for item in ex:
            col_a, col_b, col_c = st.columns([2,1,1])
            col_a.write(f"**{item}**")
            col_b.number_input("Peso (kg)", key=f"w_{item}", min_value=0)
            col_c.number_input("Reps", key=f"r_{item}", min_value=0)

with tab_evolucao:
    [attachment_0](attachment)
    st.subheader("Análise de Composição Corporal")
    col_met1, col_met2, col_met3 = st.columns(3)
    col_met1.metric("Peso", "78.5 kg", "-0.8 kg")
    col_met2.metric("Gordura Corporal", "14.2%", "-1.5%")
    col_met3.metric("Massa Magra", "64.2 kg", "+0.5 kg")
    

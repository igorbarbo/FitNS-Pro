# pages/dashboard.py
import streamlit as st
import plotly.graph_objects as go
from modules.header import render_header
from modules.navigation import render_navigation
from modules.progress_bars import render_progress_bar

def show():
    user = st.session_state.user
    service = st.session_state.service
    data = service.get_dashboard_data(user.id)
    stats = data["stats"]
    
    render_header(user)
    render_navigation()
    st.markdown('<div class="slide-in">', unsafe_allow_html=True)
    
    # Card principal de calorias
    progress = (stats.calories_consumed / stats.calories_goal) * 100
    st.markdown(f"""
    <div class="glass-card" style="background: linear-gradient(135deg, rgba(255,75,43,0.1), rgba(255,65,108,0.1)); border: 1px solid rgba(255,75,43,0.3);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div>
                <p style="font-size: 11px; color: #ff4b2b; margin-bottom: 5px; font-weight: 600;">🔥 Calorias Hoje</p>
                <h2 style="margin:0; font-size: 36px; font-weight: 800;">{stats.calories_consumed}</h2>
                <p style="font-size: 13px; color: #8b8b9a; margin-top: 5px;">/ {stats.calories_goal} kcal</p>
            </div>
            <div style="background: rgba(255,75,43,0.2); padding: 8px 12px; border-radius: 12px; font-size: 12px; font-weight: 700; color: #ff4b2b;">
                {progress:.0f}%
            </div>
        </div>
        <div class="progress-bg" style="margin-top: 15px; height: 10px;">
            <div class="progress-fill" style="width: {min(progress, 100)}%; background: linear-gradient(90deg, #ff4b2b, #ff416c);"></div>
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 15px; font-size: 11px;">
            <span style="color: #8b8b9a;">Consumidas</span>
            <span style="color: #ff4b2b; font-weight: 600;">Restam {data['remaining_calories']} kcal</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Macros em duas colunas
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        render_progress_bar("Proteína 💪", stats.protein_consumed, stats.protein_goal, "#00d4ff", "g")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        carbs = sum(m.carbs for m in data["meals"]) if data["meals"] else 0
        fat = sum(m.fat for m in data["meals"]) if data["meals"] else 0
        render_progress_bar("Carboidratos 🍞", carbs, 250, "#10b981", "g")
        render_progress_bar("Gorduras 🥑", fat, 80, "#ffb800", "g")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Água
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    water_progress = (stats.water_consumed / stats.water_goal) * 100
    water_glasses = int(stats.water_consumed / 0.3)
    remaining_glasses = int((stats.water_goal - stats.water_consumed) / 0.3)
    cols = st.columns([3, 1])
    with cols[0]:
        st.markdown(f"""
        <div>
            <p style="font-size: 11px; color: #00d4ff; margin-bottom: 5px;">💧 Hidratação</p>
            <h3 style="margin:0; font-size: 24px;">{stats.water_consumed:.1f} <span style="font-size: 14px; opacity: 0.5;">/ {stats.water_goal} L</span></h3>
            <div style="margin-top: 10px; font-size: 20px; letter-spacing: 2px;">
                {''.join(['💧' for _ in range(water_glasses)])}
                {''.join(['<span style="opacity:0.2">💧</span>' for _ in range(remaining_glasses)])}
            </div>
        </div>
        """, unsafe_allow_html=True)
    with cols[1]:
        if st.button("+ 300ml", key="add_water", use_container_width=True):
            st.session_state.service.store.add_water(user.id)
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Card do próximo treino (apenas conteúdo)
    st.markdown(f"""
    <div class="glass-card" style="background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.4)), 
                                    url('https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=600'); 
                                    background-size: cover; background-position: center; min-height: 160px;
                                    display: flex; flex-direction: column; justify-content: space-between;">
        <div>
            <div style="float: right; background: rgba(0,0,0,0.6); backdrop-filter: blur(10px); 
                        padding: 6px 12px; border-radius: 10px; font-size: 11px; border: 1px solid rgba(255,255,255,0.1);">
                ⏱️ 45 min
            </div>
            <p style="color: #00d4ff; margin-bottom: 5px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Próximo Treino</p>
            <h2 style="margin: 0; font-size: 24px; font-weight: 800;">Superiores - Dia A</h2>
            <p style="color: #8b8b9a; font-size: 12px; margin-top: 5px;">Peito, Ombros e Tríceps</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Botão funcional abaixo do card
    if st.button("🏋️ Iniciar Treino", key="start_workout", use_container_width=True):
        st.session_state.page = "workout"
        st.rerun()
    
    # Gráfico de evolução de peso
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;'>"
                "<span style='font-weight: 700; font-size: 14px;'>📊 Evolução de Peso</span>"
                "<span style='color: #10b981; font-weight: 800; font-size: 13px;'>+2.3 kg/mês</span></div>", unsafe_allow_html=True)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'], 
        y=data["weekly_progress"],
        mode='lines+markers', 
        line=dict(color='#00d4ff', width=3),
        fill='tozeroy', 
        fillcolor='rgba(0, 212, 255, 0.1)', 
        marker=dict(size=8, color='#00d4ff', line=dict(color='#fff', width=2))
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=10, b=0), height=200,
        xaxis=dict(showgrid=False, color="#8b8b9a", tickfont=dict(size=10)),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', color="#8b8b9a", tickfont=dict(size=10))
    )
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    # Métricas rápidas
    cols = st.columns(3)
    metrics = [("🔥", "12", "Treinos", "#ff4b2b"), ("⚡", "8,450", "Kcal", "#00d4ff"), ("💪", "78.5", "Kg", "#10b981")]
    for col, (icon, value, label, color) in zip(cols, metrics):
        col.markdown(f"""
        <div style="text-align: center; padding: 10px; background: rgba(255,255,255,0.02); border-radius: 12px;">
            <div style="font-size: 16px; margin-bottom: 4px;">{icon}</div>
            <div style="font-size: 18px; font-weight: 800; color: {color};">{value}</div>
            <div style="font-size: 9px; color: #8b8b9a; text-transform: uppercase; letter-spacing: 0.5px;">{label}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

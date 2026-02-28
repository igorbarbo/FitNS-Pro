# pages/progress.py
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta
from modules.header import render_header
from modules.navigation import render_navigation
from utils.helpers import calculate_bmi

def show():
    """Página de progresso com histórico de peso e métricas."""
    try:
        user = st.session_state.user
        service = st.session_state.service
        store = service.store

        # Obtém histórico de peso
        weight_history = store.get_weight_history(user.id)
        # Obtém perfil para exibir IMC atual
        profile = store.get_user_profile(user.id)

        render_header(user)
        render_navigation()
        st.markdown('<div class="slide-in">', unsafe_allow_html=True)

        st.markdown("""
        <div style="margin-bottom: 20px;">
            <h2 style="margin:0; font-size: 24px;">📈 Progresso</h2>
            <p style="color: #8b8b9a; font-size: 12px; margin-top: 5px;">Acompanhe sua evolução</p>
        </div>
        """, unsafe_allow_html=True)

        # Métricas principais
        col1, col2, col3 = st.columns(3)
        with col1:
            if profile:
                bmi = calculate_bmi(profile.weight, profile.height)
                delta_bmi = "saudável" if 18.5 <= bmi <= 24.9 else "fora do ideal"
                col1.metric("IMC Atual", f"{bmi}", delta_bmi)
            else:
                col1.metric("IMC", "---", "cadastre seu perfil")
        with col2:
            if weight_history:
                last_weight = weight_history[-1]["weight"]
                first_weight = weight_history[0]["weight"] if len(weight_history) > 1 else last_weight
                change = last_weight - first_weight
                col2.metric("Último Peso", f"{last_weight} kg", f"{change:+.1f} kg")
            else:
                col2.metric("Peso", "---", "sem registros")
        with col3:
            workouts = store.get_today_stats(user.id).workouts_completed
            col3.metric("Treinos no Mês", workouts, "meta: 5")

        # Gráfico de evolução de peso (se houver dados)
        if len(weight_history) >= 2:
            st.markdown("### 📊 Histórico de Peso")
            dates = [entry["date"] for entry in weight_history[-10:]]  # últimos 10
            weights = [entry["weight"] for entry in weight_history[-10:]]

            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=dates,
                y=weights,
                mode='lines+markers',
                line=dict(color='#00d4ff', width=3),
                marker=dict(size=8, color='#00d4ff', line=dict(color='#fff', width=2))
            ))
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                margin=dict(l=0, r=0, t=10, b=0),
                height=300,
                xaxis=dict(showgrid=False, color="#8b8b9a"),
                yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', color="#8b8b9a")
            )
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        else:
            st.info("Adicione registros de peso para visualizar o gráfico de evolução.")

        # Botão para adicionar novo peso
        with st.expander("➕ Adicionar novo peso"):
            with st.form("weight_form"):
                new_weight = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0, step=0.1)
                if st.form_submit_button("Registrar"):
                    store.add_weight_entry(user.id, new_weight)
                    st.success("Peso registrado!")
                    st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Erro na página de progresso: {e}")
        import traceback
        st.code(traceback.format_exc())

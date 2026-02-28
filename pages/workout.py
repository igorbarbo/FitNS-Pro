# pages/workout.py
import streamlit as st
from modules.header import render_header
from modules.navigation import render_navigation

def show():
    """Página de treinos com sugestões baseadas no perfil."""
    try:
        user = st.session_state.user
        service = st.session_state.service
        store = service.store

        # Tenta obter perfil para personalizar sugestões
        profile = store.get_user_profile(user.id)

        render_header(user)
        render_navigation()
        st.markdown('<div class="slide-in">', unsafe_allow_html=True)

        st.markdown("""
        <div style="margin-bottom: 20px;">
            <h2 style="margin:0; font-size: 24px;">🏋️ Treinos</h2>
            <p style="color: #8b8b9a; font-size: 12px; margin-top: 5px;">Seu plano de treino</p>
        </div>
        """, unsafe_allow_html=True)

        # Treino do dia em destaque (pode variar conforme objetivo)
        if profile and profile.goal == "gain":
            treino_destaque = "Treino A - Superiores (Hipertrofia)"
            musculos = "Peito • Ombros • Tríceps • Abdômen"
            cor_borda = "#00d4ff"
        elif profile and profile.goal == "lose":
            treino_destaque = "Circuito HIIT + Musculação"
            musculos = "Full body • Cardio intenso"
            cor_borda = "#ff4b2b"
        else:
            treino_destaque = "Treino A - Superiores"
            musculos = "Peito • Ombros • Tríceps • Abdômen"
            cor_borda = "#00d4ff"

        st.markdown(f"""
        <div class="glass-card" style="border: 2px solid {cor_borda}; background: rgba(0,212,255,0.05);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                <span style="background: {cor_borda}; color: #000; padding: 4px 10px; border-radius: 8px; font-size: 10px; font-weight: 800;">HOJE</span>
                <span style="color: #8b8b9a; font-size: 12px;">⏱️ 60 min</span>
            </div>
            <h3 style="margin:0; font-size: 20px; margin-bottom: 10px;">{treino_destaque}</h3>
            <div style="font-size: 12px; color: #8b8b9a; margin-bottom: 15px;">{musculos}</div>
            <button class="btn-neon">Iniciar Treino</button>
        </div>
        """, unsafe_allow_html=True)

        # Próximos treinos (simulados)
        workouts = [
            ("Amanhã", "Treino B - Inferiores", "Quadríceps • Posterior • Glúteos", "#10b981"),
            ("Quarta", "Treino C - Costas", "Dorsais • Bíceps • Antebraço", "#ffb800"),
            ("Sexta", "Cardio + Core", "Corrida • Abdominais • Pranche", "#8b8b9a")
        ]

        for day, title, muscles, color in workouts:
            st.markdown(f"""
            <div class="glass-card" style="opacity: 0.9;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <div style="font-size: 10px; color: {color}; font-weight: 600; margin-bottom: 4px;">{day}</div>
                        <div style="font-size: 16px; font-weight: 700; margin-bottom: 4px;">{title}</div>
                        <div style="font-size: 11px; color: #8b8b9a;">{muscles}</div>
                    </div>
                    <div style="color: #8b8b9a;">›</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Erro na página de treino: {e}")
        import traceback
        st.code(traceback.format_exc())

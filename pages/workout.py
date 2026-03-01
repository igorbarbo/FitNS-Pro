# pages/workout.py
import streamlit as st
from modules.header import render_header
from modules.navigation import render_navigation
from utils.helpers import generate_workout_plan

def show():
    try:
        user = st.session_state.user
        service = st.session_state.service
        store = service.store

        profile = store.get_user_profile(user.id)
        goal = profile.goal if profile else "maintain"

        render_header(user)
        render_navigation()
        st.markdown('<div class="slide-in">', unsafe_allow_html=True)

        st.markdown("""
        <div style="margin-bottom: 20px;">
            <h2 style="margin:0; font-size: 24px;">🏋️ Treinos</h2>
            <p style="color: #8b8b9a; font-size: 12px; margin-top: 5px;">Seu plano de treino personalizado</p>
        </div>
        """, unsafe_allow_html=True)

        workout_plan = generate_workout_plan(goal)

        for day, details in workout_plan.items():
            with st.expander(f"**{day}** – {details['name']}", expanded=(day=="Segunda")):
                for exercise, reps, _ in details["exercises"]:
                    st.markdown(f"- {exercise}: {reps}")
                st.markdown("---")

        st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Erro na página de treino: {e}")
        import traceback
        st.code(traceback.format_exc())
# Adicione instruções rápidas no workout.py
st.info("""
**Dicas importantes:**
- 🔥 HIIT: 30s esforço máximo / 15s descanso
- 💪 Musculação: escolha um peso que desafie nas últimas repetições
- 🧘 Alongamento: segure cada posição por 30s
""")

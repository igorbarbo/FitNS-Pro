# pages/profile.py
import streamlit as st
from datetime import datetime
from modules.header import render_header
from modules.navigation import render_navigation
from utils.models import UserProfile
from utils.helpers import (
    calculate_bmi, calculate_tmb, get_activity_factor,
    calculate_daily_calories, calculate_macros, suggest_workout
)

def show():
    user = st.session_state.user
    service = st.session_state.service
    store = service.store

    render_header(user)
    render_navigation()
    st.markdown('<div class="slide-in">', unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-bottom: 20px;">
        <h2 style="margin:0; font-size: 24px;">📊 Meu Perfil</h2>
        <p style="color: #8b8b9a; font-size: 12px; margin-top: 5px;">Informe seus dados para recomendações personalizadas</p>
    </div>
    """, unsafe_allow_html=True)

    # Carregar perfil existente, se houver
    existing_profile = store.get_user_profile(user.id)

    with st.form("profile_form"):
        col1, col2 = st.columns(2)
        with col1:
            weight = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0, 
                                     value=existing_profile.weight if existing_profile else 70.0, step=0.1)
            height = st.number_input("Altura (cm)", min_value=100.0, max_value=250.0, 
                                     value=existing_profile.height if existing_profile else 170.0, step=0.5)
            age = st.number_input("Idade", min_value=15, max_value=100, 
                                  value=existing_profile.age if existing_profile else 30, step=1)
        with col2:
            gender = st.selectbox("Gênero", ["Masculino", "Feminino"], 
                                  index=0 if existing_profile and existing_profile.gender=="male" else 1)
            activity_map = {
                "sedentary": "Sedentário (pouco ou nenhum exercício)",
                "light": "Levemente ativo (exercício leve 1-3x/semana)",
                "moderate": "Moderadamente ativo (exercício moderado 3-5x/semana)",
                "active": "Muito ativo (exercício intenso 6-7x/semana)",
                "very_active": "Extremamente ativo (treinos diários + trabalho físico)"
            }
            activity_level = st.selectbox(
                "Nível de atividade",
                options=list(activity_map.keys()),
                format_func=lambda x: activity_map[x],
                index=list(activity_map.keys()).index(existing_profile.activity_level) if existing_profile and existing_profile.activity_level in activity_map else 2
            )
            goal_map = {"lose": "Perder peso", "maintain": "Manter peso", "gain": "Ganhar massa muscular"}
            goal = st.selectbox(
                "Objetivo",
                options=list(goal_map.keys()),
                format_func=lambda x: goal_map[x],
                index=list(goal_map.keys()).index(existing_profile.goal) if existing_profile and existing_profile.goal in goal_map else 1
            )
            target_weight = st.number_input("Peso desejado (kg)", min_value=30.0, max_value=200.0, 
                                            value=existing_profile.target_weight if existing_profile else weight, step=0.1)

        submitted = st.form_submit_button("Salvar e Calcular", use_container_width=True, type="primary")

    if submitted:
        gender_code = "male" if gender == "Masculino" else "female"
        profile = UserProfile(
            user_id=user.id,
            weight=weight,
            height=height,
            age=age,
            gender=gender_code,
            activity_level=activity_level,
            goal=goal,
            target_weight=target_weight,
            updated_at=datetime.now().isoformat()
        )
        store.save_user_profile(profile)
        st.success("Perfil salvo com sucesso!")
        st.session_state.profile = profile
        st.rerun()

    # Se já existe perfil, mostrar recomendações
    profile = existing_profile or st.session_state.get('profile')
    if profile:
        st.markdown("---")
        st.markdown("### 🔥 Suas Recomendações Personalizadas")

        bmi = calculate_bmi(profile.weight, profile.height)
        tmb = calculate_tmb(profile.weight, profile.height, profile.age, profile.gender)
        activity_factor = get_activity_factor(profile.activity_level)
        daily_calories = calculate_daily_calories(tmb, activity_factor, profile.goal)
        macros = calculate_macros(profile.weight, daily_calories, profile.goal)
        workout_suggestion = suggest_workout(profile.goal)

        col1, col2, col3 = st.columns(3)
        col1.metric("IMC", f"{bmi}", "kg/m²")
        col2.metric("Taxa Metabólica Basal", f"{tmb} kcal", "TMB")
        col3.metric("Calorias Diárias", f"{daily_calories} kcal", "recomendadas")

        st.markdown("#### 🥗 Macros Diários")
        cols = st.columns(3)
        cols[0].markdown(f"""
        <div class="glass-card" style="text-align:center;">
            <h4 style="color:#00d4ff;">Proteína</h4>
            <p style="font-size:28px; font-weight:800;">{macros['protein']}g</p>
        </div>
        """, unsafe_allow_html=True)
        cols[1].markdown(f"""
        <div class="glass-card" style="text-align:center;">
            <h4 style="color:#10b981;">Carboidratos</h4>
            <p style="font-size:28px; font-weight:800;">{macros['carbs']}g</p>
        </div>
        """, unsafe_allow_html=True)
        cols[2].markdown(f"""
        <div class="glass-card" style="text-align:center;">
            <h4 style="color:#ffb800;">Gorduras</h4>
            <p style="font-size:28px; font-weight:800;">{macros['fat']}g</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 🏋️ Sugestão de Treino")
        st.info(workout_suggestion)

        if st.button("Aplicar estas metas ao meu diário", use_container_width=True):
            store.set_daily_goals(user.id, daily_calories, macros['protein'])
            st.success("Metas de calorias e proteína atualizadas no seu diário de hoje!")

    st.markdown('</div>', unsafe_allow_html=True)

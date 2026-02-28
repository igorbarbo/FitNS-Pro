# pages/meal_plan.py
import streamlit as st
from modules.header import render_header
from modules.navigation import render_navigation
from utils.helpers import (
    calculate_tmb, get_activity_factor, calculate_daily_calories,
    calculate_macros, generate_meal_plan_dynamic
)

def show():
    try:
        user = st.session_state.user
        service = st.session_state.service
        store = service.store

        profile = store.get_user_profile(user.id)
        if not profile:
            st.warning("Você ainda não preencheu seu perfil. Vá em 'Perfil' para configurar.")
            st.stop()

        tmb = calculate_tmb(profile.weight, profile.height, profile.age, profile.gender)
        activity_factor = get_activity_factor(profile.activity_level)
        daily_calories = calculate_daily_calories(tmb, activity_factor, profile.goal)
        macros = calculate_macros(profile.weight, daily_calories, profile.goal)

        render_header(user)
        render_navigation()
        st.markdown('<div class="slide-in">', unsafe_allow_html=True)

        st.markdown("""
        <div style="margin-bottom: 20px;">
            <h2 style="margin:0; font-size: 24px;">🍽️ Plano Alimentar</h2>
            <p style="color: #8b8b9a; font-size: 12px; margin-top: 5px;">Sugestões para o seu dia</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        col1.metric("Calorias", f"{daily_calories} kcal")
        col2.metric("Proteína", f"{macros['protein']}g")
        col3.metric("Carboidratos", f"{macros['carbs']}g")

        # Gerar plano dinâmico
        meal_plan = generate_meal_plan_dynamic(daily_calories, macros['protein'], macros['carbs'], macros['fat'])

        st.markdown("### 🥗 Refeições sugeridas (quantidades em gramas)")
        totais_dia = {"cal": 0, "prot": 0, "carb": 0, "fat": 0}
        
        for meal_name, foods in meal_plan.items():
            with st.expander(meal_name, expanded=True):
                total_cal = 0
                total_prot = 0
                total_carb = 0
                total_fat = 0
                for food in foods:
                    name, qtd, cal, prot, carb, fat = food
                    st.markdown(f"- {name}: **{qtd}g** – {cal:.0f} kcal | {prot:.1f}g prot | {carb:.1f}g carb | {fat:.1f}g fat")
                    total_cal += cal
                    total_prot += prot
                    total_carb += carb
                    total_fat += fat
                st.markdown(f"**Totais da refeição:** {total_cal:.0f} kcal, {total_prot:.1f}g prot, {total_carb:.1f}g carb, {total_fat:.1f}g fat")
                st.markdown("---")
                totais_dia["cal"] += total_cal
                totais_dia["prot"] += total_prot
                totais_dia["carb"] += total_carb
                totais_dia["fat"] += total_fat

        st.markdown(f"### 📊 Totais do dia: {totais_dia['cal']:.0f} kcal, {totais_dia['prot']:.1f}g prot, {totais_dia['carb']:.1f}g carb, {totais_dia['fat']:.1f}g fat")
        
        if st.button("➕ Adicionar estas refeições ao diário", use_container_width=True):
            st.info("Funcionalidade em desenvolvimento: em breve você poderá adicionar todas de uma vez!")

        st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Erro na página de plano alimentar: {e}")
        import traceback
        st.code(traceback.format_exc())

# pages/meal_plan.py
import streamlit as st
from modules.header import render_header
from modules.navigation import render_navigation
from utils.helpers import (
    calculate_tmb, get_activity_factor, calculate_daily_calories,
    calculate_macros, optimize_meal_plan
)

def distribute_to_meals(foods, meal_percentages):
    """
    Distribui os alimentos totais em refeições baseado nos percentuais de calorias.
    Retorna um dicionário com cada refeição e os alimentos com quantidades proporcionais.
    """
    meals = {}
    for meal, pct in meal_percentages.items():
        meals[meal] = []
        for food in foods:
            # Calcula a quantidade proporcional para esta refeição
            qtd_meal = food["quantity"] * pct
            if qtd_meal >= 5:  # só inclui se tiver pelo menos 5g
                meals[meal].append({
                    "name": food["name"],
                    "quantity": round(qtd_meal, 1),
                    "cal": round(food["cal"] * pct, 1),
                    "prot": round(food["prot"] * pct, 1),
                    "carb": round(food["carb"] * pct, 1),
                    "fat": round(food["fat"] * pct, 1)
                })
    return meals

def show():
    try:
        user = st.session_state.user
        service = st.session_state.service
        store = service.store

        profile = store.get_user_profile(user.id)
        if not profile:
            st.warning("Você ainda não preencheu seu perfil. Vá em 'Perfil' para configurar.")
            st.stop()

        # Calcula metas
        tmb = calculate_tmb(profile.weight, profile.height, profile.age, profile.gender)
        activity_factor = get_activity_factor(profile.activity_level)
        daily_calories = calculate_daily_calories(tmb, activity_factor, profile.goal)
        macros = calculate_macros(profile.weight, daily_calories, profile.goal)

        render_header(user)
        render_navigation()
        st.markdown('<div class="slide-in">', unsafe_allow_html=True)

        st.markdown("""
        <div style="margin-bottom: 20px;">
            <h2 style="margin:0; font-size: 24px;">🍽️ Plano Alimentar Diário</h2>
            <p style="color: #8b8b9a; font-size: 12px; margin-top: 5px;">Refeições distribuídas ao longo do dia</p>
        </div>
        """, unsafe_allow_html=True)

        # Exibe as metas
        col1, col2, col3 = st.columns(3)
        col1.metric("Calorias", f"{daily_calories} kcal")
        col2.metric("Proteína", f"{macros['protein']}g")
        col3.metric("Carboidratos", f"{macros['carbs']}g")

        # Botão para gerar o plano
        if st.button("🔍 Gerar Plano Alimentar", use_container_width=True, type="primary"):
            with st.spinner("Calculando a melhor combinação..."):
                meal_plan = optimize_meal_plan(
                    daily_calories, 
                    macros['protein'], 
                    macros['carbs'], 
                    macros['fat']
                )

            if meal_plan:
                st.success("✅ Plano gerado com sucesso!")
                
                # Distribuição percentual típica das refeições
                meal_pcts = {
                    "Café da manhã": 0.20,
                    "Lanche da manhã": 0.10,
                    "Almoço": 0.35,
                    "Lanche da tarde": 0.15,
                    "Jantar": 0.20
                }
                
                # Distribui os alimentos nas refeições
                meals = distribute_to_meals(meal_plan, meal_pcts)
                
                # Exibe cada refeição
                for meal_name, foods in meals.items():
                    if foods:  # só mostra se tiver alimentos
                        with st.expander(f"**{meal_name}**", expanded=True):
                            total_cal = 0
                            total_prot = 0
                            total_carb = 0
                            total_fat = 0
                            for food in foods:
                                st.markdown(f"- {food['name']}: **{food['quantity']}g** – {food['cal']} kcal | {food['prot']}g prot | {food['carb']}g carb | {food['fat']}g fat")
                                total_cal += food['cal']
                                total_prot += food['prot']
                                total_carb += food['carb']
                                total_fat += food['fat']
                            st.markdown(f"**Totais da refeição:** {total_cal:.0f} kcal, {total_prot:.1f}g prot, {total_carb:.1f}g carb, {total_fat:.1f}g fat")
                
                # Totais do dia (para conferência)
                total_cal = sum(food['cal'] for food in meal_plan)
                total_prot = sum(food['prot'] for food in meal_plan)
                total_carb = sum(food['carb'] for food in meal_plan)
                total_fat = sum(food['fat'] for food in meal_plan)
                
                st.markdown("---")
                st.markdown(f"### 📊 Totais do dia: {total_cal:.0f} kcal, {total_prot:.1f}g prot, {total_carb:.1f}g carb, {total_fat:.1f}g fat")
                st.caption(f"Calorias: {total_cal:.0f}/{daily_calories} ({abs(total_cal-daily_calories):.0f} de diferença)")
            else:
                st.error("❌ Não foi possível encontrar uma combinação exata. Tente ajustar as metas.")
        else:
            st.info("Clique no botão acima para gerar seu plano alimentar personalizado.")

        st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Erro na página de plano alimentar: {e}")
        import traceback
        st.code(traceback.format_exc())

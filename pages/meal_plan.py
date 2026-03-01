# pages/meal_plan.py
import streamlit as st
from modules.header import render_header
from modules.navigation import render_navigation
from utils.helpers import (
    calculate_tmb, get_activity_factor, calculate_daily_calories,
    calculate_macros, optimize_meal_plan
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

        # Recalcula metas (ou poderia usar as salvas no perfil)
        tmb = calculate_tmb(profile.weight, profile.height, profile.age, profile.gender)
        activity_factor = get_activity_factor(profile.activity_level)
        daily_calories = calculate_daily_calories(tmb, activity_factor, profile.goal)
        macros = calculate_macros(profile.weight, daily_calories, profile.goal)

        render_header(user)
        render_navigation()
        st.markdown('<div class="slide-in">', unsafe_allow_html=True)

        st.markdown("""
        <div style="margin-bottom: 20px;">
            <h2 style="margin:0; font-size: 24px;">🍽️ Plano Alimentar Otimizado</h2>
            <p style="color: #8b8b9a; font-size: 12px; margin-top: 5px;">Quantidades calculadas para bater suas metas exatas</p>
        </div>
        """, unsafe_allow_html=True)

        # Exibe as metas
        col1, col2, col3 = st.columns(3)
        col1.metric("Calorias", f"{daily_calories} kcal")
        col2.metric("Proteína", f"{macros['protein']}g")
        col3.metric("Carboidratos", f"{macros['carbs']}g")

        # Botão para gerar o plano (evita execução automática a cada carregamento)
        if st.button("🔍 Gerar Plano Otimizado", use_container_width=True, type="primary"):
            with st.spinner("Calculando a combinação ideal..."):
                meal_plan = optimize_meal_plan(
                    daily_calories, 
                    macros['protein'], 
                    macros['carbs'], 
                    macros['fat']
                )

            if meal_plan:
                st.success("✅ Plano gerado com sucesso!")
                st.markdown("### 🥗 Alimentos recomendados para o dia")
                
                total_cal = 0
                total_prot = 0
                total_carb = 0
                total_fat = 0
                
                for item in meal_plan:
                    st.markdown(f"- **{item['name']}**: {item['quantity']}g – {item['cal']} kcal | {item['prot']}g prot | {item['carb']}g carb | {item['fat']}g fat")
                    total_cal += item['cal']
                    total_prot += item['prot']
                    total_carb += item['carb']
                    total_fat += item['fat']
                
                st.markdown("---")
                st.markdown(f"### 📊 Totais do dia: {total_cal:.0f} kcal, {total_prot:.1f}g prot, {total_carb:.1f}g carb, {total_fat:.1f}g fat")
                
                # Mostra quão próximo das metas
                st.caption(f"Calorias: {total_cal}/{daily_calories} ({abs(total_cal-daily_calories):.0f} de diferença)")
            else:
                st.error("❌ Não foi possível encontrar uma combinação exata. Tente ajustar as metas ou consulte um nutricionista.")
        else:
            st.info("Clique no botão acima para gerar seu plano alimentar personalizado.")

        st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Erro na página de plano alimentar: {e}")
        import traceback
        st.code(traceback.format_exc())

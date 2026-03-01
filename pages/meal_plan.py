# pages/meal_plan.py
import streamlit as st
import pulp
from modules.header import render_header
from modules.navigation import render_navigation
from utils.helpers import (
    calculate_tmb, get_activity_factor, calculate_daily_calories,
    calculate_macros
)
from utils.food_database import FOODS

# Estrutura das refeições com os alimentos permitidos em cada uma
MEAL_STRUCTURE = {
    "Café da manhã": {
        "foods": ["Ovo", "Pão integral", "Banana", "Aveia"],
        "cal_pct": 0.20  # 20% das calorias do dia
    },
    "Lanche da manhã": {
        "foods": ["Iogurte grego", "Castanhas", "Maçã"],
        "cal_pct": 0.10
    },
    "Almoço": {
        "foods": ["Frango grelhado", "Arroz integral cozido", "Brócolis cozido", "Azeite de oliva"],
        "cal_pct": 0.35
    },
    "Lanche da tarde": {
        "foods": ["Whey protein", "Banana", "Aveia"],
        "cal_pct": 0.15
    },
    "Jantar": {
        "foods": ["Peixe grelhado", "Batata doce cozida", "Brócolis cozido", "Azeite de oliva"],
        "cal_pct": 0.20
    }
}

def optimize_meal(meal_name, meal_data, cal_goal, prot_goal, carb_goal, fat_goal):
    """
    Otimiza as quantidades dos alimentos de uma refeição para atingir as metas parciais.
    Retorna lista de alimentos com quantidades em gramas.
    """
    # Filtra os alimentos da refeição
    meal_foods = [f for f in FOODS if f["name"] in meal_data["foods"]]
    if not meal_foods:
        return []
    
    prob = pulp.LpProblem(f"Otimização {meal_name}", pulp.LpMinimize)
    
    # Variáveis: quantidade de cada alimento em gramas
    food_vars = [pulp.LpVariable(f"{meal_name}_{i}", lowBound=0, upBound=300) for i in range(len(meal_foods))]
    
    # Variáveis de desvio
    dev_cal = pulp.LpVariable(f"dev_cal_{meal_name}", lowBound=0)
    dev_prot = pulp.LpVariable(f"dev_prot_{meal_name}", lowBound=0)
    dev_carb = pulp.LpVariable(f"dev_carb_{meal_name}", lowBound=0)
    dev_fat = pulp.LpVariable(f"dev_fat_{meal_name}", lowBound=0)
    
    # Restrições: soma dos nutrientes deve estar próxima da meta
    prob += pulp.lpSum([(f["cal"]/100) * food_vars[i] for i, f in enumerate(meal_foods)]) <= cal_goal + dev_cal
    prob += pulp.lpSum([(f["cal"]/100) * food_vars[i] for i, f in enumerate(meal_foods)]) >= cal_goal - dev_cal
    
    prob += pulp.lpSum([(f["prot"]/100) * food_vars[i] for i, f in enumerate(meal_foods)]) <= prot_goal + dev_prot
    prob += pulp.lpSum([(f["prot"]/100) * food_vars[i] for i, f in enumerate(meal_foods)]) >= prot_goal - dev_prot
    
    prob += pulp.lpSum([(f["carb"]/100) * food_vars[i] for i, f in enumerate(meal_foods)]) <= carb_goal + dev_carb
    prob += pulp.lpSum([(f["carb"]/100) * food_vars[i] for i, f in enumerate(meal_foods)]) >= carb_goal - dev_carb
    
    prob += pulp.lpSum([(f["fat"]/100) * food_vars[i] for i, f in enumerate(meal_foods)]) <= fat_goal + dev_fat
    prob += pulp.lpSum([(f["fat"]/100) * food_vars[i] for i, f in enumerate(meal_foods)]) >= fat_goal - dev_fat
    
    # Função objetivo: minimizar desvios e quantidade total
    prob += dev_cal*10 + dev_prot*10 + dev_carb*10 + dev_fat*10 + pulp.lpSum(food_vars)/100
    
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    
    if prob.status == pulp.LpStatusOptimal:
        result = []
        for i, var in enumerate(food_vars):
            qtd = var.varValue
            if qtd and qtd > 1:
                food = meal_foods[i]
                result.append({
                    "name": food["name"],
                    "quantity": round(qtd, 1),
                    "cal": round((food["cal"]/100) * qtd, 1),
                    "prot": round((food["prot"]/100) * qtd, 1),
                    "carb": round((food["carb"]/100) * qtd, 1),
                    "fat": round((food["fat"]/100) * qtd, 1)
                })
        return result
    else:
        return None

def show():
    try:
        user = st.session_state.user
        service = st.session_state.service
        store = service.store

        profile = store.get_user_profile(user.id)
        if not profile:
            st.warning("Você ainda não preencheu seu perfil. Vá em 'Perfil' para configurar.")
            st.stop()

        # Calcula metas totais
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
            <p style="color: #8b8b9a; font-size: 12px; margin-top: 5px;">Refeições balanceadas com alimentos específicos</p>
        </div>
        """, unsafe_allow_html=True)

        # Exibe as metas totais
        col1, col2, col3 = st.columns(3)
        col1.metric("Calorias", f"{daily_calories} kcal")
        col2.metric("Proteína", f"{macros['protein']}g")
        col3.metric("Carboidratos", f"{macros['carbs']}g")

        if st.button("🔍 Gerar Plano Alimentar", use_container_width=True, type="primary"):
            with st.spinner("Calculando refeições..."):
                meal_plans = {}
                total_cal = 0
                total_prot = 0
                total_carb = 0
                total_fat = 0
                
                # Para cada refeição, calcula as metas parciais e otimiza
                for meal_name, meal_data in MEAL_STRUCTURE.items():
                    cal_meal = daily_calories * meal_data["cal_pct"]
                    # Distribui proteínas, carboidratos e gorduras proporcionalmente (simplificado)
                    # Poderíamos usar percentuais específicos, mas por simplicidade usamos o mesmo percentual
                    prot_meal = macros['protein'] * meal_data["cal_pct"]
                    carb_meal = macros['carbs'] * meal_data["cal_pct"]
                    fat_meal = macros['fat'] * meal_data["cal_pct"]
                    
                    result = optimize_meal(meal_name, meal_data, cal_meal, prot_meal, carb_meal, fat_meal)
                    if result:
                        meal_plans[meal_name] = result
                        for food in result:
                            total_cal += food["cal"]
                            total_prot += food["prot"]
                            total_carb += food["carb"]
                            total_fat += food["fat"]
                    else:
                        st.warning(f"Não foi possível otimizar {meal_name}. Tente novamente.")
                
                if meal_plans:
                    st.success("✅ Plano gerado com sucesso!")
                    
                    # Exibe cada refeição
                    for meal_name, foods in meal_plans.items():
                        with st.expander(f"**{meal_name}**", expanded=True):
                            cal_meal = sum(f["cal"] for f in foods)
                            prot_meal = sum(f["prot"] for f in foods)
                            carb_meal = sum(f["carb"] for f in foods)
                            fat_meal = sum(f["fat"] for f in foods)
                            for food in foods:
                                st.markdown(f"- {food['name']}: **{food['quantity']}g** – {food['cal']} kcal | {food['prot']}g prot | {food['carb']}g carb | {food['fat']}g fat")
                            st.markdown(f"**Totais da refeição:** {cal_meal:.0f} kcal, {prot_meal:.1f}g prot, {carb_meal:.1f}g carb, {fat_meal:.1f}g fat")
                    
                    # Totais do dia
                    st.markdown("---")
                    st.markdown(f"### 📊 Totais do dia: {total_cal:.0f} kcal, {total_prot:.1f}g prot, {total_carb:.1f}g carb, {total_fat:.1f}g fat")
                    st.caption(f"Calorias: {total_cal:.0f}/{daily_calories} ({abs(total_cal-daily_calories):.0f} de diferença)")
                else:
                    st.error("❌ Não foi possível gerar o plano. Tente ajustar as metas.")
        else:
            st.info("Clique no botão acima para gerar seu plano alimentar personalizado.")

        st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Erro na página de plano alimentar: {e}")
        import traceback
        st.code(traceback.format_exc())

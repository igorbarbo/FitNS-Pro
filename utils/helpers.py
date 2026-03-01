# utils/helpers.py
import pulp
from .food_database import FOODS

def optimize_meal_plan(cal_goal, prot_goal, carb_goal, fat_goal):
    """
    Usa programação linear para encontrar quantidades (em gramas) de alimentos
    que atendam às metas de macronutrientes, minimizando desvios.
    """
    prob = pulp.LpProblem("Dieta", pulp.LpMinimize)
    
    # Variáveis: quantidade de cada alimento em gramas (0 a 500g)
    food_vars = [pulp.LpVariable(f"x{i}", lowBound=0, upBound=500) for i in range(len(FOODS))]
    
    # Variáveis de desvio (folga) para cada macro
    dev_cal = pulp.LpVariable("dev_cal", lowBound=0)
    dev_prot = pulp.LpVariable("dev_prot", lowBound=0)
    dev_carb = pulp.LpVariable("dev_carb", lowBound=0)
    dev_fat = pulp.LpVariable("dev_fat", lowBound=0)
    
    # Restrições: soma dos nutrientes deve estar próxima da meta (± desvio)
    prob += pulp.lpSum([(food["cal"]/100) * food_vars[i] for i, food in enumerate(FOODS)]) <= cal_goal + dev_cal
    prob += pulp.lpSum([(food["cal"]/100) * food_vars[i] for i, food in enumerate(FOODS)]) >= cal_goal - dev_cal
    
    prob += pulp.lpSum([(food["prot"]/100) * food_vars[i] for i, food in enumerate(FOODS)]) <= prot_goal + dev_prot
    prob += pulp.lpSum([(food["prot"]/100) * food_vars[i] for i, food in enumerate(FOODS)]) >= prot_goal - dev_prot
    
    prob += pulp.lpSum([(food["carb"]/100) * food_vars[i] for i, food in enumerate(FOODS)]) <= carb_goal + dev_carb
    prob += pulp.lpSum([(food["carb"]/100) * food_vars[i] for i, food in enumerate(FOODS)]) >= carb_goal - dev_carb
    
    prob += pulp.lpSum([(food["fat"]/100) * food_vars[i] for i, food in enumerate(FOODS)]) <= fat_goal + dev_fat
    prob += pulp.lpSum([(food["fat"]/100) * food_vars[i] for i, food in enumerate(FOODS)]) >= fat_goal - dev_fat
    
    # Função objetivo: minimizar os desvios (peso 10) e a quantidade total de alimentos (peso 1/100)
    prob += dev_cal*10 + dev_prot*10 + dev_carb*10 + dev_fat*10 + pulp.lpSum(food_vars)/100
    
    # Resolver
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    
    if prob.status == pulp.LpStatusOptimal:
        result = []
        for i, var in enumerate(food_vars):
            qtd = var.varValue
            if qtd and qtd > 1:  # ignora quantidades muito pequenas
                food = FOODS[i]
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

# utils/helpers.py
import pulp
from .food_database import FOODS

def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)

def calculate_tmb(weight_kg: float, height_cm: float, age: int, gender: str) -> float:
    if gender == "male":
        tmb = 88.36 + (13.4 * weight_kg) + (4.8 * height_cm) - (5.7 * age)
    else:
        tmb = 447.6 + (9.2 * weight_kg) + (3.1 * height_cm) - (4.3 * age)
    return round(tmb)

def get_activity_factor(level: str) -> float:
    factors = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very_active": 1.9
    }
    return factors.get(level, 1.2)

def calculate_daily_calories(tmb: float, activity_factor: float, goal: str) -> int:
    if goal == "lose":
        factor = 0.8
    elif goal == "gain":
        factor = 1.1
    else:
        factor = 1.0
    return int(tmb * activity_factor * factor)

def calculate_macros(weight_kg: float, total_calories: int, goal: str) -> dict:
    if goal == "lose":
        protein_per_kg = 1.8
    else:
        protein_per_kg = 2.0

    protein_g = round(weight_kg * protein_per_kg)
    protein_cal = protein_g * 4

    fat_cal = total_calories * 0.25
    fat_g = round(fat_cal / 9)

    carb_cal = total_calories - protein_cal - fat_cal
    carb_g = round(carb_cal / 4)

    return {
        "protein": protein_g,
        "fat": fat_g,
        "carbs": carb_g
    }

def generate_workout_plan(goal: str) -> dict:
    """
    Retorna um plano de treino semanal baseado no objetivo.
    """
    plans = {
        "gain": {
            "Segunda": {
                "name": "Peito e Tríceps",
                "exercises": [
                    ("Supino reto", "4x8-12", ""),
                    ("Crucifixo", "3x12-15", ""),
                    ("Tríceps pulley", "4x10-12", ""),
                    ("Tríceps francês", "3x12", ""),
                    ("Flexão de braço", "3x falha", "")
                ]
            },
            "Terça": {
                "name": "Costas e Bíceps",
                "exercises": [
                    ("Puxada frontal", "4x10", ""),
                    ("Remada curvada", "4x8-12", ""),
                    ("Rosca direta", "3x10", ""),
                    ("Rosca martelo", "3x12", ""),
                    ("Pull-over", "3x12", "")
                ]
            },
            "Quarta": {
                "name": "Pernas",
                "exercises": [
                    ("Agachamento", "4x8-10", ""),
                    ("Leg press", "4x12", ""),
                    ("Cadeira extensora", "3x15", ""),
                    ("Mesa flexora", "3x15", ""),
                    ("Panturrilha em pé", "4x20", "")
                ]
            },
            "Quinta": {
                "name": "Ombros e Abdômen",
                "exercises": [
                    ("Desenvolvimento", "4x10", ""),
                    ("Elevação lateral", "3x15", ""),
                    ("Encolhimento", "3x12", ""),
                    ("Prancha", "3x45s", ""),
                    ("Abdominal infra", "3x20", "")
                ]
            },
            "Sexta": {
                "name": "Cardio + Full Body",
                "exercises": [
                    ("Corrida", "20 min", ""),
                    ("Polichinelo", "3x30s", ""),
                    ("Burpee", "3x10", ""),
                    ("Mountain climber", "3x30s", "")
                ]
            }
        },
        "lose": {
            "Segunda": {
                "name": "HIIT Full Body",
                "exercises": [
                    ("Polichinelo", "30s", ""),
                    ("Agachamento com salto", "30s", ""),
                    ("Prancha", "30s", ""),
                    ("Mountain climber", "30s", ""),
                    ("Descanso", "15s", "")
                ]
            },
            "Terça": {
                "name": "Musculação leve",
                "exercises": [
                    ("Supino", "3x12", ""),
                    ("Puxada frontal", "3x12", ""),
                    ("Leg press", "3x15", ""),
                    ("Abdominal", "3x20", "")
                ]
            },
            "Quarta": {
                "name": "HIIT + Core",
                "exercises": [
                    ("Corrida intervalada", "20 min", ""),
                    ("Prancha lateral", "3x30s", ""),
                    ("Abdominal bicicleta", "3x20", "")
                ]
            },
            "Quinta": {
                "name": "Musculação moderada",
                "exercises": [
                    ("Remada", "3x12", ""),
                    ("Desenvolvimento", "3x12", ""),
                    ("Cadeira flexora", "3x15", ""),
                    ("Panturrilha", "4x20", "")
                ]
            },
            "Sexta": {
                "name": "Cardio longo",
                "exercises": [
                    ("Caminhada rápida", "40 min", ""),
                    ("Alongamento", "10 min", "")
                ]
            }
        },
        "maintain": {
            "Segunda": {
                "name": "Treino A - Superior",
                "exercises": [
                    ("Supino", "3x10", ""),
                    ("Puxada", "3x10", ""),
                    ("Desenvolvimento", "3x10", ""),
                    ("Rosca", "3x10", "")
                ]
            },
            "Terça": {
                "name": "Cardio moderado",
                "exercises": [
                    ("Corrida", "30 min", ""),
                    ("Alongamento", "10 min", "")
                ]
            },
            "Quarta": {
                "name": "Treino B - Inferior",
                "exercises": [
                    ("Agachamento", "3x12", ""),
                    ("Leg press", "3x12", ""),
                    ("Cadeira extensora", "3x12", ""),
                    ("Mesa flexora", "3x12", "")
                ]
            },
            "Quinta": {
                "name": "Treino C - Completo",
                "exercises": [
                    ("Circuito 5 exercícios", "3x12", ""),
                    ("Abdominal", "3x15", "")
                ]
            },
            "Sexta": {
                "name": "Atividade livre",
                "exercises": [
                    ("Caminhada ou esporte", "30 min", "")
                ]
            }
        }
    }
    return plans.get(goal, plans["maintain"])

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

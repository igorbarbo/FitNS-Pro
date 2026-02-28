# utils/helpers.py
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

def generate_meal_plan_dynamic(calories_goal: int, protein_goal: int, carb_goal: int, fat_goal: int) -> dict:
    """
    Gera um plano alimentar com quantidades calculadas para bater as metas.
    Distribui as calorias em 5 refeições com percentuais fixos.
    """
    # Percentuais de distribuição das calorias por refeição
    meal_distribution = {
        "Café da manhã": 0.20,
        "Lanche da manhã": 0.10,
        "Almoço": 0.35,
        "Lanche da tarde": 0.15,
        "Jantar": 0.20
    }
    
    # Metas para cada refeição (calorias)
    meal_calories = {meal: round(calories_goal * pct) for meal, pct in meal_distribution.items()}
    
    # Estrutura do plano
    meal_plan = {}
    
    # Café da manhã: ovos, pão, banana
    cafe = []
    # Ovos (2 unidades ~ 100g)
    qtd_ovo = 100  # gramas
    cal_ovo, prot_ovo, carb_ovo, fat_ovo = [FOODS["ovo"][k] for k in ("cal", "prot", "carb", "fat")]
    cafe.append(("Ovos (2 unidades)", qtd_ovo, cal_ovo * qtd_ovo/100, prot_ovo * qtd_ovo/100, carb_ovo * qtd_ovo/100, fat_ovo * qtd_ovo/100))
    
    # Pão integral (50g)
    qtd_pao = 50
    cal_pao, prot_pao, carb_pao, fat_pao = [FOODS["pão_integral"][k] for k in ("cal", "prot", "carb", "fat")]
    cafe.append(("Pão integral (2 fatias)", qtd_pao, cal_pao * qtd_pao/100, prot_pao * qtd_pao/100, carb_pao * qtd_pao/100, fat_pao * qtd_pao/100))
    
    # Banana (100g)
    qtd_banana = 100
    cal_banana, prot_banana, carb_banana, fat_banana = [FOODS["banana"][k] for k in ("cal", "prot", "carb", "fat")]
    cafe.append(("Banana", qtd_banana, cal_banana * qtd_banana/100, prot_banana * qtd_banana/100, carb_banana * qtd_banana/100, fat_banana * qtd_banana/100))
    
    meal_plan["Café da manhã"] = cafe
    
    # Lanche da manhã: iogurte + castanhas
    lanche_manha = []
    qtd_iogurte = 170  # 1 pote
    cal_iog, prot_iog, carb_iog, fat_iog = [FOODS["iogurte_grego"][k] for k in ("cal", "prot", "carb", "fat")]
    lanche_manha.append(("Iogurte grego", qtd_iogurte, cal_iog * qtd_iogurte/100, prot_iog * qtd_iogurte/100, carb_iog * qtd_iogurte/100, fat_iog * qtd_iogurte/100))
    
    qtd_castanha = 20
    cal_cast, prot_cast, carb_cast, fat_cast = [FOODS["castanhas"][k] for k in ("cal", "prot", "carb", "fat")]
    lanche_manha.append(("Castanhas", qtd_castanha, cal_cast * qtd_castanha/100, prot_cast * qtd_castanha/100, carb_cast * qtd_castanha/100, fat_cast * qtd_castanha/100))
    
    meal_plan["Lanche da manhã"] = lanche_manha
    
    # Almoço: frango, arroz, brócolis, azeite
    almoco = []
    qtd_frango = 200
    cal_fr, prot_fr, carb_fr, fat_fr = [FOODS["frango_grelhado"][k] for k in ("cal", "prot", "carb", "fat")]
    almoco.append(("Frango grelhado", qtd_frango, cal_fr * qtd_frango/100, prot_fr * qtd_frango/100, carb_fr * qtd_frango/100, fat_fr * qtd_frango/100))
    
    qtd_arroz = 200
    cal_arroz, prot_arroz, carb_arroz, fat_arroz = [FOODS["arroz_integral"][k] for k in ("cal", "prot", "carb", "fat")]
    almoco.append(("Arroz integral", qtd_arroz, cal_arroz * qtd_arroz/100, prot_arroz * qtd_arroz/100, carb_arroz * qtd_arroz/100, fat_arroz * qtd_arroz/100))
    
    qtd_brocolis = 100
    cal_bro, prot_bro, carb_bro, fat_bro = [FOODS["brócolis"][k] for k in ("cal", "prot", "carb", "fat")]
    almoco.append(("Brócolis", qtd_brocolis, cal_bro * qtd_brocolis/100, prot_bro * qtd_brocolis/100, carb_bro * qtd_brocolis/100, fat_bro * qtd_brocolis/100))
    
    qtd_azeite = 15
    cal_azeite, prot_azeite, carb_azeite, fat_azeite = [FOODS["azeite"][k] for k in ("cal", "prot", "carb", "fat")]
    almoco.append(("Azeite", qtd_azeite, cal_azeite * qtd_azeite/100, prot_azeite * qtd_azeite/100, carb_azeite * qtd_azeite/100, fat_azeite * qtd_azeite/100))
    
    meal_plan["Almoço"] = almoco
    
    # Lanche da tarde: whey + maçã
    lanche_tarde = []
    qtd_whey = 30  # 1 scoop
    cal_whey, prot_whey, carb_whey, fat_whey = [FOODS["whey"][k] for k in ("cal", "prot", "carb", "fat")]
    lanche_tarde.append(("Whey protein", qtd_whey, cal_whey * qtd_whey/100, prot_whey * qtd_whey/100, carb_whey * qtd_whey/100, fat_whey * qtd_whey/100))
    
    qtd_maca = 150  # 1 unidade média
    cal_maca, prot_maca, carb_maca, fat_maca = [FOODS["maçã"][k] for k in ("cal", "prot", "carb", "fat")]
    lanche_tarde.append(("Maçã", qtd_maca, cal_maca * qtd_maca/100, prot_maca * qtd_maca/100, carb_maca * qtd_maca/100, fat_maca * qtd_maca/100))
    
    meal_plan["Lanche da tarde"] = lanche_tarde
    
    # Jantar: peixe, batata doce, salada (brócolis)
    jantar = []
    qtd_peixe = 200
    cal_peixe, prot_peixe, carb_peixe, fat_peixe = [FOODS["peixe_grelhado"][k] for k in ("cal", "prot", "carb", "fat")]
    jantar.append(("Peixe grelhado", qtd_peixe, cal_peixe * qtd_peixe/100, prot_peixe * qtd_peixe/100, carb_peixe * qtd_peixe/100, fat_peixe * qtd_peixe/100))
    
    qtd_batata = 200
    cal_bat, prot_bat, carb_bat, fat_bat = [FOODS["batata_doce"][k] for k in ("cal", "prot", "carb", "fat")]
    jantar.append(("Batata doce", qtd_batata, cal_bat * qtd_batata/100, prot_bat * qtd_batata/100, carb_bat * qtd_batata/100, fat_bat * qtd_batata/100))
    
    qtd_salada = 100
    jantar.append(("Salada verde (brócolis)", qtd_salada, cal_bro * qtd_salada/100, prot_bro * qtd_salada/100, carb_bro * qtd_salada/100, fat_bro * qtd_salada/100))
    
    meal_plan["Jantar"] = jantar
    
    return meal_plan

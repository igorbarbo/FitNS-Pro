# utils/helpers.py
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

def generate_meal_plan(calories: int, macros: dict) -> dict:
    meal_plan = {
        "Café da manhã": [
            ("Ovos mexidos (2 unidades)", 140, 12, 1, 10),
            ("Pão integral (1 fatia)", 70, 3, 15, 1),
            ("Banana (1 unidade)", 105, 1, 27, 0)
        ],
        "Lanche da manhã": [
            ("Iogurte grego (1 pote)", 150, 15, 5, 8),
            ("Castanhas (10g)", 60, 2, 2, 5)
        ],
        "Almoço": [
            ("Frango grelhado (150g)", 247, 46, 0, 5),
            ("Arroz integral (100g)", 112, 2.6, 23, 1),
            ("Brócolis (100g)", 34, 2.8, 4, 0.4),
            ("Azeite (1 colher)", 120, 0, 0, 14)
        ],
        "Lanche da tarde": [
            ("Whey protein (1 scoop)", 120, 24, 3, 2),
            ("Maçã (1 unidade)", 95, 0.5, 25, 0.3)
        ],
        "Jantar": [
            ("Peixe grelhado (150g)", 200, 30, 0, 8),
            ("Batata doce (150g)", 130, 2, 30, 0.2),
            ("Salada verde", 50, 2, 8, 1)
        ]
    }
    return meal_plan

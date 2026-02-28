# utils/helpers.py

def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """Calcula IMC: peso / (altura em metros)²"""
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)

def calculate_tmb(weight_kg: float, height_cm: float, age: int, gender: str) -> float:
    """Taxa Metabólica Basal (fórmula de Harris-Benedict)"""
    if gender == "male":
        tmb = 88.36 + (13.4 * weight_kg) + (4.8 * height_cm) - (5.7 * age)
    else:  # female
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
        factor = 0.8  # déficit de 20%
    elif goal == "gain":
        factor = 1.1  # superávit de 10%
    else:  # maintain
        factor = 1.0
    return int(tmb * activity_factor * factor)

def calculate_macros(weight_kg: float, total_calories: int, goal: str) -> dict:
    """
    Retorna dicionário com proteína (g), gordura (g) e carboidrato (g)
    """
    if goal == "lose":
        protein_per_kg = 1.8
    else:  # maintain ou gain
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

def suggest_workout(goal: str) -> str:
    """Sugestão simples de treino baseada no objetivo"""
    if goal == "lose":
        return "🔥 Treino HIIT 3x/semana + Musculação 2x/semana (foco em queima de gordura)"
    elif goal == "gain":
        return "💪 Musculação pesada 4-5x/semana (foco em hipertrofia) + superávit calórico"
    else:
        return "⚖️ Musculação 3x/semana + Cardio moderado 2x/semana (manutenção)"

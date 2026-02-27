"""
Cálculos de fitness, nutrição e metabolismo
"""
import math

def calculate_bmi(weight_kg: float, height_cm: float) -> dict:
    """Calcula IMC e retorna classificação"""
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    
    if bmi < 18.5:
        category = "Abaixo do peso"
        color = "#F9A825"
    elif bmi < 25:
        category = "Peso normal"
        color = "#1A936F"
    elif bmi < 30:
        category = "Sobrepeso"
        color = "#FF6B35"
    else:
        category = "Obesidade"
        color = "#E63946"
    
    ideal_weight_low = 18.5 * (height_m ** 2)
    ideal_weight_high = 24.9 * (height_m ** 2)
    
    return {
        'bmi': round(bmi, 1),
        'category': category,
        'color': color,
        'ideal_range': f"{ideal_weight_low:.1f} - {ideal_weight_high:.1f} kg"
    }

def calculate_tdee(weight_kg: float, height_cm: float, age: int, 
                   gender: str, activity_level: str) -> dict:
    """Calcula TDEE usando Mifflin-St Jeor"""
    if gender.lower() == 'masculino':
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161
    
    multipliers = {
        'sedentario': 1.2,
        'leve': 1.375,
        'moderado': 1.55,
        'ativo': 1.725,
        'muito_ativo': 1.9
    }
    
    tdee = bmr * multipliers.get(activity_level, 1.2)
    
    return {
        'bmr': round(bmr),
        'tdee': round(tdee),
        'activity_multiplier': multipliers.get(activity_level, 1.2)
    }

def calculate_macros(calories: int, goal: str) -> dict:
    """Calcula distribuição de macronutrientes"""
    splits = {
        'perder_gordura': {'protein': 0.40, 'carbs': 0.30, 'fat': 0.30},
        'ganhar_musculo': {'protein': 0.30, 'carbs': 0.50, 'fat': 0.20},
        'manter_peso': {'protein': 0.30, 'carbs': 0.40, 'fat': 0.30}
    }
    
    split = splits.get(goal, splits['manter_peso'])
    
    protein_cal = calories * split['protein']
    carbs_cal = calories * split['carbs']
    fat_cal = calories * split['fat']
    
    return {
        'protein_g': round(protein_cal / 4),
        'carbs_g': round(carbs_cal / 4),
        'fat_g': round(fat_cal / 9),
        'protein_pct': int(split['protein'] * 100),
        'carbs_pct': int(split['carbs'] * 100),
        'fat_pct': int(split['fat'] * 100)
    }

def calculate_goal_timeline(current_weight: float, target_weight: float, 
                           goal: str) -> dict:
    """Calcula tempo estimado para atingir meta"""
    weight_diff = abs(target_weight - current_weight)
    
    if goal == 'perder_gordura':
        # Perda segura: 0.5-1kg por semana
        weeks_low = weight_diff / 1.0
        weeks_high = weight_diff / 0.5
        rate = "0.5 - 1.0 kg/semana"
    elif goal == 'ganhar_musculo':
        # Ganho muscular: 0.25-0.5kg por semana
        weeks_low = weight_diff / 0.5
        weeks_high = weight_diff / 0.25
        rate = "0.25 - 0.5 kg/semana"
    else:
        return {
            'weeks': 0,
            'months': 0,
            'message': "Manutenção - foco em composição corporal"
        }
    
    weeks_avg = (weeks_low + weeks_high) / 2
    months = weeks_avg / 4.33
    
    return {
        'weeks': round(weeks_avg),
        'months': round(months, 1),
        'rate': rate,
        'message': f"Meta em aproximadamente {round(months, 1)} meses"
    }

def get_workout_recommendation(goal: str, level: str) -> dict:
    """Retorna recomendações de treino baseadas no objetivo"""
    recommendations = {
        'perder_gordura': {
            'foco': 'Cardio + HIIT + Musculação',
            'frequencia': '5-6x por semana',
            'cardio': '30-45 min após treino ou em dias separados',
            'intensidade': 'Moderada a alta'
        },
        'ganhar_musculo': {
            'foco': 'Musculação progressiva',
            'frequencia': '4-5x por semana',
            'cardio': 'Mínimo (2x leve para saúde)',
            'intensidade': 'Alta com descanso adequado'
        },
        'manter_peso': {
            'foco': 'Equilíbrio cardio + força',
            'frequencia': '3-4x por semana',
            'cardio': '2-3x por semana moderado',
            'intensidade': 'Moderada'
        }
    }
    return recommendations.get(goal, recommendations['manter_peso'])
  

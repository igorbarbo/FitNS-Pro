"""
FitNS Pro - Configurações Globais
"""
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Cores do tema
COLORS = {
    'primary': '#FF6B35',
    'secondary': '#004E89',
    'success': '#1A936F',
    'warning': '#F9A825',
    'danger': '#E63946',
    'background': '#0E1117',
    'surface': '#1E1E1E',
    'text': '#FAFAFA'
}

# Metas de calorias por objetivo
CALORIE_ADJUSTMENT = {
    'perder_gordura': -500,
    'ganhar_musculo': 300,
    'manter_peso': 0
}

# Distribuição de macros por objetivo (%)
MACRO_SPLIT = {
    'perder_gordura': {'protein': 40, 'carbs': 30, 'fat': 30},
    'ganhar_musculo': {'protein': 30, 'carbs': 50, 'fat': 20},
    'manter_peso': {'protein': 30, 'carbs': 40, 'fat': 30}
}

# Níveis de atividade
ACTIVITY_MULTIPLIERS = {
    'sedentario': 1.2,
    'leve': 1.375,
    'moderado': 1.55,
    'ativo': 1.725,
    'muito_ativo': 1.9
}

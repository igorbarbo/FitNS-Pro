"""
Gerenciamento de dados CSV e JSON
"""
import os
import json
import pandas as pd
from pathlib import Path

def get_data_path(filename: str) -> str:
    """Retorna path absoluto para arquivo de dados"""
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "data"
    data_dir.mkdir(exist_ok=True)
    return str(data_dir / filename)

def load_csv(filename: str) -> pd.DataFrame:
    """Carrega CSV ou cria DataFrame vazio se não existir"""
    filepath = get_data_path(filename)
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        return pd.DataFrame()

def save_csv(df: pd.DataFrame, filename: str):
    """Salva DataFrame em CSV"""
    filepath = get_data_path(filename)
    df.to_csv(filepath, index=False)

def load_json(filename: str) -> dict:
    """Carrega JSON ou retorna dict vazio"""
    filepath = get_data_path(filename)
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_json(data: dict, filename: str):
    """Salva dict em JSON"""
    filepath = get_data_path(filename)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

# Dados iniciais para popular o app
def get_default_exercises() -> pd.DataFrame:
    """Retorna DataFrame com exercícios padrão"""
    exercises = [
        # Peito
        {"name": "Supino Reto", "muscle": "Peito", "equipment": "Barra", "difficulty": "Intermediário"},
        {"name": "Supino Inclinado", "muscle": "Peito Superior", "equipment": "Barra", "difficulty": "Intermediário"},
        {"name": "Crucifixo", "muscle": "Peito", "equipment": "Halteres", "difficulty": "Iniciante"},
        {"name": "Flexão", "muscle": "Peito", "equipment": "Peso Corporal", "difficulty": "Iniciante"},
        {"name": "Pullover", "muscle": "Peito/Costas", "equipment": "Halter", "difficulty": "Intermediário"},
        
        # Costas
        {"name": "Puxada Frontal", "muscle": "Costas", "equipment": "Máquina", "difficulty": "Iniciante"},
        {"name": "Remada Curvada", "muscle": "Costas", "equipment": "Barra", "difficulty": "Intermediário"},
        {"name": "Remada Unilateral", "muscle": "Costas", "equipment": "Halter", "difficulty": "Iniciante"},
        {"name": "Levantamento Terra", "muscle": "Costas/Pernas", "equipment": "Barra", "difficulty": "Avançado"},
        {"name": "Barra Fixa", "muscle": "Costas", "equipment": "Peso Corporal", "difficulty": "Avançado"},
        
        # Ombros
        {"name": "Desenvolvimento", "muscle": "Ombros", "equipment": "Barra", "difficulty": "Intermediário"},
        {"name": "Elevação Lateral", "muscle": "Ombros", "equipment": "Halteres", "difficulty": "Iniciante"},
        {"name": "Elevação Frontal", "muscle": "Ombros", "equipment": "Halteres", "difficulty": "Iniciante"},
        {"name": "Crucifixo Invertido", "muscle": "Ombros Posteriores", "equipment": "Halteres", "difficulty": "Intermediário"},
        
        # Braços
        {"name": "Rosca Direta", "muscle": "Bíceps", "equipment": "Barra", "difficulty": "Iniciante"},
        {"name": "Rosca Martelo", "muscle": "Bíceps/Braquial", "equipment": "Halteres", "difficulty": "Iniciante"},
        {"name": "Tríceps Testa", "muscle": "Tríceps", "equipment": "Barra/Halter", "difficulty": "Iniciante"},
        {"name": "Tríceps Corda", "muscle": "Tríceps", "equipment": "Máquina", "difficulty": "Iniciante"},
        {"name": "Francês", "muscle": "Tríceps", "equipment": "Halter", "difficulty": "Intermediário"},
        
        # Pernas
        {"name": "Agachamento", "muscle": "Pernas", "equipment": "Barra", "difficulty": "Intermediário"},
        {"name": "Leg Press", "muscle": "Pernas", "equipment": "Máquina", "difficulty": "Iniciante"},
        {"name": "Cadeira Extensora", "muscle": "Quadríceps", "equipment": "Máquina", "difficulty": "Iniciante"},
        {"name": "Mesa Flexora", "muscle": "Posterior", "equipment": "Máquina", "difficulty": "Iniciante"},
        {"name": "Stiff", "muscle": "Posterior/Glúteos", "equipment": "Barra", "difficulty": "Intermediário"},
        {"name": "Cadeira Adutora", "muscle": "Adutores", "equipment": "Máquina", "difficulty": "Iniciante"},
        {"name": "Cadeira Abdutora", "muscle": "Glúteos", "equipment": "Máquina", "difficulty": "Iniciante"},
        {"name": "Panturrilha", "muscle": "Panturrilha", "equipment": "Máquina", "difficulty": "Iniciante"},
        {"name": "Avanço", "muscle": "Pernas", "equipment": "Halteres", "difficulty": "Intermediário"},
        
        # Core
        {"name": "Prancha", "muscle": "Abdômen", "equipment": "Peso Corporal", "difficulty": "Iniciante"},
        {"name": "Crunch", "muscle": "Abdômen", "equipment": "Peso Corporal", "difficulty": "Iniciante"},
        {"name": "Elevação de Pernas", "muscle": "Abdômen Inferior", "equipment": "Peso Corporal", "difficulty": "Iniciante"},
        {"name": "Russian Twist", "muscle": "Oblíquos", "equipment": "Halter/Medicine", "difficulty": "Intermediário"},
        
        # Cardio
        {"name": "Corrida", "muscle": "Cardio", "equipment": "Esteira", "difficulty": "Iniciante"},
        {"name": "Bicicleta", "muscle": "Cardio", "equipment": "Bike", "difficulty": "Iniciante"},
        {"name": "Elíptico", "muscle": "Cardio", "equipment": "Elíptico", "difficulty": "Iniciante"},
        {"name": "Burpee", "muscle": "Full Body", "equipment": "Peso Corporal", "difficulty": "Avançado"},
        {"name": "Jump Rope", "muscle": "Cardio", "equipment": "Corda", "difficulty": "Intermediário"}
    ]
    return pd.DataFrame(exercises)

def get_default_foods() -> pd.DataFrame:
    """Retorna DataFrame com alimentos padrão"""
    foods = [
        # Proteínas
        {"name": "Peito de Frango", "category": "Proteína", "calories": 165, "protein": 31, "carbs": 0, "fat": 3.6, "portion": "100g"},
        {"name": "Carne Moída Magra", "category": "Proteína", "calories": 250, "protein": 26, "carbs": 0, "fat": 15, "portion": "100g"},
        {"name": "Salmão", "category": "Proteína", "calories": 208, "protein": 20, "carbs": 0, "fat": 13, "portion": "100g"},
        {"name": "Atum", "category": "Proteína", "calories": 132, "protein": 28, "carbs": 0, "fat": 1, "portion": "100g"},
        {"name": "Ovos", "category": "Proteína", "calories": 155, "protein": 13, "carbs": 1.1, "fat": 11, "portion": "2 unidades"},
        {"name": "Claras de Ovo", "category": "Proteína", "calories": 52, "protein": 11, "carbs": 0.7, "fat": 0.2, "portion": "100g"},
        {"name": "Whey Protein", "category": "Proteína", "calories": 120, "protein": 24, "carbs": 3, "fat": 1, "portion": "30g"},
        {"name": "Peito de Peru", "category": "Proteína", "calories": 135, "protein": 30, "carbs": 0, "fat": 1, "portion": "100g"},
        {"name": "Cottage", "category": "Proteína", "calories": 98, "protein": 11, "carbs": 3.4, "fat": 4.3, "portion": "100g"},
        {"name": "Iogurte Grego", "category": "Proteína", "calories": 97, "protein": 9, "carbs": 3.6, "fat": 5, "portion": "100g"},
        
        # Carboidratos
        {"name": "Arroz Branco", "category": "Carboidrato", "calories": 130, "protein": 2.7, "carbs": 28, "fat": 0.3, "portion": "100g cozido"},
        {"name": "Arroz Integral", "category": "Carboidrato", "calories": 111, "protein": 2.6, "carbs": 23, "fat": 0.9, "portion": "100g cozido"},
        {"name": "Batata Doce", "category": "Carboidrato", "calories": 86, "protein": 1.6, "carbs": 20, "fat": 0.1, "portion": "100g"},
        {"name": "Aveia", "category": "Carboidrato", "calories": 389, "protein": 16.9, "carbs": 66, "fat": 6.9, "portion": "100g"},
        {"name": "Pão Integral", "category": "Carboidrato", "calories": 247, "protein": 13, "carbs": 41, "fat": 3.4, "portion": "100g"},
        {"name": "Macarrão Integral", "category": "Carboidrato", "calories": 124, "protein": 5, "carbs": 25, "fat": 1, "portion": "100g cozido"},
        {"name": "Quinoa", "category": "Carboidrato", "calories": 120, "protein": 4.4, "carbs": 21, "fat": 1.9, "portion": "100g cozida"},
        {"name": "Mandioca", "category": "Carboidrato", "calories": 160, "protein": 1.4, "carbs": 38, "fat": 0.3, "portion": "100g cozida"},
        
        # Vegetais
        {"name": "Brócolis", "category": "Vegetal", "calories": 34, "protein": 2.8, "carbs": 7, "fat": 0.4, "portion": "100g"},
        {"name": "Couve-Flor", "category": "Vegetal", "calories": 25, "protein": 1.9, "carbs": 5, "fat": 0.3, "portion": "100g"},
        {"name": "Espinafre", "category": "Vegetal", "calories": 23, "protein": 2.9, "carbs": 3.6, "fat": 0.4, "portion": "100g"},
        {"name": "Alface", "category": "Vegetal", "calories": 15, "protein": 1.4, "carbs": 2.9, "fat": 0.2, "portion": "100g"},
        {"name": "Tomate", "category": "Vegetal", "calories": 18, "protein": 0.9, "carbs": 3.9, "fat": 0.2, "portion": "100g"},
        {"name": "Cenoura", "category": "Vegetal", "calories": 41, "protein": 0.9, "carbs": 9.6, "fat": 0.2, "portion": "100g"},
        {"name": "Pimentão", "category": "Vegetal", "calories": 31, "protein": 1, "carbs": 6, "fat": 0.3, "portion": "100g"},
        {"name": "Abobrinha", "category": "Vegetal", "calories": 17, "protein": 1.2, "carbs": 3.1, "fat": 0.3, "portion": "100g"},
        
        # Frutas
        {"name": "Banana", "category": "Fruta", "calories": 89, "protein": 1.1, "carbs": 22.8, "fat": 0.3, "portion": "1 unidade média"},
        {"name": "Maçã", "category": "Fruta", "calories": 52, "protein": 0.3, "carbs": 14, "fat": 0.2, "portion": "1 unidade média"},
        {"name": "Morango", "category": "Fruta", "calories": 32, "protein": 0.7, "carbs": 7.7, "fat": 0.3, "portion": "100g"},
        {"name": "Mirtilo", "category": "Fruta", "calories": 57, "protein": 0.7, "carbs": 14, "fat": 0.3, "portion": "100g"},
        {"name": "Laranja", "category": "Fruta", "calories": 47, "protein": 0.9, "carbs": 12, "fat": 0.1, "portion": "1 unidade média"},
        {"name": "Abacate", "category": "Fruta", "calories": 160, "protein": 2, "carbs": 8.5, "fat": 14.7, "portion": "100g"},
        {"name": "Mamão", "category": "Fruta", "calories": 43, "protein": 0.5, "carbs": 11, "fat": 0.3, "portion": "100g"},
        {"name": "Melancia", "category": "Fruta", "calories": 30, "protein": 0.6, "carbs": 7.6, "fat": 0.2, "portion": "100g"},
        
        # Gorduras Saudáveis
        {"name": "Azeite de Oliva", "category": "Gordura", "calories": 884, "protein": 0, "carbs": 0, "fat": 100, "portion": "1 colher (15ml)"},
        {"name": "Castanhas", "category": "Gordura", "calories": 607, "protein": 20, "carbs": 21, "fat": 54, "portion": "100g"},
        {"name": "Amêndoas", "category": "Gordura", "calories": 579, "protein": 21, "carbs": 22, "fat": 50, "portion": "100g"},
        {"name": "Abacate", "category": "Gordura", "calories": 160, "protein": 2, "carbs": 8.5, "fat": 14.7, "portion": "100g"},
        {"name": "Pasta de Amendoim", "category": "Gordura", "calories": 588, "protein": 25, "carbs": 20, "fat": 50, "portion": "100g"},
        
        # Laticínios
        {"name": "Leite Desnatado", "category": "Laticínio", "calories": 34, "protein": 3.4, "carbs": 5, "fat": 0.1, "portion": "100ml"},
        {"name": "Leite Integral", "category": "Laticínio", "calories": 61, "protein": 3.2, "carbs": 4.8, "fat": 3.3, "portion": "100ml"},
        {"name": "Queijo Cottage", "category": "Laticínio", "calories": 98, "protein": 11, "carbs": 3.4, "fat": 4.3, "portion": "100g"},
        {"name": "Iogurte Natural", "category": "Laticínio", "calories": 61, "protein": 3.5, "carbs": 4.7, "fat": 3.3, "portion": "100g"}
    ]
    return pd.DataFrame(foods)

def initialize_data():
    """Inicializa arquivos de dados se não existirem"""
    exercises = get_default_exercises()
    save_csv(exercises, "exercises.csv")
    
    foods = get_default_foods()
    save_csv(foods, "foods.csv")
    
    # Inicializa user_data.json se não existir
    user_data = load_json("user_data.json")
    if not user_data:
        save_json({
            "profile": {},
            "workouts": [],
            "meals": [],
            "progress": []
        }, "user_data.json")
  

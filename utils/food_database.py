# utils/food_database.py

# Dicionário de alimentos: cada alimento tem (calorias, proteína, carboidrato, gordura) por 100g
FOODS = {
    "frango_grelhado": {"name": "Frango grelhado", "cal": 165, "prot": 31, "carb": 0, "fat": 3.6},
    "peixe_grelhado": {"name": "Peixe grelhado", "cal": 150, "prot": 25, "carb": 0, "fat": 5},
    "ovo": {"name": "Ovo", "cal": 155, "prot": 13, "carb": 1.1, "fat": 11},
    "arroz_integral": {"name": "Arroz integral cozido", "cal": 124, "prot": 2.6, "carb": 25.8, "fat": 1},
    "batata_doce": {"name": "Batata doce cozida", "cal": 86, "prot": 1.6, "carb": 20.1, "fat": 0.1},
    "brócolis": {"name": "Brócolis cozido", "cal": 35, "prot": 2.4, "carb": 5, "fat": 0.4},
    "azeite": {"name": "Azeite de oliva", "cal": 884, "prot": 0, "carb": 0, "fat": 100},
    "castanhas": {"name": "Castanhas", "cal": 607, "prot": 15, "carb": 18, "fat": 54},
    "iogurte_grego": {"name": "Iogurte grego", "cal": 120, "prot": 10, "carb": 4, "fat": 7},  # por 100g
    "whey": {"name": "Whey protein", "cal": 400, "prot": 80, "carb": 6, "fat": 5},  # por 100g
    "aveia": {"name": "Aveia", "cal": 389, "prot": 16.9, "carb": 66.3, "fat": 6.9},
    "pão_integral": {"name": "Pão integral", "cal": 265, "prot": 10, "carb": 45, "fat": 3.5},  # por 100g
    "banana": {"name": "Banana", "cal": 89, "prot": 1.1, "carb": 22.8, "fat": 0.3},
    "maçã": {"name": "Maçã", "cal": 52, "prot": 0.3, "carb": 14, "fat": 0.2},
    "leite": {"name": "Leite desnatado", "cal": 35, "prot": 3.4, "carb": 5, "fat": 0.1},  # por 100ml
}
# utils/food_database.py

# Lista de alimentos com seus macros por 100g
FOODS = [
    {"name": "Frango grelhado", "cal": 165, "prot": 31, "carb": 0, "fat": 3.6},
    {"name": "Peixe grelhado", "cal": 150, "prot": 25, "carb": 0, "fat": 5},
    {"name": "Ovo", "cal": 155, "prot": 13, "carb": 1.1, "fat": 11},
    {"name": "Arroz integral cozido", "cal": 124, "prot": 2.6, "carb": 25.8, "fat": 1},
    {"name": "Batata doce cozida", "cal": 86, "prot": 1.6, "carb": 20.1, "fat": 0.1},
    {"name": "Brócolis cozido", "cal": 35, "prot": 2.4, "carb": 5, "fat": 0.4},
    {"name": "Azeite de oliva", "cal": 884, "prot": 0, "carb": 0, "fat": 100},
    {"name": "Castanhas", "cal": 607, "prot": 15, "carb": 18, "fat": 54},
    {"name": "Iogurte grego", "cal": 120, "prot": 10, "carb": 4, "fat": 7},
    {"name": "Whey protein", "cal": 400, "prot": 80, "carb": 6, "fat": 5},
    {"name": "Aveia", "cal": 389, "prot": 16.9, "carb": 66.3, "fat": 6.9},
    {"name": "Pão integral", "cal": 265, "prot": 10, "carb": 45, "fat": 3.5},
    {"name": "Banana", "cal": 89, "prot": 1.1, "carb": 22.8, "fat": 0.3},
    {"name": "Maçã", "cal": 52, "prot": 0.3, "carb": 14, "fat": 0.2},
    {"name": "Leite desnatado", "cal": 35, "prot": 3.4, "carb": 5, "fat": 0.1},
]

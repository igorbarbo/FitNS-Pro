"""
Validação de inputs do usuário
"""
import re

def validate_height(height_str: str) -> tuple[bool, float, str]:
    """Valida altura em cm"""
    try:
        height = float(height_str)
        if 100 <= height <= 250:
            return True, height, ""
        return False, 0, "Altura deve estar entre 100cm e 250cm"
    except ValueError:
        return False, 0, "Altura inválida"

def validate_weight(weight_str: str) -> tuple[bool, float, str]:
    """Valida peso em kg"""
    try:
        weight = float(weight_str)
        if 30 <= weight <= 300:
            return True, weight, ""
        return False, 0, "Peso deve estar entre 30kg e 300kg"
    except ValueError:
        return False, 0, "Peso inválido"

def validate_age(age_str: str) -> tuple[bool, int, str]:
    """Valida idade"""
    try:
        age = int(age_str)
        if 10 <= age <= 120:
            return True, age, ""
        return False, 0, "Idade deve estar entre 10 e 120 anos"
    except ValueError:
        return False, 0, "Idade inválida"

def validate_positive_number(value_str: str, field_name: str) -> tuple[bool, float, str]:
    """Valida número positivo"""
    try:
        value = float(value_str)
        if value > 0:
            return True, value, ""
        return False, 0, f"{field_name} deve ser maior que zero"
    except ValueError:
        return False, 0, f"{field_name} inválido"
      

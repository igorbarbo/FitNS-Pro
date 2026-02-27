def tdee(weight, height, age, gender="male", activity_level=1.2):
    # Mifflin-St Jeor
    if gender=="male":
        bmr = 10*weight + 6.25*height - 5*age + 5
    else:
        bmr = 10*weight + 6.25*height - 5*age - 161
    return bmr * activity_level

def macros(weight, goal="maintain"):
    protein = weight * 2
    fat = weight * 0.8
    calories = weight * 24
    if goal=="lose":
        calories -= 300
    elif goal=="gain":
        calories += 300
    carbs = (calories - (protein*4 + fat*9)) / 4
    return {"calories": calories, "protein": protein, "carbs": carbs, "fat": fat}

def strength_balance(push, pull, lower, upper):
    return {
        "push_pull_ratio": push/pull if pull!=0 else 0,
        "lower_upper_ratio": lower/upper if upper!=0 else 0
    }

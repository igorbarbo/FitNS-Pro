# utils/models.py
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional
from config import Config

@dataclass
class User:
    id: str
    name: str
    email: str
    plan: str
    avatar: str = "👤"
    created_at: str = None
    
    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()

@dataclass
class Meal:
    id: str
    name: str
    quantity: str
    calories: int
    protein: float
    carbs: float
    fat: float
    timestamp: str
    meal_type: str

@dataclass
class DailyStats:
    date: str
    calories_consumed: int = 0
    calories_goal: int = Config.DEFAULT_CALORIES_GOAL
    protein_consumed: float = 0
    protein_goal: float = Config.DEFAULT_PROTEIN_GOAL
    carbs_consumed: float = 0
    fat_consumed: float = 0
    water_consumed: float = 0
    water_goal: float = Config.DEFAULT_WATER_GOAL
    workouts_completed: int = 0
    workouts_goal: int = 5

@dataclass
class UserProfile:
    user_id: str
    weight: float          # kg
    height: float          # cm
    age: int
    gender: str            # "male" ou "female"
    activity_level: str    # "sedentary", "light", "moderate", "active", "very_active"
    goal: str              # "lose", "maintain", "gain"
    target_weight: float   # kg desejado
    updated_at: str = None

    def __post_init__(self):
        if not self.updated_at:
            self.updated_at = datetime.now().isoformat()

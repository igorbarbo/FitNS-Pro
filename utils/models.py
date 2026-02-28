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
    water_consumed: float = 0
    water_goal: float = Config.DEFAULT_WATER_GOAL
    workouts_completed: int = 0
    workouts_goal: int = 5

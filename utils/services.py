# utils/services.py
from datetime import datetime
from typing import Dict, List, Optional
import hashlib
from .models import User, Meal
from .data_store import DataStore
from config import Config

class FitnessService:
    def __init__(self):
        self.store = DataStore()
    
    def authenticate(self, email: str, password: str) -> Optional[User]:
        # Gera um ID simples baseado no email
        user_id = hashlib.md5(email.encode()).hexdigest()[:8]
        user = User(
            id=user_id,
            name=email.split('@')[0].title(),
            email=email,
            plan="Premium"
        )
        self.store.set_current_user(user)
        return user
    
    def get_dashboard_data(self, user_id: str) -> Dict:
        stats = self.store.get_today_stats(user_id)
        meals = self.store.get_today_meals(user_id)
        weight_history = self.store.get_weight_history(user_id)
        
        weekly_data = self._generate_weekly_data(weight_history)
        
        return {
            "stats": stats,
            "meals": meals,
            "weekly_progress": weekly_data,
            "remaining_calories": stats.calories_goal - stats.calories_consumed,
            "remaining_protein": stats.protein_goal - stats.protein_consumed
        }
    
    def _generate_weekly_data(self, history: List[Dict]) -> List[float]:
        # Gera dados simulados de peso para a semana
        if len(history) >= 7:
            return [h["weight"] for h in history[-7:]]
        base_weight = 78.5
        return [base_weight - 3.5 + (i * 0.5) + (i * 0.2) for i in range(7)]

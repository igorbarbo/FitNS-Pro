# utils/data_store.py
import os
import json
from datetime import datetime
from typing import List, Dict, Optional
from .models import User, Meal, DailyStats, asdict
from config import Config

class DataStore:
    def __init__(self):
        self.file_path = Config.DATA_FILE
        self._ensure_data_file()
    
    def _ensure_data_file(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            initial_data = {
                "users": {},
                "current_user": None,
                "meals": {},
                "daily_stats": {},
                "weight_history": []
            }
            self._save_data(initial_data)
    
    def _load_data(self) -> Dict:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {"users": {}, "current_user": None, "meals": {}, "daily_stats": {}, "weight_history": []}
    
    def _save_data(self, data: Dict):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def get_current_user(self) -> Optional[User]:
        data = self._load_data()
        if data.get("current_user"):
            return User(**data["current_user"])
        return None
    
    def set_current_user(self, user: User):
        data = self._load_data()
        data["current_user"] = asdict(user)
        data["users"][user.id] = asdict(user)
        self._save_data(data)
    
    def logout(self):
        data = self._load_data()
        data["current_user"] = None
        self._save_data(data)
    
    def get_today_meals(self, user_id: str) -> List[Meal]:
        data = self._load_data()
        today = datetime.now().strftime("%Y-%m-%d")
        meals = data.get("meals", {}).get(user_id, [])
        return [Meal(**m) for m in meals if m["timestamp"].startswith(today)]
    
    def add_meal(self, user_id: str, meal: Meal):
        data = self._load_data()
        if user_id not in data["meals"]:
            data["meals"][user_id] = []
        data["meals"][user_id].append(asdict(meal))
        self._save_data(data)
        self._update_daily_stats(user_id)
    
    def delete_meal(self, user_id: str, meal_id: str):
        data = self._load_data()
        if user_id in data["meals"]:
            data["meals"][user_id] = [m for m in data["meals"][user_id] if m["id"] != meal_id]
            self._save_data(data)
            self._update_daily_stats(user_id)
    
    def get_today_stats(self, user_id: str) -> DailyStats:
        data = self._load_data()
        today = datetime.now().strftime("%Y-%m-%d")
        stats = data.get("daily_stats", {}).get(user_id, {}).get(today)
        if stats:
            return DailyStats(**stats)
        return DailyStats(date=today)
    
    def _update_daily_stats(self, user_id: str):
        data = self._load_data()
        today = datetime.now().strftime("%Y-%m-%d")
        meals = self.get_today_meals(user_id)
        
        total_calories = sum(m.calories for m in meals)
        total_protein = sum(m.protein for m in meals)
        total_carbs = sum(m.carbs for m in meals)
        total_fat = sum(m.fat for m in meals)
        
        if user_id not in data["daily_stats"]:
            data["daily_stats"][user_id] = {}
        
        # Preserva água e treinos já registrados
        current_stats = data["daily_stats"][user_id].get(today, {})
        data["daily_stats"][user_id][today] = {
            "date": today,
            "calories_consumed": total_calories,
            "calories_goal": Config.DEFAULT_CALORIES_GOAL,
            "protein_consumed": round(total_protein, 1),
            "protein_goal": Config.DEFAULT_PROTEIN_GOAL,
            "carbs_consumed": round(total_carbs, 1),
            "fat_consumed": round(total_fat, 1),
            "water_consumed": current_stats.get("water_consumed", 0),
            "water_goal": Config.DEFAULT_WATER_GOAL,
            "workouts_completed": current_stats.get("workouts_completed", 0),
            "workouts_goal": 5
        }
        self._save_data(data)
    
    def add_water(self, user_id: str, amount: float = 0.3):
        data = self._load_data()
        today = datetime.now().strftime("%Y-%m-%d")
        if user_id not in data["daily_stats"]:
            data["daily_stats"][user_id] = {}
        if today not in data["daily_stats"][user_id]:
            data["daily_stats"][user_id][today] = asdict(DailyStats(date=today))
        
        current = data["daily_stats"][user_id][today].get("water_consumed", 0)
        data["daily_stats"][user_id][today]["water_consumed"] = round(current + amount, 1)
        self._save_data(data)
    
    def get_weight_history(self, user_id: str) -> List[Dict]:
        data = self._load_data()
        return data.get("weight_history", [])
    
    def add_weight_entry(self, user_id: str, weight: float):
        data = self._load_data()
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "weight": weight,
            "timestamp": datetime.now().isoformat()
        }
        data["weight_history"].append(entry)
        self._save_data(data)

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
        data["meals"][user_id].append(asdict(meal

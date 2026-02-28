# modules/meal_item.py
import streamlit as st
from utils.models import Meal

def render_meal_item(meal: Meal, on_delete=None):
    emoji_map = {"breakfast": "🍳", "lunch": "🍽️", "dinner": "🌙", "snack": "🍎"}
    color_map = {"breakfast": "#ffb800", "lunch": "#00d4ff", "dinner": "#ff4b2b", "snack": "#10b981"}
    emoji = emoji_map.get(meal.meal_type, "🍽️")
    color = color_map.get(meal.meal_type, "#00d4ff")
    cols = st.columns([0.8, 3, 0.5])
    with cols[0]:
        st.markdown(f"<div style='font-size: 24px; text-align: center;'>{emoji}</div>", unsafe_allow_html=True)
    with cols[1]:
        st.markdown(f"""
        <div>
            <div style="font-size: 13px; font-weight: 700; margin-bottom: 2px;">{meal.name}</div>
            <div style="font-size: 10px; color: #8b8b9a;">{meal.quantity} • {meal.calories} kcal</div>
            <div style="font-size: 9px; color: {color}; margin-top: 4px;">
                P: {meal.protein:.1f}g • C: {meal.carbs:.1f}g • G: {meal.fat:.1f}g
            </div>
        </div>
        """, unsafe_allow_html=True)
    with cols[2]:
        if st.button("🗑️", key=f"del_{meal.id}", help="Remover"):
            if on_delete:
                on_delete(meal.id)

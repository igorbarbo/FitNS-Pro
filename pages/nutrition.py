# pages/nutrition.py
import streamlit as st
import time
from datetime import datetime
from modules.header import render_header
from modules.navigation import render_navigation
from modules.meal_item import render_meal_item
from utils.models import Meal

def delete_meal(meal_id: str):
    user = st.session_state.user
    st.session_state.service.store.delete_meal(user.id, meal_id)
    st.rerun()

def show():
    user = st.session_state.user
    service = st.session_state.service
    meals = service.store.get_today_meals(user.id)
    stats = service.store.get_today_stats(user.id)
    
    render_header(user)
    render_navigation()
    st.markdown('<div class="slide-in">', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <h2 style="margin:0; font-size: 24px;">🥗 Diário Alimentar</h2>
        <p style="color: #8b8b9a; font-size: 12px; margin-top: 5px;">Registre suas refeições</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Cards de resumo
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("Calorias", f"{stats.calories_consumed}", f"{stats.calories_goal - stats.calories_consumed} restantes")
    col2.metric("Proteína", f"{stats.protein_consumed}g", f"{stats.protein_goal - stats.protein_consumed}g restantes")
    col3.metric("Refeições", len(meals), "hoje")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Botão para adicionar refeição
    if st.button("+ Adicionar Refeição", use_container_width=True, key="btn_add_meal"):
        st.session_state.show_add_meal = True
    
    # Formulário de adição (controlado por session_state)
    if st.session_state.get('show_add_meal', False):
        with st.form("add_meal_form"):
            st.markdown("<h4 style='margin-bottom: 15px;'>Nova Refeição</h4>", unsafe_allow_html=True)
            cols = st.columns([2, 1])
            with cols[0]:
                name = st.text_input("Nome do alimento", placeholder="Ex: Frango Grelhado")
            with cols[1]:
                meal_type = st.selectbox("Refeição", ["breakfast", "lunch", "dinner", "snack"], 
                                        format_func=lambda x: {"breakfast": "Café", "lunch": "Almoço", "dinner": "Jantar", "snack": "Lanche"}[x])
            cols2 = st.columns(4)
            with cols2[0]:
                quantity = st.text_input("Quantidade", placeholder="200g")
            with cols2[1]:
                calories = st.number_input("Kcal", min_value=0, value=0, step=10)
            with cols2[2]:
                protein = st.number_input("Proteína (g)", min_value=0.0, value=0.0, step=0.1)
            with cols2[3]:
                carbs = st.number_input("Carbos (g)", min_value=0.0, value=0.0, step=0.1)
            fat = st.number_input("Gorduras (g)", min_value=0.0, value=0.0, step=0.1)
            cols3 = st.columns(2)
            with cols3[0]:
                if st.form_submit_button("Cancelar", use_container_width=True):
                    st.session_state.show_add_meal = False
                    st.rerun()
            with cols3[1]:
                if st.form_submit_button("Salvar", type="primary", use_container_width=True):
                    if name and calories > 0:
                        meal = Meal(
                            id=f"meal_{int(time.time())}",
                            name=name,
                            quantity=quantity or "1 porção",
                            calories=calories,
                            protein=protein,
                            carbs=carbs,
                            fat=fat,
                            timestamp=datetime.now().isoformat(),
                            meal_type=meal_type
                        )
                        service.store.add_meal(user.id, meal)
                        st.success("Refeição adicionada!")
                        st.session_state.show_add_meal = False
                        time.sleep(0.3)
                        st.rerun()
                    else:
                        st.error("Preencha nome e calorias!")
    
    # Lista de refeições do dia
    st.markdown("<h4 style='margin: 20px 0 15px 0;'>Refeições de Hoje</h4>", unsafe_allow_html=True)
    if not meals:
        st.info("Nenhuma refeição registrada hoje.")
    else:
        for meal in sorted(meals, key=lambda x: x.timestamp, reverse=True):
            render_meal_item(meal, on_delete=delete_meal)
    
    st.markdown('</div>', unsafe_allow_html=True)

"""
Módulo de Nutrição
"""
import streamlit as st
import pandas as pd
from datetime import datetime
from utils.data_manager import load_csv, load_json, save_json

def render_nutrition():
    """Renderiza o módulo de nutrição"""
    st.header("🥗 Módulo de Nutrição")
    st.markdown("---")
    
    # Carrega dados
    foods_df = load_csv("foods.csv")
    if foods_df.empty:
        from utils.data_manager import get_default_foods
        foods_df = get_default_foods()
        from utils.data_manager import save_csv
        save_csv(foods_df, "foods.csv")
    
    user_data = load_json("user_data.json")
    profile = user_data.get('profile', {})
    
    # Metas do usuário
    if profile:
        target_calories = profile.get('target_calories', 2000)
        macros = profile.get('macros', {'protein_g': 150, 'carbs_g': 200, 'fat_g': 67})
    else:
        target_calories = 2000
        macros = {'protein_g': 150, 'carbs_g': 200, 'fat_g': 67}
    
    # Calcula totais do dia
    today = str(datetime.now().date())
    if 'meals' not in user_data:
        user_data['meals'] = []
    
    today_meals = [m for m in user_data['meals'] if m['date'] == today]
    total_cal = sum(m['calories'] for m in today_meals)
    total_prot = sum(m['protein'] for m in today_meals)
    total_carbs = sum(m['carbs'] for m in today_meals)
    total_fat = sum(m['fat'] for m in today_meals)
    
    # Dashboard de macros
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Calorias", f"{total_cal}/{target_calories}", 
                 delta=f"{target_calories - total_cal} restantes")
    with col2:
        st.metric("Proteínas", f"{total_prot}g/{macros['protein_g']}g")
    with col3:
        st.metric("Carbs", f"{total_carbs}g/{macros['carbs_g']}g")
    with col4:
        st.metric("Gorduras", f"{total_fat}g/{macros['fat_g']}g")
    
    # Barras de progresso
    st.progress(min(total_cal / target_calories, 1.0), text=f"Calorias: {total_cal}/{target_calories}")
    
    tab1, tab2, tab3 = st.tabs(["🍽️ Diário", "📊 Alimentos", "💧 Água"])
    
    with tab1:
        st.subheader("Registrar Refeição")
        
        meal_type = st.selectbox("Refeição", ["Café da Manhã", "Almoço", "Jantar", "Lanche"])
        
        with st.form("meal_form"):
            food_search = st.text_input("Buscar alimento")
            filtered_foods = foods_df[foods_df['name'].str.contains(food_search, case=False, na=False)] if food_search else foods_df
            
            food = st.selectbox("Alimento", filtered_foods['name'].tolist())
            quantity = st.number_input("Quantidade (porções)", 0.1, 10.0, 1.0, 0.1)
            
            # Pega info do alimento selecionado
            food_info = foods_df[foods_df['name'] == food].iloc[0]
            
            st.write(f"**Porção:** {food_info['portion']}")
            st.write(f"**Calorias:** {food_info['calories'] * quantity:.0f} kcal")
            st.write(f"**P: {food_info['protein'] * quantity:.1f}g | C: {food_info['carbs'] * quantity:.1f}g | G: {food_info['fat'] * quantity:.1f}g**")
            
            if st.form_submit_button("Adicionar"):
                user_data['meals'].append({
                    'date': today,
                    'meal_type': meal_type,
                    'food': food,
                    'quantity': quantity,
                    'calories': food_info['calories'] * quantity,
                    'protein': food_info['protein'] * quantity,
                    'carbs': food_info['carbs'] * quantity,
                    'fat': food_info['fat'] * quantity
                })
                save_json(user_data, "user_data.json")
                st.success(f"{food} adicionado!")
                st.rerun()
        
        # Lista de refeições de hoje
        st.markdown("### Refeições de Hoje")
        if today_meals:
            for meal in today_meals:
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.write(f"**{meal['meal_type']}:** {meal['food']} ({meal['quantity']}x)")
                with col2:
                    st.write(f"{meal['calories']:.0f} kcal")
                with col3:
                    st.write(f"P:{meal['protein']:.0f} C:{meal['carbs']:.0f} G:{meal['fat']:.0f}")
        else:
            st.info("Nenhuma refeição registrada hoje")
    
    with tab2:
        st.subheader("Base de Dados de Alimentos")
        category = st.multiselect("Categoria", foods_df['category'].unique())
        
        if category:
            st.dataframe(foods_df[foods_df['category'].isin(category)], use_container_width=True)
        else:
            st.dataframe(foods_df, use_container_width=True)
    
    with tab3:
        st.subheader("Controle de Água")
        
        if 'water' not in user_data:
            user_data['water'] = []
        
        today_water = sum(w['amount'] for w in user_data['water'] if w['date'] == today)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Água Hoje", f"{today_water}ml", "Meta: 3000ml")
        with col2:
            add_water = st.number_input("Adicionar (ml)", 100, 1000, 250, 50)
            if st.button("💧 Registrar"):
                user_data['water'].append({'date': today, 'amount': add_water})
                save_json(user_data, "user_data.json")
                st.success(f"+{add_water}ml")
                st.rerun()
        
        st.progress(min(today_water / 3000, 1.0))
      

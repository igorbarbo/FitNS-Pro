"""
Módulo de Treinos
"""
import streamlit as st
import pandas as pd
from datetime import datetime
from utils.data_manager import load_csv, save_csv, load_json, save_json

def render_workout():
    """Renderiza o módulo de treinos"""
    st.header("💪 Módulo de Treino")
    st.markdown("---")
    
    # Carrega dados
    exercises_df = load_csv("exercises.csv")
    if exercises_df.empty:
        from utils.data_manager import get_default_exercises
        exercises_df = get_default_exercises()
        save_csv(exercises_df, "exercises.csv")
    
    user_data = load_json("user_data.json")
    
    tab1, tab2, tab3 = st.tabs(["🎯 Meu Treino", "📚 Biblioteca", "➕ Registrar"])
    
    with tab1:
        st.subheader("Seu Plano de Treino")
        
        if 'profile' not in user_data or not user_data['profile']:
            st.warning("Configure sua meta na Balança primeiro!")
        else:
            goal = user_data['profile'].get('goal', 'manter_peso')
            
            # Gera plano baseado no objetivo
            if goal == 'perder_gordura':
                plan = {
                    "Segunda": ["Supino Reto", "Agachamento", "Puxada Frontal", "Prancha"],
                    "Terça": ["Corrida", "Burpee", "Jump Rope"],
                    "Quarta": ["Desenvolvimento", "Leg Press", "Remada Curvada", "Crunch"],
                    "Quinta": ["Bicicleta", "Elíptico", "Burpee"],
                    "Sexta": ["Supino Inclinado", "Stiff", "Elevação Lateral", "Panturrilha"],
                    "Sábado": ["Cardio LISS", "Prancha", "Russian Twist"]
                }
            elif goal == 'ganhar_musculo':
                plan = {
                    "Segunda": ["Supino Reto", "Desenvolvimento", "Tríceps Corda", "Crucifixo"],
                    "Terça": ["Agachamento", "Leg Press", "Stiff", "Panturrilha"],
                    "Quarta": ["Puxada Frontal", "Remada Curvada", "Rosca Direta", "Barra Fixa"],
                    "Quinta": ["Supino Inclinado", "Elevação Lateral", "Tríceps Testa", "Francês"],
                    "Sexta": ["Levantamento Terra", "Cadeira Extensora", "Mesa Flexora", "Prancha"],
                    "Sábado": ["Cardio leve", "Core completo"]
                }
            else:  # manter
                plan = {
                    "Segunda": ["Supino Reto", "Agachamento", "Puxada Frontal"],
                    "Terça": ["Corrida", "Prancha"],
                    "Quarta": ["Desenvolvimento", "Leg Press", "Remada Unilateral"],
                    "Quinta": ["Bicicleta", "Abdominais"],
                    "Sexta": ["Peito completo", "Costas completas"]
                }
            
            selected_day = st.selectbox("Dia da semana", list(plan.keys()))
            st.markdown(f"**Treino de {selected_day}:**")
            
            for exercise in plan[selected_day]:
                col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
                with col1:
                    st.write(f"🏋️ {exercise}")
                with col2:
                    sets = st.number_input(f"Séries {exercise}", 1, 10, 3, key=f"sets_{exercise}")
                with col3:
                    reps = st.number_input(f"Reps {exercise}", 1, 50, 10, key=f"reps_{exercise}")
                with col4:
                    weight = st.number_input(f"Carga(kg) {exercise}", 0.0, 500.0, 20.0, key=f"weight_{exercise}")
    
    with tab2:
        st.subheader("Biblioteca de Exercícios")
        
        # Filtros
        col1, col2 = st.columns(2)
        with col1:
            muscle_filter = st.multiselect("Grupo Muscular", exercises_df['muscle'].unique())
        with col2:
            equip_filter = st.multiselect("Equipamento", exercises_df['equipment'].unique())
        
        filtered = exercises_df
        if muscle_filter:
            filtered = filtered[filtered['muscle'].isin(muscle_filter)]
        if equip_filter:
            filtered = filtered[filtered['equipment'].isin(equip_filter)]
        
        st.dataframe(filtered, use_container_width=True, hide_index=True)
    
    with tab3:
        st.subheader("Registrar Treino Realizado")
        
        with st.form("workout_log"):
            date = st.date_input("Data", datetime.now())
            exercise = st.selectbox("Exercício", exercises_df['name'].tolist())
            sets = st.number_input("Séries", 1, 20, 3)
            reps = st.number_input("Repetições", 1, 100, 10)
            weight = st.number_input("Carga (kg)", 0.0, 500.0, 20.0)
            notes = st.text_area("Observações")
            
            if st.form_submit_button("Salvar Treino"):
                if 'workouts' not in user_data:
                    user_data['workouts'] = []
                
                user_data['workouts'].append({
                    'date': str(date),
                    'exercise': exercise,
                    'sets': sets,
                    'reps': reps,
                    'weight': weight,
                    'notes': notes,
                    'volume': sets * reps * weight
                })
                save_json(user_data, "user_data.json")
                st.success("Treino registrado!")
        
        # Histórico recente
        if 'workouts' in user_data and user_data['workouts']:
            st.markdown("### Últimos Treinos")
            recent = pd.DataFrame(user_data['workouts'][-10:])
            st.dataframe(recent, use_container_width=True)
          

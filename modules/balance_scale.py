"""
Módulo Balança / Meta Física
"""
import streamlit as st
from utils.calculations import calculate_bmi, calculate_tdee, calculate_macros, calculate_goal_timeline, get_workout_recommendation
from utils.data_manager import load_json, save_json

def render_balance_scale():
    """Renderiza o módulo de balança e metas"""
    st.header("⚖️ Balança & Meta Física")
    st.markdown("---")
    
    # Verifica se já tem perfil
    user_data = load_json("user_data.json")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📊 Seus Dados")
        
        with st.form("balance_form"):
            height = st.number_input("Altura (cm)", min_value=100, max_value=250, value=170)
            current_weight = st.number_input("Peso Atual (kg)", min_value=30.0, max_value=300.0, value=70.0, step=0.1)
            age = st.number_input("Idade", min_value=10, max_value=120, value=25)
            gender = st.selectbox("Gênero", ["Masculino", "Feminino"])
            activity = st.selectbox("Nível de Atividade", [
                "sedentario", "leve", "moderado", "ativo", "muito_ativo"
            ], format_func=lambda x: {
                "sedentario": "Sedentário (pouco ou nenhum exercício)",
                "leve": "Leve (1-3 dias/semana)",
                "moderado": "Moderado (3-5 dias/semana)",
                "ativo": "Ativo (6-7 dias/semana)",
                "muito_ativo": "Muito Ativo (2x por dia, físico intenso)"
            }[x])
            
            st.markdown("---")
            st.subheader("🎯 Sua Meta")
            
            goal = st.selectbox("Objetivo Principal", [
                "perder_gordura", "ganhar_musculo", "manter_peso"
            ], format_func=lambda x: {
                "perder_gordura": "🔥 Perder Gordura",
                "ganhar_musculo": "💪 Ganhar Músculo",
                "manter_peso": "⚖️ Manter Peso"
            }[x])
            
            target_weight = st.number_input("Peso Desejado (kg)", min_value=30.0, max_value=300.0, value=current_weight, step=0.1)
            timeline_weeks = st.slider("Prazo Desejado (semanas)", 4, 52, 12)
            
            submitted = st.form_submit_button("Calcular Plano", use_container_width=True)
    
    with col2:
        if submitted:
            # Cálculos
            bmi_data = calculate_bmi(current_weight, height)
            tdee_data = calculate_tdee(current_weight, height, age, gender, activity)
            
            # Ajusta calorias pelo objetivo
            goal_adjustments = {
                "perder_gordura": -500,
                "ganhar_musculo": 300,
                "manter_peso": 0
            }
            target_calories = tdee_data['tdee'] + goal_adjustments[goal]
            macros = calculate_macros(target_calories, goal)
            timeline = calculate_goal_timeline(current_weight, target_weight, goal)
            workout_rec = get_workout_recommendation(goal, "intermediario")
            
            # Salva perfil
            profile = {
                "height": height,
                "current_weight": current_weight,
                "age": age,
                "gender": gender,
                "activity": activity,
                "goal": goal,
                "target_weight": target_weight,
                "timeline_weeks": timeline_weeks,
                "bmi": bmi_data,
                "tdee": tdee_data,
                "target_calories": target_calories,
                "macros": macros,
                "timeline": timeline
            }
            user_data['profile'] = profile
            save_json(user_data, "user_data.json")
            
            # Display resultados
            st.success("✅ Plano calculado com sucesso!")
            
            st.markdown("### 📈 Indicadores Atuais")
            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric("IMC", f"{bmi_data['bmi']}", bmi_data['category'])
            with m2:
                st.metric("Peso Ideal", bmi_data['ideal_range'])
            with m3:
                st.metric("Taxa Metabólica", f"{tdee_data['bmr']} kcal")
            
            st.markdown("### 🍽️ Meta Diária de Nutrição")
            n1, n2, n3, n4 = st.columns(4)
            with n1:
                st.metric("Calorias", f"{target_calories} kcal")
            with n2:
                st.metric("Proteínas", f"{macros['protein_g']}g ({macros['protein_pct']}%)")
            with n3:
                st.metric("Carboidratos", f"{macros['carbs_g']}g ({macros['carbs_pct']}%)")
            with n4:
                st.metric("Gorduras", f"{macros['fat_g']}g ({macros['fat_pct']}%)")
            
            st.markdown("### ⏱️ Previsão de Resultados")
            st.info(f"**{timeline['message']}**  \nTaxa recomendada: {timeline['rate']}")
            
            st.markdown("### 💪 Recomendação de Treino")
            st.write(f"**Foco:** {workout_rec['foco']}")
            st.write(f"**Frequência:** {workout_rec['frequencia']}")
            st.write(f"**Cardio:** {workout_rec['cardio']}")
            st.write(f"**Intensidade:** {workout_rec['intensidade']}")
            
            # Alerta se meta for irrealista
            weight_diff = abs(target_weight - current_weight)
            if goal == "perder_gordura" and weight_diff > timeline_weeks * 1.0:
                st.warning("⚠️ Meta agressiva! Considere aumentar o prazo para perda segura.")
            elif goal == "ganhar_musculo" and weight_diff > timeline_weeks * 0.5:
                st.warning("⚠️ Ganho muscular realista é de 0.25-0.5kg/semana. Considere ajustar.")
        else:
            st.info("👈 Preencha seus dados e clique em 'Calcular Plano' para ver suas recomendações personalizadas.")
          

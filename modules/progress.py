"""
Módulo de Progresso
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
from utils.data_manager import load_json

def render_progress():
    """Renderiza o módulo de progresso"""
    st.header("📈 Módulo de Progresso")
    st.markdown("---")
    
    user_data = load_json("user_data.json")
    profile = user_data.get('profile', {})
    workouts = user_data.get('workouts', [])
    meals = user_data.get('meals', [])
    
    if not profile:
        st.warning("Configure seu perfil na Balança primeiro!")
        return
    
    tab1, tab2, tab3 = st.tabs(["💪 Força", "⚖️ Peso", "📊 Análise"])
    
    with tab1:
        st.subheader("Evolução de Força")
        
        if workouts:
            df_workouts = pd.DataFrame(workouts)
            df_workouts['date'] = pd.to_datetime(df_workouts['date'])
            
            # Seleciona exercício
            exercises = df_workouts['exercise'].unique()
            selected = st.selectbox("Selecione o exercício", exercises)
            
            exercise_data = df_workouts[df_workouts['exercise'] == selected].sort_values('date')
            
            if not exercise_data.empty:
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=exercise_data['date'],
                    y=exercise_data['weight'],
                    mode='lines+markers',
                    name='Carga (kg)',
                    line=dict(color='#FF6B35', width=3)
                ))
                fig.add_trace(go.Bar(
                    x=exercise_data['date'],
                    y=exercise_data['volume'],
                    name='Volume Total',
                    marker_color='rgba(0, 78, 137, 0.6)',
                    yaxis='y2'
                ))
                
                fig.update_layout(
                    title=f"Progressão: {selected}",
                    xaxis_title="Data",
                    yaxis_title="Carga (kg)",
                    yaxis2=dict(title="Volume", overlaying='y', side='right'),
                    template='plotly_dark',
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # Stats
                if len(exercise_data) > 1:
                    first_weight = exercise_data.iloc[0]['weight']
                    last_weight = exercise_data.iloc[-1]['weight']
                    delta = last_weight - first_weight
                    st.metric("Progresso", f"{last_weight}kg", f"{delta:+.1f}kg desde início")
        else:
            st.info("Registre treinos para ver progresso")
    
    with tab2:
        st.subheader("Evolução de Peso")
        
        # Simula dados de peso se não tiver histórico real
        current_weight = profile.get('current_weight', 70)
        target_weight = profile.get('target_weight', 70)
        
        # Cria projeção
        weeks = profile.get('timeline_weeks', 12)
        dates = [datetime.now() + timedelta(weeks=w) for w in range(weeks + 1)]
        
        if profile.get('goal') == 'perder_gordura':
            weights = [current_weight - (current_weight - target_weight) * (w/weeks) for w in range(weeks + 1)]
        elif profile.get('goal') == 'ganhar_musculo':
            weights = [current_weight + (target_weight - current_weight) * (w/weeks) for w in range(weeks + 1)]
        else:
            weights = [current_weight] * (weeks + 1)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=dates,
            y=weights,
            mode='lines+markers',
            name='Projeção',
            line=dict(color='#1A936F', width=3, dash='dash')
        ))
        fig.add_hline(y=target_weight, line_dash="dot", line_color="#FF6B35", 
                     annotation_text="Meta")
        
        fig.update_layout(
            title="Projeção de Peso",
            xaxis_title="Data",
            yaxis_title="Peso (kg)",
            template='plotly_dark',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("💡 Dica: Pese-se sempre no mesmo horário (de preferência pela manhã em jejum)")
    
    with tab3:
        st.subheader("Análise de Composição")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Volume Semanal")
            if workouts:
                df = pd.DataFrame(workouts)
                df['date'] = pd.to_datetime(df['date'])
                df['week'] = df['date'].dt.isocalendar().week
                weekly = df.groupby('week')['volume'].sum().reset_index()
                st.bar_chart(weekly.set_index('week'))
        
        with col2:
            st.markdown("### Adesão à Dieta")
            if meals:
                df_meals = pd.DataFrame(meals)
                df_meals['date'] = pd.to_datetime(df_meals['date'])
                daily_cal = df_meals.groupby('date')['calories'].sum().reset_index()
                st.line_chart(daily_cal.set_index('date'))
              

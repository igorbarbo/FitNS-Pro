import streamlit as st
import pandas as pd

def show_progresso(get_data_path):
    # Lê o CSV usando a função segura
    df = pd.read_csv(get_data_path("workouts.csv"))
    
    st.write("### Últimos treinos")
    st.dataframe(df.head(20))

    # Exemplo: gráfico simples de evolução de peso
    st.line_chart(df[['Weight']])

import streamlit as st
import pandas as pd
import plotly.express as px

def show_progresso():
    st.title("📊 Progresso")
    df = pd.read_csv("data/workouts.csv")
    if df.empty:
        st.info("Nenhum treino registrado")
        return
    fig = px.line(df, x="Date", y="Load", color="Exercise")
    st.plotly_chart(fig, use_container_width=True)

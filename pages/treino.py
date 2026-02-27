import streamlit as st
import pandas as pd

def show_treino():
    st.title("💪 Treino")
    df = pd.read_csv("data/exercises_500.csv")
    goal = st.selectbox("Objetivo", df["Goal"].unique())
    level = st.selectbox("Nível", df["Level"].unique())
    filtered = df[(df["Goal"]==goal) & (df["Level"]==level)]
    st.dataframe(filtered.head(50))

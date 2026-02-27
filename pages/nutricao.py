import streamlit as st
import pandas as pd

def show_nutricao():
    st.title("🥗 Nutrição")
    df = pd.read_csv("data/foods_500.csv")
    food = st.selectbox("Escolher alimento", df["Food"].unique())
    quantity = st.number_input("Quantidade", 1)
    if st.button("Adicionar"):
        item = df[df["Food"]==food].iloc[0]
        calories = item["Calories"] * quantity
        st.success(f"{calories} kcal adicionadas")

import streamlit as st
import pandas as pd

def show_treino(get_data_path):
    df = pd.read_csv(get_data_path("exercises_500.csv"))
    
    st.write("### Biblioteca de exercícios")
    st.dataframe(df.head(20))

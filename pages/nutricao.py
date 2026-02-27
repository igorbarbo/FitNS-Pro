import streamlit as st
import pandas as pd

def show_nutricao(get_data_path):
    df = pd.read_csv(get_data_path("foods_500.csv"))
    
    st.write("### Alimentos disponíveis")
    st.dataframe(df.head(20))

import streamlit as st

def show_dashboard():
    st.title("🏋️ Dashboard")
    col1, col2, col3 = st.columns(3)
    col1.metric("🔥 Calorias Hoje", "1850 / 2200 kcal")
    col2.metric("💪 Treino Hoje", "Pernas 35 min")
    col3.metric("💧 Água", "2.5L")
    st.info("Bem-vindo ao FitNS Pro Premium!")

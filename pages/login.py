# pages/login.py
import streamlit as st
import time

def show():
    st.markdown("""
    <div style="text-align: center; padding: 60px 20px;">
        <div style="font-size: 64px; margin-bottom: 20px;">⚡</div>
        <h1 style="font-size: 32px; margin-bottom: 10px; font-weight: 800;">FitNS Pro</h1>
        <p style="color: #8b8b9a; margin-bottom: 40px; font-size: 14px;">Seu assistente fitness completo</p>
    </div>
    """, unsafe_allow_html=True)
    with st.form("login_form"):
        email = st.text_input("📧 Email", placeholder="seu@email.com")
        password = st.text_input("🔒 Senha", type="password", placeholder="••••••••")
        col1, col2 = st.columns(2)
        with col1:
            st.checkbox("Lembrar-me", value=True)
        with col2:
            st.markdown("<div style='text-align: right; font-size: 11px; color: #00d4ff;'>Esqueceu a senha?</div>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Entrar", use_container_width=True)
        if submitted:
            if email and password:
                user = st.session_state.service.authenticate(email, password)
                st.session_state.user = user
                st.success("Login realizado!")
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("Preencha todos os campos!")

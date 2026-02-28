# modules/navigation.py
import streamlit as st

def render_navigation():
    pages = [("dashboard", "🏠", "Início"), ("workout", "🏋️", "Treino"), 
             ("nutrition", "🥗", "Nutrição"), ("progress", "📈", "Progresso")]
    cols = st.columns(4)
    for i, (page_id, icon, label) in enumerate(pages):
        with cols[i]:
            is_active = st.session_state.page == page_id
            opacity = "1" if is_active else "0.4"
            color = "#00d4ff" if is_active else "#fff"
            border = "2px solid #00d4ff" if is_active else "2px solid transparent"
            if st.button(f"{icon} {label}", key=f"nav_{page_id}", use_container_width=True):
                st.session_state.page = page_id
                st.rerun()
            st.markdown(f"""
            <div style="text-align: center; margin-top: -10px; opacity: {opacity}; color: {color}; 
                        border-bottom: {border}; padding-bottom: 5px; transition: all 0.3s;">
                <div style="font-size: 20px;">{icon}</div>
                <div style="font-size: 9px; font-weight: 600; margin-top: 2px;">{label}</div>
            </div>
            """, unsafe_allow_html=True)

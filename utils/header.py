# modules/header.py
import streamlit as st
from utils.models import User

def render_header(user: User):
    col_logo, col_user = st.columns([1, 1])
    with col_logo:
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 8px;">
            <div style="font-size: 24px;">⚡</div>
            <div>
                <div style="font-size: 20px; font-weight: 800; letter-spacing: -0.5px;">
                    FitNS <span style="color: #00d4ff;">Pro</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_user:
        st.markdown(f"""
        <div style="display: flex; align-items: center; justify-content: flex-end; gap: 12px;">
            <div style="text-align: right;">
                <div style="font-weight: 700; font-size: 14px;">{user.name}</div>
                <div style="font-size: 11px; color: #10b981; font-weight: 600;">Plano {user.plan}</div>
            </div>
            <div style="width: 42px; height: 42px; background: linear-gradient(135deg, #1a1b26, #2d2f3f); 
                        border: 2px solid #00d4ff; border-radius: 50%; display: flex; align-items: center; 
                        justify-content: center; font-size: 18px; box-shadow: 0 0 15px rgba(0,212,255,0.3);">
                {user.avatar}
            </div>
        </div>
        """, unsafe_allow_html=True)

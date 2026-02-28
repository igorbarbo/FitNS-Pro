# modules/progress_bars.py
import streamlit as st

def render_progress_bar(label: str, current: float, goal: float, color: str, unit: str = ""):
    percentage = min((current / goal) * 100, 100) if goal > 0 else 0
    remaining = max(goal - current, 0)
    st.markdown(f"""
    <div style="margin-bottom: 16px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span style="font-size: 12px; font-weight: 600; color: #8b8b9a;">{label}</span>
            <span style="font-size: 13px; font-weight: 700;">
                {current:.1f}{unit} <span style="opacity: 0.5; font-size: 11px;">/ {goal}{unit}</span>
            </span>
        </div>
        <div class="progress-bg">
            <div class="progress-fill" style="width: {percentage}%; background: {color};"></div>
        </div>
        <div style="text-align: right; font-size: 10px; color: #8b8b9a; margin-top: 4px;">
            Faltam {remaining:.1f}{unit}
        </div>
    </div>
    """, unsafe_allow_html=True)

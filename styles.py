# styles.py
import streamlit as st

def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
        * { font-family: 'Inter', sans-serif; }
        .stApp { background-color: #08090f; color: #fff; }
        .block-container { padding-top: 1rem; padding-bottom: 5rem; max-width: 480px; margin: 0 auto; }
        header { visibility: hidden; }
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 20px;
            margin-bottom: 15px;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .glass-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 212, 255, 0.1);
        }
        .btn-neon {
            background: linear-gradient(135deg, #10b981, #059669);
            color: white !important;
            border: none;
            padding: 14px;
            border-radius: 14px;
            font-weight: 800;
            width: 100%;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
            display: block;
            box-shadow: 0 4px 20px rgba(16, 185, 129, 0.3);
            transition: all 0.3s;
            font-size: 14px;
            border: 1px solid rgba(255,255,255,0.1);
        }
        .btn-neon:hover { transform: scale(1.02); box-shadow: 0 6px 30px rgba(16, 185, 129, 0.4); }
        .btn-primary { background: linear-gradient(135deg, #00d4ff, #0099cc); box-shadow: 0 4px 20px rgba(0, 212, 255, 0.3); }
        .btn-primary:hover { box-shadow: 0 6px 30px rgba(0, 212, 255, 0.4); }
        .progress-bg { height: 8px; background: rgba(255,255,255,0.1); border-radius: 10px; overflow: hidden; margin-top: 8px; }
        .progress-fill { height: 100%; border-radius: 10px; transition: width 0.5s ease; box-shadow: 0 0 10px currentColor; }
        @keyframes slideIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        .slide-in { animation: slideIn 0.4s ease-out; }
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: #08090f; }
        ::-webkit-scrollbar-thumb { background: #00d4ff; border-radius: 3px; }
        .stButton > button { background: transparent; border: none; padding: 0; margin: 0; width: 100%; }
        .stButton > button:hover { background: transparent; border: none; }
        .stTextInput > div > div > input, .stNumberInput > div > div > input {
            background: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 12px !important;
            color: white !important;
            padding: 12px !important;
        }
        .st-b7 { color: white; }
        .st-c0 { background-color: #08090f; }
    </style>
    """, unsafe_allow_html=True)

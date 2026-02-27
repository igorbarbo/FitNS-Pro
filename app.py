"""
FitNS Pro - Aplicativo Completo de Fitness
"""
import streamlit as st
from modules.dashboard import render_dashboard
from modules.balance_scale import render_balance_scale
from modules.workout import render_workout
from modules.nutrition import render_nutrition
from modules.progress import render_progress

# Configuração da página
st.set_page_config(
    page_title="FitNS Pro",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Customizado
st.markdown("""
<style>
    .stMetric {
        background-color: #1E1E1E;
        padding: 10px;
        border-radius: 10px;
        border-left: 3px solid #FF6B35;
    }
    .stButton>button {
        background-color: #FF6B35;
        color: white;
        border-radius: 20px;
        padding: 10px 24px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #E55A2B;
        color: white;
    }
    div[data-testid="stTabs"] button {
        background-color: #1E1E1E;
        border-radius: 10px 10px 0 0;
    }
    div[data-testid="stTabs"] button[aria-selected="true"] {
        background-color: #FF6B35;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Navegação principal
st.sidebar.title("🔥 FitNS Pro")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navegação",
    ["🏠 Dashboard", "⚖️ Balança", "💪 Treino", "🥗 Nutrição", "📈 Progresso"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.info("""
**FitNS Pro v1.0**
- 50+ Exercícios
- 40+ Alimentos
- Cálculos TDEE/IMC
- Acompanhamento completo
""")

# Renderiza página selecionada
if page == "🏠 Dashboard":
    render_dashboard()
elif page == "⚖️ Balança":
    render_balance_scale()
elif page == "💪 Treino":
    render_workout()
elif page == "🥗 Nutrição":
    render_nutrition()
elif page == "📈 Progresso":
    render_progress()

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("© 2024 FitNS Pro - Todos os direitos reservados")

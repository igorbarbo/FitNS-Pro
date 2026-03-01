# pages/my_plan.py
import streamlit as st
from modules.header import render_header
from modules.navigation import render_navigation
from utils.custom_workout import CUSTOM_WORKOUT

def show():
    user = st.session_state.user
    render_header(user)
    render_navigation()
    st.markdown('<div class="slide-in">', unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-bottom: 20px;">
        <h2 style="margin:0; font-size: 24px;">🎯 Meu Plano Personalizado</h2>
        <p style="color: #8b8b9a; font-size: 12px; margin-top: 5px;">Otimizado para 40 min ginásio (13:00) + 25 min casa (06:35)</p>
    </div>
    """, unsafe_allow_html=True)

    # Treino em Casa
    casa = CUSTOM_WORKOUT["casa"]
    with st.expander(f"### {casa['nome']}", expanded=True):
        st.markdown(f"""
        **🕐 Horário:** {casa['horario']}  
        **📅 Dias:** {casa['dias']}  
        **🎯 Foco:** {casa['foco']}  
        **🔄 Circuito:** {casa['rodadas']}
        """)
        for exercicio, detalhe, emoji in casa["circuito"]:
            st.markdown(f"- {emoji} **{exercicio}**: {detalhe}")

    # Treino no Ginásio (cada dia)
    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
    for dia in dias_semana:
        treino = CUSTOM_WORKOUT["ginasio"][dia]
        with st.expander(f"### {treino['nome']}"):
            st.markdown(f"**🎯 Foco:** {treino['foco']}")
            for exercicio, reps in treino["exercicios"]:
                st.markdown(f"- **{exercicio}**: {reps}")

    # Fim de semana
    st.markdown("### 🌟 Fim de Semana")
    col1, col2 = st.columns(2)
    with col1:
        sab = CUSTOM_WORKOUT["fim_de_semana"]["Sábado"]
        st.markdown(f"**{sab['nome']}**")
        for atv in sab["atividades"]:
            st.markdown(f"- {atv}")
    with col2:
        dom = CUSTOM_WORKOUT["fim_de_semana"]["Domingo"]
        st.markdown(f"**{dom['nome']}**")
        for atv in dom["atividades"]:
            st.markdown(f"- {atv}")

    # Dicas importantes
    st.markdown("### 💡 Dicas para o Sucesso")
    for dica in CUSTOM_WORKOUT["dicas"]:
        st.info(dica)

    st.markdown("---")
    st.success("🚀 Amanhã às 06:30 começa a tua jornada para os 70kg! Força!")

    st.markdown('</div>', unsafe_allow_html=True)

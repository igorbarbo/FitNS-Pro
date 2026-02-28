"""
FitNS Pro v2.0 - Aplicativo Moderno de Fitness
Tema escuro com glassmorphism
"""
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="FitNS Pro", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
* { font-family: 'Inter', sans-serif; }
body { background: #0f0f1a; color: #fff; }
.glass { background: rgba(255,255,255,0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.06); border-radius: 16px; }
.btn-glow { background: linear-gradient(135deg, #00d4ff, #7b2cbf); border: none; color: white; padding: 12px 24px; border-radius: 12px; font-weight: 600; cursor: pointer; transition: all 0.3s; }
.btn-glow:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(0,212,255,0.3); }
.progress-circle { width: 120px; height: 120px; border-radius: 50%; background: conic-gradient(#ef4444 var(--p), rgba(255,255,255,0.1) 0); display: flex; align-items: center; justify-content: center; margin: 0 auto; }
.progress-circle-inner { width: 90px; height: 90px; border-radius: 50%; background: #1a1a2e; display: flex; align-items: center; justify-content: center; }
@keyframes pulse-glow { 0%, 100% { box-shadow: 0 0 20px rgba(0,212,255,0.4); } 50% { box-shadow: 0 0 30px rgba(0,212,255,0.6); } }
</style>
""", unsafe_allow_html=True)
USUARIO = {"nome": "Alexandre", "plano": "Premium", "notificacoes": 3}
NUTRICAO = {"calorias": {"atual": 1850, "meta": 2200}, "proteina": {"atual": 140, "meta": 180}, "agua": {"atual": 2.4, "meta": 3.0}, "carbos": {"atual": 180, "meta": 250}, "gorduras": {"atual": 55, "meta": 70}}
PROGRESSO = {"dias": ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"], "peso": [79.2, 79.0, 78.8, 78.9, 78.6, 78.5, 78.5], "variacao": "-0.8kg"}
ESTATISTICAS = [{"label": "Treinos", "valor": "24", "meta": "30", "cor": "#00d4ff"}, {"label": "Calorias", "valor": "15.2k", "meta": "18k", "cor": "#ef4444"}, {"label": "Proteína", "valor": "892g", "meta": "1.2kg", "cor": "#10b981"}, {"label": "Água", "valor": "45L", "meta": "60L", "cor": "#3b82f6"}]
TREINOS = [("🦵", "Pernas - Dia 4", "45 min", "6 exercícios", "Hoje", True), ("🏋️", "Peito e Tríceps", "50 min", "8 exercícios", "Amanhã", False), ("🎯", "Costas e Bíceps", "40 min", "7 exercícios", "Quinta", False), ("🏃", "Cardio HIIT", "30 min", "4 exercícios", "Sexta", False)]
ALIMENTOS = [("🍳", "Ovos Mexidos", "3 ovos • 280 kcal", 280, True), ("🍌", "Banana", "1 unidade • 105 kcal", 105, False), ("🍗", "Frango Grelhado", "150g • 248 kcal", 248, True), ("🍚", "Arroz Integral", "150g • 195 kcal", 195, False)]

if 'timer_running' not in st.session_state: st.session_state.timer_running = False
if 'timer_start' not in st.session_state: st.session_state.timer_start = None
if 'elapsed' not in st.session_state: st.session_state.elapsed = timedelta(0)
    st.markdown(f"""
<div style="display: flex; justify-content: space-between; align-items: center; padding: 20px 0; margin-bottom: 24px;">
    <div>
        <h1 style="margin: 0; font-size: 32px; font-weight: 800; background: linear-gradient(135deg, #fff, #00d4ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">FitNS Pro</h1>
        <p style="margin: 4px 0 0 0; color: #8b8b9a; font-size: 14px;">Olá, {USUARIO['nome']} 👋</p>
    </div>
    <div style="display: flex; gap: 16px; align-items: center;">
        <span style="background: linear-gradient(135deg, #7b2cbf, #00d4ff); padding: 6px 12px; border-radius: 20px; font-size: 12px; font-weight: 600;">{USUARIO['plano']}</span>
        <span style="position: relative; font-size: 24px; cursor: pointer;">🔔<span style="position: absolute; top: -5px; right: -5px; background: #ef4444; color: white; border-radius: 50%; width: 18px; height: 18px; font-size: 11px; display: flex; align-items: center; justify-content: center;">{USUARIO['notificacoes']}</span></span>
    </div>
</div>
""", unsafe_allow_html=True)

tab_inicio, tab_treino, tab_nutricao, tab_progresso = st.tabs(["🏠 Início", "💪 Treino", "🥗 Nutrição", "📈 Progresso"])
with tab_inicio:
    col_esq, col_centro, col_dir = st.columns([1, 1.6, 1])
    with col_esq:
        cal = NUTRICAO["calorias"]
        pct = int((cal["atual"] / cal["meta"]) * 100)
        st.markdown(f"""
        <div class="glass" style="padding: 24px; margin-bottom: 16px;">
            <h3 style="margin: 0 0 16px 0; font-size: 16px; color: #8b8b9a;">Calorias Hoje 🔥</h3>
            <div class="progress-circle" style="--p: {pct}%;"><div class="progress-circle-inner"><span style="font-size: 24px; font-weight: 800;">{pct}%</span></div></div>
            <div style="text-align: center; margin-top: 16px;"><span style="font-size: 32px; font-weight: 800;">{cal['atual']}</span><span style="color: #8b8b9a;"> / {cal['meta']} kcal</span></div>
        </div>
        """, unsafe_allow_html=True)
        prot = NUTRICAO["proteina"]
        st.markdown(f"""
        <div class="glass" style="padding: 20px; margin-bottom: 16px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 8px;"><span style="color: #8b8b9a; font-size: 14px;">💪 Proteína</span><span style="font-size: 14px;">{prot['atual']}/{prot['meta']}g</span></div>
            <div style="height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; overflow: hidden;"><div style="width: {(prot['atual']/prot['meta'])*100}%; height: 100%; background: linear-gradient(90deg, #10b981, #059669); border-radius: 4px;"></div></div>
        </div>
        """, unsafe_allow_html=True)
        agua = NUTRICAO["agua"]
        st.markdown(f"""
        <div class="glass" style="padding: 20px; margin-bottom: 16px;">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;"><span style="font-size: 32px;">{'🥤' * int(agua['atual']/0.6)}</span><div><div style="font-size: 24px; font-weight: 700;">{agua['atual']} <span style="font-size: 14px; color: #8b8b9a;">/ {agua['meta']} L</span></div></div></div>
            <div style="height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; overflow: hidden;"><div style="width: {(agua['atual']/agua['meta'])*100}%; height: 100%; background: linear-gradient(90deg, #3b82f6, #2563eb); border-radius: 4px;"></div></div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="glass" style="padding: 20px;">
            <h4 style="margin: 0 0 12px 0; color: #8b8b9a; font-size: 14px;">📅 Próximo Treino</h4>
            <div style="height: 100px; background: linear-gradient(135deg, #1a1a2e, #2d2d44); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 48px; margin-bottom: 12px;">🏋️</div>
            <h4 style="margin: 0 0 4px 0; font-size: 16px;">Peito e Tríceps</h4>
            <p style="margin: 0 0 12px 0; color: #8b8b9a; font-size: 13px;">Amanhã • 18:00</p>
            <button class="btn-glow" style="width: 100%;">Ver Treino</button>
        </div>
        """, unsafe_allow_html=True)
     with col_centro:
        st.markdown("""
        <div class="glass" style="padding: 24px; margin-bottom: 20px; border: 1px solid rgba(0,212,255,0.2);">
            <div style="height: 140px; background: linear-gradient(135deg, rgba(0,212,255,0.1), rgba(123,44,191,0.1)); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 64px; margin-bottom: 16px;">🦵</div>
            <h3 style="margin: 0 0 4px 0; font-size: 20px;">Pernas - Dia 4</h3>
            <p style="margin: 0 0 16px 0; color: #00d4ff; font-size: 14px;">⏱️ 45 min estimado</p>
            <button class="btn-glow" style="width: 100%; padding: 16px; animation: pulse-glow 2s infinite;">▶ Iniciar Treino Agora</button>
        </div>
        """, unsafe_allow_html=True)
        if st.session_state.timer_running and st.session_state.timer_start: st.session_state.elapsed = datetime.now() - st.session_state.timer_start
        horas, resto = divmod(int(st.session_state.elapsed.total_seconds()), 3600)
        minutos, segundos = divmod(resto, 60)
        tempo_str = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
        st.markdown(f"""
        <div class="glass" style="padding: 24px; margin-bottom: 20px;">
            <h4 style="margin: 0 0 16px 0; color: #8b8b9a; font-size: 14px;">⏱️ Timer de Treino</h4>
            <div style="text-align: center; font-size: 48px; font-weight: 800; font-family: monospace; color: {'#00d4ff' if st.session_state.timer_running else '#fff'};">{tempo_str}</div>
        </div>
        """, unsafe_allow_html=True)
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("⏸ Pausar" if st.session_state.timer_running else "▶ Iniciar", use_container_width=True, type="primary" if not st.session_state.timer_running else "secondary"):
                st.session_state.timer_running = not st.session_state.timer_running
                if st.session_state.timer_running: st.session_state.timer_start = datetime.now() - st.session_state.elapsed
                st.rerun()
        with col_btn2:
            if st.button("⏹ Finalizar", use_container_width=True):
                st.session_state.timer_running = False
                st.session_state.timer_start = None
                st.session_state.elapsed = timedelta(0)
                st.rerun()
        st.markdown(f"""
        <div class="glass" style="padding: 24px; margin-top: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                <span style="color: #8b8b9a; font-size: 13px;">Progresso Semanal</span>
                <span style="color: #10b981; font-weight: 700;">{PROGRESSO['variacao']} ↑</span>
            </div>
        """, unsafe_allow_html=True)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=PROGRESSO["dias"], y=PROGRESSO["peso"], mode='lines+markers', line=dict(color='#00d4ff', width=3), marker=dict(size=8, color='#00d4ff'), fill='tozeroy', fillcolor='rgba(0,212,255,0.1)'))
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=20, r=20, t=20, b=20), xaxis=dict(showgrid=False, tickfont=dict(color='#8b8b9a')), yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', tickfont=dict(color='#8b8b9a')), height=200)
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        cols = st.columns(4)
        for i, stat in enumerate(ESTATISTICAS):
            with cols[i]: st.markdown(f"""
            <div style="text-align: center; padding: 12px;">
                <div style="font-size: 20px; font-weight: 800; color: {stat['cor']};">{stat['valor']}</div>
                <div style="font-size: 11px; color: #8b8b9a; margin-top: 4px;">{stat['label']}</div>
                <div style="font-size: 10px; color: #6b6b7b;">meta: {stat['meta']}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
      with col_dir:
        nutri_content = '<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;"><span style="color: #8b8b9a; font-size: 13px;">🥗 Nutrição Hoje</span><span style="font-size: 18px; cursor: pointer;">🔄</span></div><button class="btn-glow" style="width: 100%; margin-bottom: 16px; padding: 12px; font-size: 14px;">+ Adicionar Alimento</button>'
        for icon, nome, detalhes, cal, fire in ALIMENTOS: nutri_content += f"""
        <div style="display: flex; align-items: center; gap: 12px; padding: 12px; background: rgba(255,255,255,0.02); border-radius: 12px; margin-bottom: 8px;">
            <span style="font-size: 28px;">{icon}</span>
            <div style="flex: 1;"><div style="font-size: 14px; font-weight: 600;">{nome}</div><div style="font-size: 12px; color: #8b8b9a;">{detalhes}</div></div>
            <span style="font-size: 16px;">{'🔥' if fire else ''}</span>
        </div>
        """
        nutri_content += '<div style="margin-top: 16px; padding-top: 16px; border-top: 1px solid rgba(255,255,255,0.08);">'
        macros = [("Proteína", NUTRICAO["proteina"], "#10b981"), ("Carbos", NUTRICAO["carbos"], "#f59e0b"), ("Gorduras", NUTRICAO["gorduras"], "#ef4444")]
        for label, valores, cor in macros:
            pct = int((valores["atual"]/valores["meta"])*100)
            nutri_content += f"""
            <div style="margin-bottom: 12px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px; font-size: 13px;"><span>{label}</span><span>{valores['atual']}/{valores['meta']}g</span></div>
                <div style="height: 6px; background: rgba(255,255,255,0.1); border-radius: 3px; overflow: hidden;"><div style="width: {pct}%; height: 100%; background: {cor}; border-radius: 3px;"></div></div>
            </div>
            """
        nutri_content += "</div>"
        st.markdown(f'<div class="glass" style="padding: 20px;">{nutri_content}</div>', unsafe_allow_html=True)
with tab_treino:
    st.markdown('<div style="margin-bottom: 24px;"><h2 style="font-size: 24px; margin-bottom: 4px;">💪 Meus Treinos</h2><p style="color: #8b8b9a; font-size: 14px;">Escolha seu treino de hoje</p></div>', unsafe_allow_html=True)
    cols = st.columns(3)
    for i, (col, filtro, opts) in enumerate(zip(cols, ["Categoria", "Duração", "Intensidade"], [["Todos", "Força", "Cardio"], ["Qualquer", "< 30 min", "30-60 min"], ["Todas", "Leve", "Moderada", "Alta"]])):
        with col: st.selectbox(filtro, opts, label_visibility="collapsed")
    for icon, titulo, duracao, exercicios, data_treino, ativo in TREINOS:
        border = "border: 1px solid rgba(0,212,255,0.3);" if ativo else ""
        btn = '<span style="background: rgba(0,212,255,0.2); color: #00d4ff; padding: 4px 12px; border-radius: 12px; font-size: 12px;">HOJE</span>' if ativo else f'<span style="color: #8b8b9a; font-size: 12px;">{data_treino}</span>'
        st.markdown(f"""
        <div class="glass" style="padding: 20px; margin: 12px 0; display: flex; align-items: center; gap: 16px; {border}">
            <div style="font-size: 40px;">{icon}</div>
            <div style="flex: 1;"><h4 style="margin: 0 0 4px 0; font-size: 16px;">{titulo}</h4><p style="margin: 0; color: #8b8b9a; font-size: 13px;">{duracao} • {exercicios}</p></div>
            {btn}
        </div>
        """, unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; margin-top: 24px; padding: 32px; border: 2px dashed rgba(255,255,255,0.1); border-radius: 16px;">
        <div style="font-size: 40px; margin-bottom: 12px;">➕</div>
        <h3 style="color: #8b8b9a; font-size: 16px; margin-bottom: 4px;">Criar Novo Treino</h3>
        <p style="color: #6b6b7b; font-size: 13px;">Monte seu próprio plano</p>
    </div>
    """, unsafe_allow_html=True)
with tab_nutricao:
    st.markdown('<div style="margin-bottom: 24px;"><h2 style="font-size: 24px; margin-bottom: 4px;">🥗 Diário Alimentar</h2><p style="color: #8b8b9a; font-size: 14px;">Acompanhe suas macros</p></div>', unsafe_allow_html=True)
    cols = st.columns(4)
    metricas = [("🔥 Calorias", f"{NUTRICAO['calorias']['atual']}", f"/{NUTRICAO['calorias']['meta']}", "84%"), ("💪 Proteína", f"{NUTRICAO['proteina']['atual']}g", f"/{NUTRICAO['proteina']['meta']}g", "78%"), ("🍞 Carbos", f"{NUTRICAO['carbos']['atual']}g", f"/{NUTRICAO['carbos']['meta']}g", "72%"), ("🥑 Gorduras", f"{NUTRICAO['gorduras']['atual']}g", f"/{NUTRICAO['gorduras']['meta']}g", "79%")]
    for col, (label, val, total, pct) in zip(cols, metricas):
        with col: st.markdown(f"""
        <div class="glass" style="padding: 20px; text-align: center;">
            <div style="font-size: 11px; color: #8b8b9a; margin-bottom: 8px;">{label}</div>
            <div style="font-size: 28px; font-weight: 800;">{val}<span style="font-size: 14px; color: #6b6b7b;">{total}</span></div>
            <div style="font-size: 12px; color: #10b981; margin-top: 4px;">{pct}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('<div style="margin-top: 24px;"><h3 style="font-size: 18px; margin-bottom: 16px;">🕐 Refeições de Hoje</h3></div>', unsafe_allow_html=True)
    refeicoes = [("Café da Manhã", "07:30", [("🍳", "Ovos", "3 ovos", 280), ("☕", "Café", "200ml", 5)], 285), ("Almoço", "12:30", [("🍚", "Arroz", "150g", 195), ("🍗", "Frango", "150g", 248)], 443), ("Jantar", "19:00", [("🥩", "Salmão", "200g", 412), ("🥦", "Brócolis", "100g", 35)], 447)]
    for titulo, horario, itens, total in refeicoes:
        itens_html = "".join([f"""
        <div style="display: flex; align-items: center; gap: 10px; margin: 6px 0; padding: 8px; background: rgba(255,255,255,0.02); border-radius: 8px;">
            <span style="font-size: 20px;">{icon}</span>
            <div style="flex: 1;"><div style="font-size: 14px;">{nome}</div><div style="font-size: 11px; color: #6b6b7b;">{qtd}</div></div>
            <div style="font-size: 12px; color: #f59e0b;">{cal}</div>
        </div>
        """ for icon, nome, qtd, cal in itens])
        st.markdown(f"""
        <div class="glass" style="margin: 12px 0; padding: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <div><h4 style="margin: 0; font-size: 15px;">{titulo}</h4><span style="color: #6b6b7b; font-size: 12px;">{horario}</span></div>
                <div style="text-align: right;"><div style="font-size: 20px; font-weight: 700;">{total}</div><div style="font-size: 10px; color: #6b6b7b;">kcal</div></div>
            </div>
            {itens_html}
        </div>
        """, unsafe_allow_html=True)
        with tab_progresso:
    st.markdown('<div style="margin-bottom: 24px;"><h2 style="font-size: 24px; margin-bottom: 4px;">📈 Sua Evolução</h2><p style="color: #8b8b9a; font-size: 14px;">Acompanhe suas métricas</p></div>', unsafe_allow_html=True)
    cols = st.columns(4)
    for i, (label, dias) in enumerate([("7 Dias", "7d"), ("30 Dias", "30d"), ("3 Meses", "3m"), ("1 Ano", "1a")]):
        with cols[i]: st.button(label, use_container_width=True, type="primary" if i == 1 else "secondary")
    col_graf1, col_graf2 = st.columns([2, 1])
    with col_graf1:
        st.markdown('<div class="glass" style="padding: 20px;">', unsafe_allow_html=True)
        st.markdown('<h3 style="margin-bottom: 16px; font-size: 16px;">⚖️ Evolução do Peso</h3>', unsafe_allow_html=True)
        meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
        peso = [82.5, 81.2, 80.1, 79.3, 78.8, 78.5]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=meses, y=peso, mode='lines+markers', line=dict(color='#10b981', width=3), marker=dict(size=10, color='#10b981'), fill='tozeroy', fillcolor='rgba(16,185,129,0.1)'))
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=20, r=20, t=20, b=20), xaxis=dict(showgrid=False, tickfont=dict(color='#8b8b9a')), yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', tickfont=dict(color='#8b8b9a')), height=280)
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)
    with col_graf2:
        for titulo, valor, mudanca in [("Peso Atual", "78.5 kg", "-4.0 kg"), ("Gordura", "18.2%", "-2.1%"), ("Massa Magra", "64.2 kg", "+1.8 kg"), ("IMC", "24.1", "-1.2")]:
            st.markdown(f"""
            <div class="glass" style="padding: 16px; margin: 10px 0; text-align: center;">
                <div style="font-size: 11px; color: #8b8b9a; margin-bottom: 6px;">{titulo}</div>
                <div style="font-size: 24px; font-weight: 800;">{valor}</div>
                <div style="font-size: 12px; color: #10b981;">{mudanca} ↓</div>
            </div>
            """, unsafe_allow_html=True)
    col_sec1, col_sec2 = st.columns(2)
    with col_sec1:
        st.markdown('<div class="glass" style="padding: 20px;">', unsafe_allow_html=True)
        st.markdown('<h3 style="margin-bottom: 16px; font-size: 16px;">💪 Volume de Treino</h3>', unsafe_allow_html=True)
        semanas = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']
        volume = [1200, 1350, 1400, 1550, 1600, 1750]
        fig = go.Figure(go.Bar(x=semanas, y=volume, marker_color='#3b82f6', marker_line_color='#60a5fa', marker_line_width=1))
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=20, r=20, t=20, b=20), xaxis=dict(showgrid=False, tickfont=dict(color='#8b8b9a')), yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', tickfont=dict(color='#8b8b9a')), height=220)
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)
    with col_sec2:
        st.markdown('<div class="glass" style="padding: 20px;">', unsafe_allow_html=True)
        st.markdown('<h3 style="margin-bottom: 16px; font-size: 16px;">🎯 Consistência</h3>', unsafe_allow_html=True)
        dias = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']
        sems = ['S1', 'S2', 'S3', 'S4']
        matriz = [[1,1,0,1,1,0,1],[1,1,1,0,1,1,0],[0,1,1,1,1,0,1],[1,1,1,1,0,1,1]]
        fig = go.Figure(data=go.Heatmap(z=matriz, x=dias, y=sems, colorscale=[[0, 'rgba(255,255,255,0.05)'], [1, '#00d4ff']], showscale=False))
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=20, r=20, t=20, b=20), height=220)
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)
        

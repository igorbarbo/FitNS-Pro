"""
FitNS Pro v2.0 - Aplicativo Moderno de Fitness
Tema escuro com glassmorphism
"""
import streamlit as st
import time
from datetime import datetime, timedelta
from styles import (
    load_css, Components, Charts, 
    MockData as data
)

# Configuração da página
st.set_page_config(
    page_title="FitNS Pro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Carregar CSS
load_css()

# Estado da sessão
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
if 'timer_start' not in st.session_state:
    st.session_state.timer_start = None
if 'elapsed' not in st.session_state:
    st.session_state.elapsed = timedelta(0)
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "inicio"

# Header
st.markdown(Components.header(
    data.USUARIO["nome"],
    data.USUARIO["plano"],
    data.USUARIO["notificacoes"]
), unsafe_allow_html=True)

# Navegação por tabs
tab_inicio, tab_treino, tab_nutricao, tab_progresso = st.tabs([
    "🏠 Início", "💪 Treino", "🥗 Nutrição", "📈 Progresso"
])

# ============================================
# ABA: INÍCIO (Dashboard)
# ============================================
with tab_inicio:
    col_esq, col_centro, col_dir = st.columns([1, 1.6, 1])
    
    # Coluna Esquerda
    with col_esq:
        # Calorias com círculo
        cal = data.NUTRICAO_HOJE["calorias"]
        st.markdown(Components.card(
            "Calorias Hoje 🔥",
            Components.progress_circle(cal["atual"], cal["meta"], "#ef4444") +
            f"""
            <div style="text-align: center; margin-top: 16px;">
                <span style="font-size: 36px; font-weight: 800; color: #fff;">{cal['atual']}</span>
                <span style="font-size: 16px; color: #8b8b9a;"> / {cal['meta']} kcal</span>
            </div>
            """,
            "", False, "slide"
        ), unsafe_allow_html=True)
        
        # Proteína
        prot = data.NUTRICAO_HOJE["proteina"]
        st.markdown(Components.card(
            "",
            Components.progress_bar("Proteína", prot["atual"], prot["meta"], "protein"),
            "💧 Proteína"
        ), unsafe_allow_html=True)
        
        # Água
        agua = data.NUTRICAO_HOJE["agua"]
        garrafas = int(agua["atual"] / 0.6)
        st.markdown(Components.card(
            "",
            f"""
            <div style="display: flex; align-items: center; gap: 16px; margin: 16px 0;">
                <div style="font-size: 36px;">{'🥤' * garrafas}{'💧' if agua['atual'] % 0.6 > 0.3 else ''}</div>
                <div>
                    <div style="font-size: 28px; font-weight: 700; color: #fff;">{agua['atual']} <span style="font-size: 16px; color: #8b8b9a;">/ {agua['meta']} L</span></div>
                </div>
            </div>
            {Components.progress_bar("", int(agua['atual']*10), int(agua['meta']*10), "water", "L")}
            """,
            "💧 Água"
        ), unsafe_allow_html=True)
        
        # Próximo treino
        st.markdown(Components.card(
            "",
            """
            <div style="height: 140px; background: linear-gradient(135deg, #1a1a2e, #2d2d44); border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 64px; margin-bottom: 16px;">
                🏋️
            </div>
            <h4 style="margin: 0 0 8px 0; color: #fff; font-size: 18px;">Peito e Tríceps</h4>
            <p style="margin: 0 0 16px 0; color: #8b8b9a; font-size: 14px;">Amanhã • 18:00</p>
            <button class="btn-glow" style="width: 100%; padding: 12px; font-size: 14px;">Ver Treino Completo</button>
            """,
            "📅 Próximo Treino"
        ), unsafe_allow_html=True)
    
    # Coluna Central
    with col_centro:
        # Treino Ativo
        st.markdown(Components.card(
            "",
            """
            <div style="height: 160px; background: linear-gradient(135deg, rgba(0,212,255,0.1), rgba(123,44,191,0.1)); border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 72px; margin-bottom: 20px; border: 1px solid rgba(0,212,255,0.2);">
                🦵
            </div>
            <h3 style="margin: 0 0 8px 0; color: #fff; font-size: 22px;">Pernas - Dia 4</h3>
            <p style="margin: 0 0 20px 0; color: #00d4ff; font-size: 15px; display: flex; align-items: center; gap: 8px;">
                <span>⏱️</span> 35:00 min estimado
            </p>
            <button class="btn-glow" style="width: 100%; padding: 16px; font-size: 16px; animation: pulse-glow 2s infinite;">▶ Iniciar Treino Agora</button>
            """,
            "⚡ Treino Ativo",
            True
        ), unsafe_allow_html=True)
        
        # Timer
        if st.session_state.timer_running and st.session_state.timer_start:
            st.session_state.elapsed = datetime.now() - st.session_state.timer_start
        
        horas, resto = divmod(int(st.session_state.elapsed.total_seconds()), 3600)
        minutos, segundos = divmod(resto, 60)
        tempo_str = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
        
        st.markdown(Components.card(
            "",
            Components.timer_display(tempo_str, st.session_state.timer_running) +
            """
            <div style="display: flex; gap: 16px; justify-content: center; margin-top: 24px;">
            """,
            "⏱️ Timer de Treino"
        ), unsafe_allow_html=True)
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button(
                "⏸ Pausar" if st.session_state.timer_running else "▶ Iniciar",
                use_container_width=True,
                type="primary" if not st.session_state.timer_running else "secondary"
            ):
                st.session_state.timer_running = not st.session_state.timer_running
                if st.session_state.timer_running:
                    st.session_state.timer_start = datetime.now() - st.session_state.elapsed
                st.rerun()
        
        with col_btn2:
            if st.button("⏹ Finalizar", use_container_width=True, type="secondary"):
                st.session_state.timer_running = False
                st.session_state.timer_start = None
                st.session_state.elapsed = timedelta(0)
                st.rerun()
        
        st.markdown("</div></div>", unsafe_allow_html=True)
        
        # Progresso Semanal
        prog = data.PROGRESSO_SEMANAL
        st.markdown(Components.card(
            "",
            f"""
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <span style="color: #8b8b9a; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;">Progresso Semanal</span>
                <span style="color: #10b981; font-weight: 700; font-size: 14px;">{prog['variacao']} ↑</span>
            </div>
            """,
            ""
        ), unsafe_allow_html=True)
        
        fig = Charts.line_chart(prog["dias"], prog["peso"], "", "#00d4ff")
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        
        st.markdown(Components.stats_grid(data.ESTATISTICAS), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Coluna Direita
    with col_dir:
        # Nutrição
        nutri_content = """
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <span style="color: #8b8b9a; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;">🥗 Nutrição Hoje</span>
            <span style="font-size: 20px; cursor: pointer;">🔄</span>
        </div>
        <button class="btn-glow" style="width: 100%; margin-bottom: 20px; padding: 14px; background: linear-gradient(135deg, #3b82f6, #1d4ed8); font-size: 14px;">
            + Adicionar Alimento
        </button>
        """
        
        for icon, nome, detalhes, cal, fire in data.ALIMENTOS:
            nutri_content += Components.food_item(icon, nome, detalhes, cal, fire)
        
        # Resumo macros
        nutri_content += """
        <div style="margin-top: 28px; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.08);">
        """
        
        macros = [
            ("Proteína", data.NUTRICAO_HOJE["proteina"], "protein"),
            ("Carboidratos", data.NUTRICAO_HOJE["carbos"], "carbs"),
            ("Gorduras", data.NUTRICAO_HOJE["gorduras"], "fats"),
        ]
        
        for label, valores, tipo in macros:
            nutri_content += Components.progress_bar(
                label, valores["atual"], valores["meta"], tipo
            )
        
        nutri_content += "</div>"
        
        st.markdown(Components.card("", nutri_content, ""), unsafe_allow_html=True)

# ============================================
# ABA: TREINO
# ============================================
with tab_treino:
    st.markdown("""
    <div style="margin-bottom: 32px;">
        <h2 style="color: #fff; font-size: 28px; margin-bottom: 8px;">💪 Meus Treinos</h2>
        <p style="color: #8b8b9a; font-size: 15px;">Escolha seu treino de hoje ou veja os próximos agendados</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Filtros
    col_filtro1, col_filtro2, col_filtro3 = st.columns(3)
    with col_filtro1:
        st.selectbox("Categoria", ["Todos", "Força", "Cardio", "Mobilidade"], label_visibility="collapsed")
    with col_filtro2:
        st.selectbox("Duração", ["Qualquer", "< 30 min", "30-45 min", "> 45 min"], label_visibility="collapsed")
    with col_filtro3:
        st.selectbox("Intensidade", ["Todas", "Leve", "Moderada", "Alta"], label_visibility="collapsed")
    
    # Lista de treinos
    for icon, titulo, duracao, exercicios, data_treino, ativo in data.TREINOS:
        st.markdown(Components.workout_card(
            icon, titulo, f"{duracao} • {exercicios}", 
            data_treino, duracao, exercicios, ativo
        ), unsafe_allow_html=True)
    
    # Botão adicionar
    st.markdown("""
    <div style="text-align: center; margin-top: 32px; padding: 40px; border: 2px dashed rgba(255,255,255,0.1); border-radius: 24px;">
        <div style="font-size: 48px; margin-bottom: 16px;">➕</div>
        <h3 style="color: #8b8b9a; font-size: 18px; margin-bottom: 8px;">Criar Novo Treino</h3>
        <p style="color: #6b6b7b; font-size: 14px;">Monte seu próprio plano de exercícios</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# ABA: NUTRIÇÃO
# ============================================
with tab_nutricao:
    # Resumo do dia
    st.markdown("""
    <div style="margin-bottom: 32px;">
        <h2 style="color: #fff; font-size: 28px; margin-bottom: 8px;">🥗 Diário Alimentar</h2>
        <p style="color: #8b8b9a; font-size: 15px;">Acompanhe suas macros e calorias do dia</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    
    metricas = [
        ("🔥 Calorias", f"{data.NUTRICAO_HOJE['calorias']['atual']}", f"/{data.NUTRICAO_HOJE['calorias']['meta']}", "84%", "metric-positive"),
        ("💪 Proteína", f"{data.NUTRICAO_HOJE['proteina']['atual']}g", f"/{data.NUTRICAO_HOJE['proteina']['meta']}g", "73%", "metric-positive"),
        ("🍞 Carbos", f"{data.NUTRICAO_HOJE['carbos']['atual']}g", f"/{data.NUTRICAO_HOJE['carbos']['meta']}g", "73%", "metric-positive"),
        ("🥑 Gorduras", f"{data.NUTRICAO_HOJE['gorduras']['atual']}g", f"/{data.NUTRICAO_HOJE['gorduras']['meta']}g", "65%", "metric-positive"),
    ]
    
    for col, (label, val, total, pct, cls) in zip([col_m1, col_m2, col_m3, col_m4], metricas):
        with col:
            st.markdown(f"""
            <div class="glass" style="padding: 24px; text-align: center;">
                <div style="font-size: 12px; color: #8b8b9a; margin-bottom: 12px; text-transform: uppercase;">{label}</div>
                <div style="font-size: 32px; font-weight: 800; color: #fff;">{val}<span style="font-size: 16px; color: #6b6b7b;">{total}</span></div>
                <div style="font-size: 14px; color: #10b981; margin-top: 8px; font-weight: 600;">{pct}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Timeline de refeições
    st.markdown("""
    <div style="margin-top: 32px;">
        <h3 style="color: #fff; font-size: 20px; margin-bottom: 20px;">🕐 Timeline de Hoje</h3>
    </div>
    """, unsafe_allow_html=True)
    
    refeicoes = [
        ("Café da Manhã", "07:30", [("🍳", "Ovos Mexidos", "3 ovos", 280), ("☕", "Café Preto", "200ml", 5)], 285),
        ("Lanche da Manhã", "10:00", [("🍌", "Banana", "1 unidade", 105), ("🥜", "Amendoim", "30g", 180)], 285),
        ("Almoço", "12:30", [("🍚", "Arroz", "150g", 195), ("🍗", "Frango", "150g", 248), ("🥗", "Salada", "100g", 35)], 478),
        ("Lanche da Tarde", "16:00", [("🍎", "Maçã", "1 unidade", 95), ("🥛", "Whey Protein", "1 scoop", 120)], 215),
        ("Jantar", "19:30", [("🥩", "Salmão", "200g", 412), ("🥦", "Brócolis", "100g", 35)], 447),
    ]
    
    for titulo, horario, itens, total in refeicoes:
        itens_html = ""
        for icon, nome, qtd, cal in itens:
            itens_html += f"""
            <div style="display: flex; align-items: center; gap: 12px; margin: 8px 0; padding: 8px; background: rgba(255,255,255,0.02); border-radius: 8px;">
                <span style="font-size: 20px;">{icon}</span>
                <div style="flex: 1;">
                    <div style="font-size: 14px; color: #fff;">{nome}</div>
                    <div style="font-size: 12px; color: #6b6b7b;">{qtd}</div>
                </div>
                <div style="font-size: 13px; color: #f59e0b; font-weight: 600;">{cal}</div>
            </div>
            """
        
        st.markdown(f"""
        <div class="glass" style="margin: 16px 0; padding: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <div>
                    <h4 style="color: #fff; margin: 0; font-size: 16px;">{titulo}</h4>
                    <span style="color: #6b6b7b; font-size: 13px;">{horario}</span>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 20px; font-weight: 700; color: #fff;">{total}</div>
                    <div style="font-size: 11px; color: #6b6b7b;">kcal</div>
                </div>
            </div>
            {itens_html}
        </div>
        """, unsafe_allow_html=True)

# ============================================
# ABA: PROGRESSO
# ============================================
with tab_progresso:
    st.markdown("""
    <div style="margin-bottom: 32px;">
        <h2 style="color: #fff; font-size: 28px; margin-bottom: 8px;">📈 Sua Evolução</h2>
        <p style="color: #8b8b9a; font-size: 15px;">Acompanhe suas métricas ao longo do tempo</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Seletor de período
    col_per1, col_per2, col_per3, col_per4 = st.columns(4)
    with col_per1:
        st.button("7 Dias", use_container_width=True)
    with col_per2:
        st.button("30 Dias", use_container_width=True, type="primary")
    with col_per3:
        st.button("3 Meses", use_container_width=True)
    with col_per4:
        st.button("1 Ano", use_container_width=True)
    
    # Gráfico principal de peso
    col_graf1, col_graf2 = st.columns([2, 1])
    
    with col_graf1:
        st.markdown('<div class="glass" style="padding: 24px;">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: #fff; margin-bottom: 20px; font-size: 18px;">⚖️ Evolução do Peso</h3>', unsafe_allow_html=True)
        
        meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
        peso_mensal = [82.5, 81.2, 80.1, 79.3, 78.8, 78.5]
        
        fig_peso = go.Figure()
        fig_peso.add_trace(go.Scatter(
            x=meses, y=peso_mensal,
            mode='lines+markers',
            line=dict(color='#10b981', width=4),
            marker=dict(size=12, color='#10b981', line=dict(width=3, color='#0f0f1a')),
            fill='tozeroy',
            fillcolor='rgba(16, 185, 129, 0.1)'
        ))
        fig_peso.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis=dict(showgrid=False, tickfont=dict(color='#8b8b9a')),
            yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', tickfont=dict(color='#8b8b9a')),
            height=300
        )
        st.plotly_chart(fig_peso, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_graf2:
        # Stats cards
        stats = [
            ("Peso Atual", "78.5 kg", "-4.0 kg", "metric-positive"),
            ("Gordura Corporal", "18.2%", "-2.1%", "metric-positive"),
            ("Massa Magra", "64.2 kg", "+1.8 kg", "metric-positive"),
            ("IMC", "24.1", "-1.2", "metric-positive"),
        ]
        
        for titulo, valor, mudanca, classe in stats:
            st.markdown(f"""
            <div class="glass" style="padding: 20px; margin: 12px 0; text-align: center;">
                <div style="font-size: 12px; color: #8b8b9a; text-transform: uppercase; margin-bottom: 8px;">{titulo}</div>
                <div style="font-size: 28px; font-weight: 800; color: #fff; margin-bottom: 4px;">{valor}</div>
                <div style="font-size: 13px; color: #10b981; font-weight: 600;">{mudanca} ↓</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Gráficos secundários
    col_sec1, col_sec2 = st.columns(2)
    
    with col_sec1:
        st.markdown('<div class="glass" style="padding: 24px;">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: #fff; margin-bottom: 20px; font-size: 18px;">💪 Volume de Treino (kg)</h3>', unsafe_allow_html=True)
        
        semanas = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']
        volume = [1200, 1350, 1400, 1550, 1600, 1750]
        
        fig_vol = go.Figure()
        fig_vol.add_trace(go.Bar(
            x=semanas, y=volume,
            marker_color='#3b82f6',
            marker_line_color='#60a5fa',
            marker_line_width=1,
            opacity=0.8
        ))
        fig_vol.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis=dict(showgrid=False, tickfont=dict(color='#8b8b9a')),
            yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', tickfont=dict(color='#8b8b9a')),
            height=250
        )
        st.plotly_chart(fig_vol, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_sec2:
        st.markdown('<div class="glass" style="padding: 24px;">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: #fff; margin-bottom: 20px; font-size: 18px;">🎯 Consistência de Treinos</h3>', unsafe_allow_html=True)
        
        # Heatmap de treinos
        dias_semana = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']
        semanas_mes = ['S1', 'S2', 'S3', 'S4']
        
        # Matriz de treinos (1 = treinou, 0 = não treinou)
        matriz = [
            [1, 1, 0, 1, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0, 1, 1],
        ]
        
        fig_heat = go.Figure(data=go.Heatmap(
            z=matriz,
            x=dias_semana,
            y=semanas_mes,
            colorscale=[[0, 'rgba(255,255,255,0.05)'], [1, '#00d4ff']],
            showscale=False
        ))
        fig_heat.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=20,

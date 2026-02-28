"""
FitNS Pro - Módulo de Estilos e Componentes
Tema escuro moderno com glassmorphism
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

# CSS Global - Tema Escuro
CSS_GLOBAL = """
<style>
    /* Reset e tema escuro */
    .stApp {
        background: linear-gradient(135deg, #0a0a0f 0%, #12121a 50%, #1a1a2e 100%);
        color: #ffffff;
    }
    
    /* Esconder elementos padrão */
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Glassmorphism base */
    .glass {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    .glass:hover {
        border: 1px solid rgba(255, 255, 255, 0.15);
        transform: translateY(-2px);
        transition: all 0.3s ease;
    }
    
    /* Gradientes de texto */
    .text-gradient {
        background: linear-gradient(90deg, #00d4ff, #7b2cbf);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Animações */
    @keyframes pulse-glow {
        0%, 100% { box-shadow: 0 0 20px rgba(0, 212, 255, 0.3); }
        50% { box-shadow: 0 0 40px rgba(0, 212, 255, 0.6); }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    @keyframes slide-in {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .animate-float { animation: float 3s ease-in-out infinite; }
    .animate-slide { animation: slide-in 0.5s ease-out; }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
    }
    ::-webkit-scrollbar-track { background: #0a0a0f; }
    ::-webkit-scrollbar-thumb { 
        background: #2a2a3a; 
        border-radius: 3px; 
    }
    ::-webkit-scrollbar-thumb:hover { background: #3a3a4a; }
    
    /* Botões customizados */
    .btn-glow {
        background: linear-gradient(135deg, #00d4ff, #0099cc);
        color: white;
        border: none;
        padding: 14px 32px;
        border-radius: 30px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3);
    }
    
    .btn-glow:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.5);
    }
    
    .btn-danger-glow {
        background: linear-gradient(135deg, #ef4444, #dc2626);
        color: white;
        border: none;
        padding: 14px 32px;
        border-radius: 30px;
        font-weight: 600;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(239, 68, 68, 0.3);
    }
    
    /* Inputs customizados */
    .stTextInput input, .stNumberInput input, .stSelectbox select {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: white !important;
        padding: 12px 16px !important;
    }
    
    .stTextInput input:focus, .stNumberInput input:focus {
        border-color: #00d4ff !important;
        box-shadow: 0 0 0 2px rgba(0, 212, 255, 0.2) !important;
    }
    
    /* Tabs customizadas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(255, 255, 255, 0.03);
        padding: 8px;
        border-radius: 16px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 12px;
        color: #8b8b9a;
        font-weight: 500;
        padding: 12px 24px;
        border: none;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.2), rgba(123, 44, 191, 0.2)) !important;
        color: #00d4ff !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
    }
    
    /* Métricas */
    .metric-container {
        text-align: center;
        padding: 20px;
    }
    
    .metric-value {
        font-size: 36px;
        font-weight: 800;
        color: #ffffff;
        line-height: 1;
    }
    
    .metric-label {
        font-size: 12px;
        color: #6b6b7b;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 8px;
    }
    
    .metric-change {
        font-size: 14px;
        font-weight: 600;
        margin-top: 4px;
    }
    
    .metric-positive { color: #10b981; }
    .metric-negative { color: #ef4444; }
</style>
"""

def load_css():
    """Carrega o CSS global"""
    st.markdown(CSS_GLOBAL, unsafe_allow_html=True)


# Componentes Reutilizáveis
class Components:
    
    @staticmethod
    def header(usuario="Igor Silva", plano="Plano Premium", notificacoes=2):
        """Header com perfil do usuário"""
        return f"""
        <div style="display: flex; align-items: center; justify-content: space-between; padding: 16px 0; margin-bottom: 24px;">
            <div style="display: flex; align-items: center; gap: 12px;">
                <div style="font-size: 28px;">⚡</div>
                <div style="font-size: 24px; font-weight: 800; background: linear-gradient(90deg, #00d4ff, #7b2cbf); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                    FitNS Pro
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 16px;">
                <div style="position: relative; padding: 10px; background: rgba(255,255,255,0.05); border-radius: 12px; cursor: pointer;">
                    🔔
                    <div style="position: absolute; top: 4px; right: 4px; width: 18px; height: 18px; background: #ef4444; border-radius: 50%; font-size: 10px; display: flex; align-items: center; justify-content: center; font-weight: 700; color: white;">
                        {notificacoes}
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div style="width: 42px; height: 42px; border-radius: 50%; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); display: flex; align-items: center; justify-content: center; font-weight: 700; color: white; font-size: 16px;">
                        {usuario[:2].upper()}
                    </div>
                    <div>
                        <div style="font-size: 14px; font-weight: 600; color: #fff;">{usuario}</div>
                        <div style="font-size: 12px; color: #10b981; display: flex; align-items: center; gap: 6px;">
                            <span style="width: 8px; height: 8px; background: #10b981; border-radius: 50%; display: inline-block; animation: pulse 2s infinite;"></span>
                            {plano}
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <style>
            @keyframes pulse {{
                0%, 100% {{ opacity: 1; }}
                50% {{ opacity: 0.5; }}
            }}
        </style>
        """
    
    @staticmethod
    def card(title, content, icon="", active=False, animation=""):
        """Card com glassmorphism"""
        active_class = "active-workout" if active else ""
        anim_class = f"animate-{animation}" if animation else ""
        
        return f"""
        <div class="glass {active_class} {anim_class}" style="padding: 24px; margin: 12px 0;">
            {f'<div style="font-size: 12px; color: #8b8b9a; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 16px;">{icon} {title}</div>' if title else ''}
            {content}
        </div>
        """
    
    @staticmethod
    def progress_circle(value, max_val, color="#00d4ff", size=120):
        """Círculo de progresso animado"""
        percentage = min(100, int((value / max_val) * 100))
        
        return f"""
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <div style="
                width: {size}px;
                height: {size}px;
                border-radius: 50%;
                background: conic-gradient(
                    from 0deg,
                    {color} 0deg,
                    {color} {percentage * 3.6}deg,
                    rgba(255,255,255,0.05) {percentage * 3.6}deg
                );
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
                animation: pulse-glow 2s infinite;
            ">
                <div style="
                    width: {size * 0.75}px;
                    height: {size * 0.75}px;
                    background: #0f0f1a;
                    border-radius: 50%;
                    position: absolute;
                "></div>
                <div style="position: relative; z-index: 1; font-size: {size * 0.2}px; font-weight: 700; color: {color};">
                    {percentage}%
                </div>
            </div>
        </div>
        <style>
            @keyframes pulse-glow {{
                0%, 100% {{ filter: drop-shadow(0 0 10px {color}40); }}
                50% {{ filter: drop-shadow(0 0 25px {color}60); }}
            }}
        </style>
        """
    
    @staticmethod
    def progress_bar(label, current, total, color_class="protein", unit="g"):
        """Barra de progresso horizontal"""
        percentage = min(100, int((current / total) * 100))
        colors = {
            "protein": "linear-gradient(90deg, #3b82f6, #60a5fa)",
            "carbs": "linear-gradient(90deg, #10b981, #34d399)",
            "fats": "linear-gradient(90deg, #f59e0b, #fbbf24)",
            "calories": "linear-gradient(90deg, #ef4444, #f87171)",
            "water": "linear-gradient(90deg, #06b6d4, #22d3ee)"
        }
        
        return f"""
        <div style="margin: 16px 0;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="color: #8b8b9a; font-size: 13px;">{label}</span>
                <span style="color: #fff; font-weight: 600; font-size: 14px;">{current}{unit} / {total}{unit}</span>
            </div>
            <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.05); border-radius: 10px; overflow: hidden;">
                <div style="
                    width: {percentage}%;
                    height: 100%;
                    background: {colors.get(color_class, colors['protein'])};
                    border-radius: 10px;
                    transition: width 0.8s ease;
                    box-shadow: 0 0 10px {colors.get(color_class, colors['protein']).split(',')[0].split('(')[1]}40;
                "></div>
            </div>
        </div>
        """
    
    @staticmethod
    def food_item(icon, name, details, calories, fire=False):
        """Item de alimento na lista"""
        fire_icon = "🔥" if fire else ""
        
        return f"""
        <div style="
            display: flex;
            align-items: center;
            padding: 16px;
            background: rgba(255,255,255,0.02);
            border-radius: 16px;
            margin: 10px 0;
            border: 1px solid rgba(255,255,255,0.05);
            transition: all 0.3s;
        " onmouseover="this.style.background='rgba(255,255,255,0.05)'; this.style.transform='translateX(5px)';" 
           onmouseout="this.style.background='rgba(255,255,255,0.02)'; this.style.transform='translateX(0)';">
            <div style="
                width: 52px;
                height: 52px;
                border-radius: 14px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 26px;
                margin-right: 16px;
                background: rgba(255,255,255,0.05);
            ">{icon}</div>
            <div style="flex: 1;">
                <div style="font-weight: 600; color: #ffffff; font-size: 15px; display: flex; align-items: center; gap: 8px;">
                    {name} {fire_icon}
                </div>
                <div style="font-size: 13px; color: #8b8b9a; margin-top: 4px;">{details}</div>
            </div>
            <div style="text-align: right;">
                <div style="font-weight: 700; color: #f59e0b; font-size: 15px;">{calories}</div>
                <div style="font-size: 11px; color: #6b6b7b;">kcal</div>
            </div>
        </div>
        """
    
    @staticmethod
    def workout_card(icon, title, details, date, duration, exercises, active=False):
        """Card de treino"""
        active_style = "background: linear-gradient(135deg, rgba(0,212,255,0.1), rgba(123,44,191,0.1)); border: 1px solid rgba(0,212,255,0.2);" if active else ""
        
        return f"""
        <div style="
            display: flex;
            align-items: center;
            padding: 24px;
            background: rgba(255,255,255,0.02);
            border-radius: 20px;
            margin: 12px 0;
            border: 1px solid rgba(255,255,255,0.05);
            {active_style}
        ">
            <div style="
                width: 64px;
                height: 64px;
                border-radius: 16px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 32px;
                margin-right: 20px;
                background: {'linear-gradient(135deg, rgba(0,212,255,0.2), rgba(0,212,255,0.05))' if active else 'rgba(255,255,255,0.05)'};
            ">{icon}</div>
            <div style="flex: 1;">
                <div style="font-weight: 700; color: #fff; font-size: 17px; margin-bottom: 6px;">{title}</div>
                <div style="font-size: 13px; color: #8b8b9a; display: flex; gap: 16px;">
                    <span>⏱️ {duration}</span>
                    <span>🏋️ {exercises} exercícios</span>
                </div>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 12px; color: #6b6b7b; margin-bottom: 10px;">{date}</div>
                <button style="
                    padding: 10px 24px;
                    background: {'linear-gradient(135deg, #00d4ff, #0099cc)' if active else 'rgba(0,212,255,0.1)'};
                    border: {'none' if active else '1px solid rgba(0,212,255,0.3)'};
                    color: white;
                    border-radius: 24px;
                    font-size: 13px;
                    font-weight: 600;
                    cursor: pointer;
                    box-shadow: {('0 4px 15px rgba(0, 212, 255, 0.3)' if active else 'none')};
                ">{'▶ Iniciar' if active else 'Ver'}</button>
            </div>
        </div>
        """
    
    @staticmethod
    def timer_display(time_str, running=False):
        """Display do timer com efeito de brilho"""
        glow = "text-shadow: 0 0 30px rgba(0, 212, 255, 0.6), 0 0 60px rgba(0, 212, 255, 0.3);" if running else ""
        
        return f"""
        <div style="text-align: center; padding: 32px;">
            <div style="
                font-size: 72px;
                font-weight: 200;
                font-family: 'Courier New', monospace;
                color: #ffffff;
                letter-spacing: 8px;
                {glow}
                transition: all 0.3s;
            ">{time_str}</div>
            <div style="margin-top: 16px; color: {'#00d4ff' if running else '#6b6b7b'}; font-size: 14px;">
                {'⏱️ Treino em andamento...' if running else '⏸️ Timer pausado'}
            </div>
        </div>
        """
    
    @staticmethod
    def stats_grid(items):
        """Grid de estatísticas"""
        stats_html = '<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 20px;">'
        
        for icon, value, label in items:
            stats_html += f"""
            <div style="
                text-align: center;
                padding: 20px;
                background: rgba(255,255,255,0.02);
                border-radius: 16px;
                border: 1px solid rgba(255,255,255,0.05);
            ">
                <div style="font-size: 24px; margin-bottom: 8px;">{icon}</div>
                <div style="font-size: 20px; font-weight: 700; color: #ffffff;">{value}</div>
                <div style="font-size: 11px; color: #6b6b7b; margin-top: 4px; text-transform: uppercase;">{label}</div>
            </div>
            """
        
        stats_html += '</div>'
        return stats_html


# Funções de Gráficos
class Charts:
    
    @staticmethod
    def line_chart(dias, valores, titulo="Progresso", cor="#00d4ff", fill=True):
        """Gráfico de linha estilizado"""
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=dias,
            y=valores,
            mode='lines+markers',
            line=dict(color=cor, width=4),
            marker=dict(
                size=10,
                color=cor,
                line=dict(width=3, color='#0f0f1a'),
                symbol='circle'
            ),
            fill='tozeroy' if fill else None,
            fillcolor=f'rgba{tuple(list(int(cor.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)) + [0.1])}' if fill else None
        ))
        
        fig.update_layout(
            title=dict(
                text=titulo,
                font=dict(size=16, color='#fff'),
                x=0.5,
                xanchor='center'
            ),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=50, b=20),
            xaxis=dict(
                showgrid=False,
                showline=False,
                tickfont=dict(color='#8b8b9a', size=12)
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(255,255,255,0.05)',
                showline=False,
                tickfont=dict(color='#8b8b9a', size=12)
            ),
            height=220,
            hovermode='x unified'
        )
        
        return fig
    
    @staticmethod
    def donut_chart(valor, total, titulo, cor="#00d4ff"):
        """Gráfico de rosca para métricas"""
        fig = go.Figure(data=[go.Pie(
            values=[valor, total - valor],
            hole=0.75,
            marker_colors=[cor, 'rgba(255,255,255,0.05)'],
            textinfo='none',
            hoverinfo='none',
            showlegend=False
        )])
        
        fig.add_annotation(
            text=f"<b>{int((valor/total)*100)}%</b>",
            x=0.5, y=0.5,
            font_size=28,
            font_color='#fff',
            showarrow=False
        )
        
        fig.update_layout(
            title=dict(text=titulo, font=dict(size=14, color='#8b8b9a'), x=0.5),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=0, t=40, b=0),
            height=200
        )
        
        return fig


# Dados Mockados
class MockData:
    USUARIO = {
        "nome": "Igor Silva",
        "plano": "Plano Premium",
        "iniciais": "IS",
        "notificacoes": 2
    }
    
    NUTRICAO_HOJE = {
        "calorias": {"atual": 1850, "meta": 2200},
        "proteina": {"atual": 110, "meta": 150},
        "carbos": {"atual": 220, "meta": 300},
        "gorduras": {"atual": 65, "meta": 100},
        "agua": {"atual": 2.4, "meta": 3.0}
    }
    
    ALIMENTOS = [
        ("🍚", "Arroz Branco", "200g • 1 xícara", 260, False),
        ("🍗", "Frango Grelhado", "150g • Peito", 248, False),
        ("🥚", "Ovos Cozidos", "2 unidades • Grandes", 140, True),
        ("🍎", "Maçã Gala", "1 unidade • Média", 95, False),
        ("🥗", "Salada Verde", "100g • Alface/Tomate", 3

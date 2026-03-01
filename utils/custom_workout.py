# utils/custom_workout.py

CUSTOM_WORKOUT = {
    "casa": {
        "nome": "🏠 Treino em Casa",
        "horario": "06:35 - 07:00",
        "dias": "Segunda a Sexta",
        "foco": "Abdómen e Queima Residual",
        "circuito": [
            ("Escalador (Mountain Climber)", "45 segundos (rápido)", "🔥"),
            ("Prancha Isométrica", "45 segundos (contrair abdómen e glúteo)", "🧘"),
            ("Abdominal Bicicleta", "1 minuto (foco nos oblíquos)", "🚴"),
            ("Elevação de Pernas (Deitado)", "15 repetições (foco na pochete)", "🦵"),
            ("Burpees", "10 repetições (gasto máximo)", "💥")
        ],
        "rodadas": "3 a 4 vezes"
    },
    "ginasio": {
        "Segunda": {
            "nome": "🏋️ Pernas (Foco Quadríceps)",
            "foco": "O maior gasto calórico",
            "exercicios": [
                ("Agachamento (Smith ou Livre)", "3 x 12"),
                ("Leg Press 45º", "3 x 12"),
                ("Cadeira Extensora", "3 x 15 (movimento controlado)"),
                ("Afundo com Halteres", "3 x 10 (cada perna)"),
                ("Panturrilha em pé", "4 x 15")
            ]
        },
        "Terça": {
            "nome": "🏋️ Peito, Ombro e Tríceps",
            "foco": "Membros superiores",
            "exercicios": [
                ("Supino Reto (Máquina ou Halteres)", "3 x 12"),
                ("Desenvolvimento de Ombros (Halteres)", "3 x 12"),
                ("Elevação Lateral", "3 x 15 (foco na técnica)"),
                ("Tríceps Corda na Polia", "3 x 15"),
                ("Tríceps Testa ou Mergulho no banco", "3 x 12")
            ]
        },
        "Quarta": {
            "nome": "🏋️ Costas, Bíceps e Trapézio",
            "foco": "Costas e braços",
            "exercicios": [
                ("Puxada Alta (Lat Pulldown)", "3 x 12"),
                ("Remada Baixa Sentada", "3 x 12"),
                ("Rosca Direta (Barra ou Polia)", "3 x 12"),
                ("Rosca Martelo", "3 x 12"),
                ("Encolhimento de Ombros (Halteres)", "3 x 15")
            ]
        },
        "Quinta": {
            "nome": "🏋️ Posteriores de Coxa e Glúteo",
            "foco": "Posterior e glúteos",
            "exercicios": [
                ("Cadeira Flexora", "3 x 15"),
                ("Stiff com Halteres", "3 x 12 (costas retas)"),
                ("Elevação Pélvica", "3 x 12 (contrair no topo)"),
                ("Cadeira Abdutora", "3 x 20"),
                ("Panturrilha sentado", "4 x 15")
            ]
        },
        "Sexta": {
            "nome": "🔥 Full Body 'Queima Extrema'",
            "foco": "Corpo todo + cardio final",
            "exercicios": [
                ("Agachamento Livre", "3 x 15"),
                ("Flexões de Braço", "3 x máximo"),
                ("Remada com Halteres", "3 x 12"),
                ("Desenvolvimento com Halteres", "3 x 12"),
                ("Caminhada Rápida na Esteira (Inclinação 5%)", "10 minutos finais")
            ]
        }
    },
    "fim_de_semana": {
        "Sábado": {
            "nome": "🧘 Recuperação Ativa",
            "atividades": [
                "30 min de Caminhada leve",
                "Alongamentos de corpo inteiro"
            ]
        },
        "Domingo": {
            "nome": "🌅 Manutenção",
            "atividades": [
                "Vacuum Abdominal em jejum (5 repetições de 15 segundos)",
                "40 min de caminhada ou passeio ativo"
            ]
        }
    },
    "dicas": [
        "💧 Hidratação: 4 litros de água por dia (leve garrafa para o trabalho e ginásio)",
        "⚡ Mounjaro: Se sentir cansaço, ajuste a carga mas mantenha o movimento",
        "🥗 Alimentação: Siga o plano da Pera, Morango e Limão",
        "⏱️ Descanso entre séries: 45 a 60 segundos",
        "🎯 Foco total: pouco tempo, máxima intensidade"
    ]
}

# FitNS Pro

Aplicativo de fitness e nutrição desenvolvido com Streamlit.

## Funcionalidades

- Dashboard com resumo diário (calorias, macros, água)
- Registro de refeições com macros
- Acompanhamento de treinos
- Visualização de progresso de peso

## Como executar

1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute: `streamlit run app.py`

## Estrutura do Projeto

- `app.py`: ponto de entrada
- `config.py`: configurações globais
- `styles.py`: CSS customizado
- `pages/`: páginas da aplicação
- `modules/`: componentes de UI reutilizáveis
- `utils/`: lógica de negócio e persistência
- `data/`: armazenamento de dados em JSON

# MktShare Agrícola

Este projeto tem como objetivo consolidar, transformar e analisar dados de produção agrícola, com foco na soja, em Goiás. 
Ele realiza o processamento e a transformação de dados, gerando relatórios e dashboards interativos que podem ser utilizados para tomada de decisões estratégicas.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

mktshare_agricola/
│
├── input/                   # Dados brutos de entrada
│   ├── Tabela 3.9 - Goias 2021.xlsx
│   ├── Tabela 3.9 - Goias 2022.xlsx
│   ├── Tabela 3.9 - Goias 2023.xlsx
│
├── output/                 # Arquivos gerados (consolidados e transformados)
│
├── scripts/                 # Scripts Python para processamento
│   ├── extract.py           # Consolidação dos dados
│   ├── transform.py         # Transformações de dados (cálculos)
│   ├── dashboard.py         # Dashboard interativo com Streamlit
│
├── main.py                 # Arquivo principal para execução
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação


## Funcionalidades

1. **Extração e Consolidação de Dados**: O script `extract.py` realiza a consolidação dos dados de produção de soja de diferentes anos (2021, 2022, 2023) e gera um arquivo consolidado.
2. **Transformação de Dados**: O script `transform.py` aplica cálculos como a quantidade de sementes necessárias para plantio, considerando a área plantada e a taxa de semeadura.
3. **Dashboard Interativo**: O script `dashboard.py` utiliza o Streamlit para gerar um gráfico interativo que compara a produção de soja por ano, permitindo filtragem por diferentes municípios.
4. **Análise de Mercado**: A análise de dados gerados pode ser utilizada para gerar insights sobre o mercado agrícola, como projeções de produção, comparações entre anos, e mais.

## Requisitos

Certifique-se de ter o Python 3.7 ou superior instalado. O projeto utiliza as seguintes bibliotecas:

- `pandas`
- `openpyxl`
- `plotly`
- `streamlit`
- `matplotlib`
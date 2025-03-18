import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_excel("./output/consolidado_soja_transformado.xlsx")

def gerar_grafico(df):
    fig = px.pie(df, 
                 names='Ano', 
                 values='Quantidade de Sementes (Toneladas)', 
                 title="Distribuição das Quantidades de Sementes de Soja por Ano")
    
    st.plotly_chart(fig)

def app():
    st.title('Dashboard de Sementes de Soja')

    locais = df['Unnamed: 0'].unique()
    local_selecionado = st.selectbox('Escolha o Local', locais)

    df_filtrado = df[df['Unnamed: 0'] == local_selecionado]

    gerar_grafico(df_filtrado)

if __name__ == "__main__":
    app()
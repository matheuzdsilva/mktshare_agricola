import pandas as pd
import os

def calcular_sementes(area_plantada: float, taxa_semeadura: float = 50) -> float:
    try:
        area_plantada = float(area_plantada)
    except ValueError:
        area_plantada = 0
    sementes_kg = area_plantada * taxa_semeadura
    sementes_toneladas = sementes_kg / 1000
    return sementes_toneladas

def aplicar_transformacao(arquivo_entrada: str, arquivo_saida: str):
    try:
        df = pd.read_excel(arquivo_entrada)
        df["Área plantada (Hectares)"] = pd.to_numeric(df["Área plantada (Hectares)"], errors='coerce')
        df["Quantidade de Sementes (Toneladas)"] = df["Área plantada (Hectares)"].apply(calcular_sementes)
        df.to_excel(arquivo_saida, index=False)
        print(f"Transformação concluída! Arquivo salvo em: {arquivo_saida}")
    except Exception as e:
        print(f"Erro ao aplicar transformação: {e}")

if __name__ == "__main__":
    arquivo_entrada = "./output/consolidado_soja.xlsx"
    arquivo_saida = "./output/consolidado_soja_transformado.xlsx"
    
    aplicar_transformacao(arquivo_entrada, arquivo_saida)

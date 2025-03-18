from scripts.extract import consolidar_dados
from scripts.transform import aplicar_transformacao
import os

if __name__ == "__main__":
    pasta_entrada = "./input"
    pasta_saida = "./output"
    arquivo_consolidado = "consolidado_soja.xlsx"
    arquivo_transformado = "consolidado_soja_transformado.xlsx"

    os.makedirs(pasta_saida, exist_ok=True)

    # Etapa 1: Consolidar as planilhas
    consolidar_dados(pasta_entrada, pasta_saida, arquivo_consolidado)

    # Etapa 2: Aplicar transformações no arquivo consolidado
    arquivo_entrada = os.path.join(pasta_saida, arquivo_consolidado)
    arquivo_saida = os.path.join(pasta_saida, arquivo_transformado)
    
    aplicar_transformacao(arquivo_entrada, arquivo_saida)

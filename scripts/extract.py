import pandas as pd
import os

def processar_planilha(arquivo: str, ano: int) -> pd.DataFrame:
    try:
        df = pd.read_excel(arquivo, sheet_name=f"{ano}; Soja (em grão)", skiprows=4)
        df["Ano"] = ano
        return df
    except Exception as e:
        print(f"Erro ao processar {arquivo}: {e}")
        return pd.DataFrame()

def consolidar_dados(pasta_entrada: str, pasta_saida: str, arquivo_saida: str):
    anos = [2021, 2022, 2023]
    arquivos = [f"Tabela 3.9 - Goias {ano}.xlsx" for ano in anos]
    
    dataframes = []
    
    for ano, arquivo in zip(anos, arquivos):
        caminho_arquivo = os.path.join(pasta_entrada, arquivo)
        
        if os.path.exists(caminho_arquivo):
            df = processar_planilha(caminho_arquivo, ano)
            if not df.empty:
                dataframes.append(df)
        else:
            print(f"Arquivo não encontrado: {caminho_arquivo}")
    
    if dataframes:
        df_final = pd.concat(dataframes, ignore_index=True)
        caminho_saida = os.path.join(pasta_saida, arquivo_saida)
        df_final.to_excel(caminho_saida, index=False)
        print(f"Consolidação concluída! Arquivo salvo em: {caminho_saida}")
    else:
        print("Nenhum dado foi consolidado.")

if __name__ == "__main__":
    pasta_entrada = "./input"
    pasta_saida = "./output"
    arquivo_saida = "consolidado_soja.xlsx"
    
    os.makedirs(pasta_saida, exist_ok=True)
    
    consolidar_dados(pasta_entrada, pasta_saida, arquivo_saida)

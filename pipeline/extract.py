import pandas as pd
from pathlib import Path
from utils import get_raw_dir

RAW_DIR = get_raw_dir()

# Lista de arquivos esperados
ARQUIVOS_RAW = {
    "atendimento": "atendimento_raw.csv",
    "clientes": "clientes_raw.csv",
    "compras": "compras_raw.csv",
    "estoque": "estoque_raw.csv",
    "financeiro": "financeiro_raw.csv",
    "fornecedores": "fornecedores_raw.csv",
    "logistica": "logistica_raw.csv",
    "marketing_campanhas": "marketing_campanhas_raw.csv",
    "marketing_performance": "marketing_performance_raw.csv",
    "produtos": "produtos_raw.csv",
    "rh": "rh_raw.csv",
    "vendas": "vendas_raw.csv"
}


def carregar_dados_csv() -> dict[str, pd.DataFrame]:
    """Carrega todos os CSVs da pasta RAW_DIR e retorna um dicionário de DataFrames."""

    dfs = {}

    # 1. Valida existência dos arquivos
    for nome, arquivo in ARQUIVOS_RAW.items():
        caminho = RAW_DIR / arquivo
        if not caminho.exists():
            raise FileNotFoundError(f"Arquivo ausente: {caminho}")

    # 2. Carrega os DataFrames
    for nome, arquivo in ARQUIVOS_RAW.items():
        caminho = RAW_DIR / arquivo
        print(f"→ Carregando: {arquivo}")
        dfs[nome] = pd.read_csv(caminho, encoding="utf-8", sep=",")

    return dfs


if __name__ == "__main__":
    dfs = carregar_dados_csv()
    print("Extração concluída.")

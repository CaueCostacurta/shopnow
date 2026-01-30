# %%
import pandas as pd
import random
from pathlib import Path

# Função para encontrar o diretório raiz do repositório
def find_repo_root(start: Path = Path.cwd()) -> Path:
    p = start.resolve()
    for parent in [p] + list(p.parents):
        if (parent / "README.md").exists() or (parent / ".git").exists():
            return parent
    return p  # fallback: cwd


BASE_DIR = find_repo_root()
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)
metas_raw = RAW_DIR / "metas_vendas_raw.csv"


# %%
meses = pd.period_range("2023-01", "2024-12", freq="M")
categorias = ["Eletrônicos", "Roupas", "Casa", "Beleza"]
canais = ["Site", "App"]

metas = []

for mes in meses:
    for categoria in categorias:
        for canal in canais:
            metas.append({
                "ano_mes": str(mes),
                "categoria_produto": categoria,
                "canal": canal,
                "meta_faturamento": random.randint(200000, 800000)
            })


# %%
df_metas = pd.DataFrame(metas)

#df_metas

# %%
df_metas.to_csv(
    metas_raw,
    index=False,
    encoding="utf-8"
)



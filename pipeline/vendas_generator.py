# %%
import pandas as pd
import random
from faker import Faker
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
raw_out = RAW_DIR / "vendas_raw.csv"


# %%
# Gera o objeto Faker com localidade brasileira
fake = Faker("pt_BR")


## Gera uma lista dicionario e popula ela com dados falsos da bibli. faker para gerar uma tabela de dados 
dados = []

for i in range(5000):
    dados.append({
        "id_venda": i + 1,
        "data_venda": fake.date_between(start_date="-2y", end_date="today"),
        "id_cliente": random.randint(1, 1200),
        "nome_cliente": fake.name(),
        "categoria_produto": random.choice(
            ["Eletrônicos", "Roupas", "Casa", "Beleza"]
        ),
        "valor_venda": round(random.uniform(50, 3500), 2),
        "canal": random.choice(["Site", "App"])
    })

# %%
df_raw = pd.DataFrame(dados)

#df_raw

# %%
df_raw.to_csv(
    raw_out,
    index=False,
    encoding="utf-8"
)



import pandas as pd
import random
from faker import Faker

fake = Faker("pt_BR")

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

df_raw = pd.DataFrame(dados)

df_raw.to_csv(
    "data/raw/vendas_raw.csv",
    index=False,
    encoding="utf-8"
)

# %%
import sys
from pathlib import Path
import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta

# Caminho real do notebook 
NOTEBOOK_DIR = Path.cwd() 

# Sobe até a raiz do projeto (shopnow/) 
ROOT = NOTEBOOK_DIR.parents[1] 

# Adiciona ao sys.path 
if str(ROOT) not in sys.path: sys.path.append(str(ROOT)) 

# Agora sim, pode importar 
from pipeline.utils import find_repo_root, get_raw_dir

# 1. Configuração do ambiente

ROOT = find_repo_root()
RAWDIR = get_raw_dir()



# %%
# 2. Configuração do Faker, Seed e geração dos dados

# Inicializa o Faker e a seed para reprodutibilidade
fake = Faker("pt_BR")
random.seed(42)

# Geração dos dados de vendas
def gerar_vendas(qtd: int = 5000) -> list[dict]:
    """Gera uma lista de dicionários simulando vendas completas."""

    categorias = ["Eletrônicos", "eletronicos", "Roupas", "Casa", "Beleza"]
    canais = ["Site", "SITE", "App", "Aplicativo", "app"]
    marcas = ["Samsung", "Apple", "LG", "Nike", "Adidas", "Genérica"]
    status_pagamento = ["Aprovado", "aprovado", "Recusado", "Pendente"]
    transportadoras = ["Correios", "Jadlog", "Total Express"]
    status_entrega = ["Entregue", "Em trânsito", "Atrasado"]

    vendas = []

    for i in range(qtd):
        data_venda = fake.date_between(start_date="-2y", end_date="today")
        data_envio = fake.date_between(start_date="-2y", end_date="today")

        vendas.append({
            # Identificadores
            "id_venda": i + 1,
            "id_pedido": f"PED-{random.randint(10000, 99999)}",

            # Datas
            "data_venda": data_venda,
            "data_envio": data_envio,

            # Cliente
            "id_cliente": random.randint(1, 1200),
            "nome_cliente": fake.name(),
            "email_cliente": fake.email(),
            "cidade_cliente": fake.city(),
            "estado_cliente": fake.state_abbr(),

            # Produto
            "categoria_produto": random.choice(categorias),
            "produto": fake.word().capitalize(),
            "marca": random.choice(marcas),

            # Valores
            "quantidade": random.randint(1, 5),
            "valor_unitario": round(random.uniform(50, 3500), 2),
            "valor_venda": round(random.uniform(50, 3500), 2),
            "desconto": random.choice([0, 0, 0, 10, 20, 30]),
            "frete": round(random.uniform(0, 120), 2),

            # Canal
            "canal": random.choice(canais),

            # Pagamento
            "forma_pagamento": random.choice(["Crédito", "Débito", "Pix", "Boleto"]),
            "parcelas": random.choice([1, 1, 1, 2, 3, 6, 12]),
            "status_pagamento": random.choice(status_pagamento),

            # Logística
            "transportadora": random.choice(transportadoras),
            "status_entrega": random.choice(status_entrega),
        })

    return vendas


# %%
# 3. Gera o DataFrame de vendas
df_vendas = pd.DataFrame(gerar_vendas(5000))


# %%
# 4. Salva o DataFrame como CSV no diretório de dados brutos
df_vendas.to_csv(
    RAWDIR / "vendas_raw.csv",
    index=False, encoding="utf-8")




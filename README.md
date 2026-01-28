# Projeto de Dados – ShopNow

## Análise de Vendas de um E-commerce com Pipeline ETL e Power BI

1️⃣ Visão Geral do Projeto

O projeto ShopNow simula um pipeline completo de dados, desde a geração de dados brutos (RAW) até a visualização em Power BI, utilizando:

- Python
- CSV
- ETL
- PostgreSQL
- Power BI

O objetivo é reproduzir um cenário real de mercado, onde os dados:

- chegam sujos e inconsistentes
- passam por tratamento e padronização
- são armazenados em um banco analítico
- alimentam um dashboard executivo



2️⃣ Contexto de Negócio

A ShopNow é um e-commerce nacional que vende produtos das categorias:

- Eletrônicos
- Roupas
- Casa
- Beleza

Os canais de venda são:

- Site
- Aplicativo (App)

A diretoria enfrenta dificuldades para responder perguntas básicas de negócio, como:

- Quais categorias geram mais faturamento?
- Qual canal performa melhor?
- Existe sazonalidade nas vendas?
- Quem são os clientes mais valiosos?



3️⃣ Objetivo do Projeto

Construir um pipeline de dados ponta a ponta para:

- Organizar os dados de vendas
- Padronizar informações inconsistentes
- Criar um modelo analítico (Star Schema)
- Disponibilizar os dados no PostgreSQL

Alimentar dashboards no Power BI



4️⃣ Perguntas de Negócio

- Qual o faturamento total da empresa?
- Qual o faturamento por categoria?
- Qual canal gera mais receita?
- Como as vendas evoluem ao longo do tempo?
- Quem são os principais clientes?



5️⃣ Arquitetura do Projeto
shopnow
├── pipelines
│   ├── extract
│   ├── transform
│   └── load
│
├── data
│   ├── raw
│   ├── processed
│   └── trusted
│
├── dashboards
│   └── powerbi
│       └── shopnow_dashboard.pbix
│
├── configs
├── logs
└── README.md

Conceito das camadas

- raw → dados brutos, sem regra de negócio
- processed → dados tratados e padronizados
- trusted → dados analíticos prontos para BI



6️⃣ Geração dos Dados (Extract – RAW)

Os dados são gerados artificialmente em Python, simulando problemas reais como:

- valores em formatos diferentes
- textos não padronizados
- redundância de informações

Exemplo de dados RAW

Campos:

- id_venda
- data_venda
- id_cliente
- nome_cliente
- categoria_produto
- valor_venda
- canal

data/raw/vendas_raw.csv

Importante:
Mesmo sendo sintéticos, os dados são tratados como dados sujos, exatamente como em sistemas reais.



7️⃣ Transformação dos Dados (Transform – ETL)

Nesta etapa ocorre:

- padronização de textos
- ajuste de tipos de dados
- remoção de redundâncias
- modelagem dimensional

📐 Modelo de Dados – Star Schema
📘 Dimensão Cliente

- id_cliente
- nome_cliente

📘 Dimensão Produto

- id_produto
- categoria_produto

📗 Fato Vendas

- id_venda
- data_venda
- id_cliente
- id_produto
- valor_venda
- canal

Os arquivos tratados são salvos em:

data/processed/
├── dim_cliente.csv
├── dim_produto.csv
└── fato_vendas.csv



8️⃣ Carga no Banco de Dados (Load – PostgreSQL)

Após o tratamento, os dados são carregados em um banco PostgreSQL, formando a camada trusted.

📌 Tabelas no banco

- dim_cliente
- dim_produto
- fato_vendas

Essas tabelas são usadas como fonte única da verdade para análises e BI.



9️⃣ Consumo no Power BI

O Power BI se conecta diretamente ao PostgreSQL.

🔗 Relacionamentos

- fato_vendas.id_cliente → dim_cliente.id_cliente
- fato_vendas.id_produto → dim_produto.id_produto

📊 Dashboard inclui:

- Faturamento total
- Faturamento por categoria
- Vendas por canal
- Evolução mensal das vendas
- Top clientes

Arquivo salvo em:

dashboards/powerbi/shopnow_dashboard.pbix



🔟 Principais Insights Esperados

✔ Eletrônicos lideram o faturamento
✔ App apresenta melhor performance que o Site
✔ Existe sazonalidade clara ao longo do ano
✔ Poucos clientes concentram grande parte da receita



1️⃣1️⃣ Boas Práticas Aplicadas

Separação de camadas (raw / processed / trusted)

- ETL desacoplado
- Modelo dimensional
- Banco analítico como fonte do BI
- Pipeline reproduzível
- Arquitetura escalável



1️⃣2️⃣ Possíveis Evoluções do Projeto

- ETL incremental (novas vendas por dia)
- Dimensão tempo
- Logs e monitoramento
- Docker (Postgres + Python)
- Airflow
- Views analíticas no Postgres
- Métricas DAX avançadas
- Testes de qualidade de dados



1️⃣3️⃣ Conclusão

O projeto ShopNow demonstra domínio de:

- Python para dados
- ETL
- Modelagem dimensional
- PostgreSQL
- Power BI
- Arquitetura de dados
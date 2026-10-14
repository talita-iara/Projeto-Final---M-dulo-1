import pandas as pd
import matplotlib.pyplot as plt
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Conectar ao banco de dados
load_dotenv()

ETL_DATABASE_URL = os.getenv("ETL_DATABASE_URL")
engine_etl = create_engine(ETL_DATABASE_URL)

# Ler os dados do PostgreSQL
df = pd.read_sql("SELECT * FROM tratada_vendas", engine_etl)

# Criar a pasta de resultados, se necessario
os.makedirs("resultados", exist_ok=True)

# Converter a data
df["data_venda"] = pd.to_datetime(df["data_venda"])

# 1. Faturamento por filial
faturamento_filial = df.groupby("filial")["valor_total"].sum()
print("Faturamento por filial:")
print(faturamento_filial)

faturamento_filial.plot(kind="bar")
plt.title("Faturamento por filial")
plt.ylabel("Faturamento")
plt.tight_layout()
plt.savefig("resultados/faturamento_por_filial.png")
plt.close()

# 2. Quantidade de vendas por filial
vendas_filial = df["filial"].value_counts()
print("\nQuantidade de vendas por filial:")
print(vendas_filial)

# 3. Faturamento por linha de produto
faturamento_produto = df.groupby("linha_produto")["valor_total"].sum()
print("\nFaturamento por linha de produto:")
print(faturamento_produto)

faturamento_produto.plot(kind="bar")
plt.title("Faturamento por linha de produto")
plt.ylabel("Faturamento")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("resultados/faturamento_por_produto.png")
plt.close()

# 4. Avaliacao media por linha de produto
avaliacao_produto = df.groupby("linha_produto")["avaliacao"].mean()
print("\nAvaliacao media por linha de produto:")
print(avaliacao_produto)

# 5. Forma de pagamento mais utilizada
pagamentos = df["forma_pagamento"].value_counts()
print("\nFormas de pagamento:")
print(pagamentos)

# 6. Valor medio das vendas
print("\nValor medio das vendas:")
print(df["valor_total"].mean())

# 7. Maior venda
print("\nMaior venda:")
print(df.loc[df["valor_total"].idxmax()])

# 8. Dia da semana com mais vendas
df["dia_semana"] = df["data_venda"].dt.day_name()
vendas_dia = df["dia_semana"].value_counts()
print("\nQuantidade de vendas por dia da semana:")
print(vendas_dia)

vendas_dia.plot(kind="bar")
plt.title("Vendas por dia da semana")
plt.ylabel("Quantidade de vendas")
plt.tight_layout()
plt.savefig("resultados/vendas_por_dia_semana.png")
plt.close()

print("\nAnalises concluidas!")

engine_etl.dispose()
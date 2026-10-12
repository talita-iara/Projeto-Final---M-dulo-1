# TRANSFORMAÇÃO DE DADOS

# Importando as bibliotecas
import pandas as pd
import os

# Lendo o arquivo original
caminho = r"data\raw\SuperMarket Analysis.csv"
df_base = pd.read_csv(caminho, sep=",")

# Convertendo a coluna Date para data
df_base["Date"] = pd.to_datetime(
    df_base["Date"],
    format="%m/%d/%Y"
)

# Convertendo a coluna Time para hora
df_base["Time"] = pd.to_datetime(
    df_base["Time"],
    format="%I:%M:%S %p"
).dt.time

# Verificando se existem linhas duplicadas
print("Linhas duplicadas:", df_base.duplicated().sum())

# Verificando se existem dados nulos
print("Valores nulos por coluna:")
print(df_base.isnull().sum())

# Verificando as categorias das colunas
print("Cidades:", df_base["City"].unique())
print("Filiais:", df_base["Branch"].unique())
print("Tipos de cliente:", df_base["Customer type"].unique())
print("Gêneros:", df_base["Gender"].unique())
print("Linhas de produto:", df_base["Product line"].unique())
print("Formas de pagamento:", df_base["Payment"].unique())
#Não será necessário tratar as categorias para padronizar

# Criando a pasta de saída, se necessário
os.makedirs("data/processed", exist_ok=True)

# Salvando a base tratada
df_base.to_csv(
    "data/processed/vendas_tratadas.csv",
    index=False
)

print("Arquivo tratado salvo com sucesso!")
print(df_base.info())
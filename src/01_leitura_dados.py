#Exploração dos dados
#importando as bibliotecas
import pandas as pd

#colunas
"""
'Invoice ID' - número da nota
'Branch' - Filial
'City' - cidade
'Customer type' - tipo de cliente 
'Gender' - gênero
'Product line' - linha de produto
'Unit price' - preço inutário
'Quantity' - qtde
'Tax 5%'- impostos (5%)
'Sales' - vendas
'Date' - data
'Time' -hora
'Payment' - forma de pagamento
'cogs' - custo do produto vendido
gross margin percentage' - margem bruta
'gross income' - lucro bruto
'Rating' - avaliação
"""

#Lendo o arquivo
caminho = r"data\raw\SuperMarket Analysis.csv"
df_base = pd.read_csv(caminho, sep=",")
print(df_base.head(20))

print(df_base.columns.tolist())
print(df_base.info())
"""
Análise:
temos 1000 linhas
17 colunas
Não tenho dados nulos
Tipos: 7 colunas float (decimal)
1 coluna int (inteiro)
9 colunas str (textos)
Possíveis erros:
Coluna date como texto
time como texto
"""
#Resumo de linhas e colunas
print(df_base.shape)

#Estatística descritiva
print(df_base[['Unit price']].describe())
#preço varia de 10,08 a 99,96
print(df_base[['Quantity']].describe())
#quantidade varia de 1 a 10 unidades
print(df_base[['Sales']].describe())
# o valor total varia de 10,68 a 1.042,65
print(df_base[['cogs']].describe())
# varia de 10,17 a 993
print(df_base[['gross margin percentage']].describe())
#mantém o padrão de 4,761905
print(df_base[['gross income']].describe())
# o lucro varia de 0,51 a 49,65
print(df_base[['Rating']].describe())
#a avaliação média é de 6,97 - variando de 4 a 10

#não existem valores negativos


#Confirmando que não existem valores nulos
print(df_base.isnull().sum())

# Verificar identificadores duplicados
print(df_base["Invoice ID"].duplicated().sum())
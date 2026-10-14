# Importando a biblioteca
import pandas as pd


def extracao_produtos():
    """
    Extrai as categorias de produtos e os preços unitários.
    """

    # Lendo o arquivo original
    caminho_csv = "data/raw/SuperMarket Analysis.csv"
    df_produtos = pd.read_csv(caminho_csv)

    # Selecionando as colunas de produto e preço unitário
    df_produtos = df_produtos[["Product line", "Unit price"]]

    # Verificando a quantidade de linhas antes de remover duplicatas
    print("Quantidade de linhas antes:", len(df_produtos))

    # Removendo linhas duplicadas
    df_produtos = df_produtos.drop_duplicates()

    # Organiza os produtos em ordem alfabética
    df_produtos = df_produtos.sort_values(by="Product line")

    # Verificando a quantidade de linhas após remover duplicatas
    print("Quantidade de linhas após:", len(df_produtos))

    # Salvando os dados extraídos
    df_produtos.to_csv(
        "data/raw/produtos_extraidos.csv",
        index=False
    )
    print("\nArquivo salvo com sucesso!")


    # Exibindo os primeiros registros
    print("\nDados extraídos:")
    print(df_produtos.head(10))

    return df_produtos


if __name__ == "__main__":
    df_produtos = extracao_produtos()
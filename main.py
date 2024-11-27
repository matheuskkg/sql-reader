import pandas as pd

df = pd.read_excel('Planilha_de_dados_P2_BD_Tarde.xlsx')

#INSERT categorias
""" categorias = []
id = 1
for index, row in df.iterrows():
    if row['Categoria'] not in categorias:
        categorias.append(row['Categoria'])
        print(f"INSERT INTO categorias(cat_id, cat_nome) VALUES({id}, '{row['Categoria']}');")
        id = id + 1 """

#INSERT produtos
""" produtos = []
id = 1
for index, row in df.iterrows():
    if row['Produto'] not in produtos:
        produtos.append(row['Produto'])
        print(f"INSERT INTO produtos(prd_id, prd_nome, prd_preco, categorias_cat_id) VALUES({id}, '{row['Produto']}', {row['Preço']}, (SELECT cat_id FROM categorias WHERE cat_nome = '{row['Categoria']}'));")
        id = id + 1 """

#INSERT vendas
""" for index, row in df.iterrows():
    timestamp = pd.to_datetime(row['Data de compra'])
    data = timestamp.strftime('%d/%m/%Y')    

    print(f"INSERT INTO vendas (ven_id, ven_data) VALUES({index+1}, TO_DATE('{data}', 'DD/MM/YYYY'));") """

#INSERT vendas_produtos
""" for index, row in df.iterrows():
    valor = float(row['Valor Total'])
    valor = f"{valor:.2f}"

    print(f"INSERT INTO vendas_produtos(vendas_ven_id, produtos_prd_id, quantidade, valor_total) VALUES({index+1}, (SELECT prd_id FROM produtos WHERE prd_nome = '{row['Produto']}'), {row['Quantidade']}, {valor});") """
import pandas as pd
import os

base_dir = os.path.dirname(__file__)

df = pd.read_csv(os.path.join(base_dir, "../data/vendas_ecommerce.csv"))
#print(df)

#cinco primeiro itens da lista

"""cabecario = df.head();
print(cabecario)"""

#ultimos 5 da lista

"""ultimas = df.tail(n=10)
print(ultimas)"""

#uma amostra aleatoria

'''amostra = df.sample(10)
print(amostra)'''

#olha os atributos da tabela, como quantidade de linhas e colunas

'''atributo = df.shape
print(atributo)'''

#retonar todas as colunas no arquivo

'''colunas = df.columns
print(colunas)'''

#aqui retornar os indices

'''indices = df.index
print(indices)'''


'''info = df.info(memory_usage='deep')
print(info)'''

#uma serie que mostra os valores de cada campo e coluna
#print(df.dtypes['categoria'])

# SELECT * FROM df
print(df)

# SELECT pedido_id FROM df
print(df[["pedido_id"]])

# SELECT pedido_id, status FROM df LIMIT 5
print(df[["pedido_id", "status"]].tail(5))


# SELECT pedido_id, status, cliente
# FROM df
# LIMIT 5

print(df[["pedido_id", "status", "cliente"]].head(5))

colunas = list(df.columns)
colunas.sort()
print(colunas)

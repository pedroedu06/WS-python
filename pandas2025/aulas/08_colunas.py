import pandas as pd
import os

base_dir = os.path.dirname(__file__)

df = pd.read_csv(os.path.join(base_dir, "../data/funcionarios_empresa.csv"))
'''print(df.shape)
print(df.info(memory_usage='deep'))
print(df.dtypes)'''

"""a chave desse dicionario e nome antigo da coluna, e o valor associado vai ser o nome novo"""

"""df.rename(columns={"horas_extras_mes": "hrsExtras"}, inplace=True)
print(df)"""

print(df[["func_id"]])
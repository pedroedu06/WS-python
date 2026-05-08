import pandas as pd
import os

base_dir = os.path.dirname(__file__)

df = pd.read_csv(os.path.join(base_dir, "../data/vendas_ecommerce.csv"))

print(df)

#df.to_csv("vendas_ecommerce.csv", index=False)
#df.to_json("vendas_ecommerce.json", index=False)
#df_2 = pd.read_json('vendas_ecommerce.json')
#print(df_2)
#df = pd.read_csv("vendas_ecommerce.csv", sep=";")
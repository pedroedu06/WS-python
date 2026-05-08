import pandas as pd
import os

base_dir = os.path.dirname(__file__)

df = pd.read_csv(os.path.join(base_dir, "../data/vendas_ecommerce.csv"))

exemplo = pd.DataFrame(
    {
        "nome": ["joao", "maria", "jose"],
        "idade": [32, 42, 12],
        "uf": ['sp', "pa", 'rj']
    }
)

print(exemplo['idade'] >= 18)
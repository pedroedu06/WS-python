

import pandas as pd

idades = [
    3, 7, 12, 15, 18, 21, 25, 
    24, 27, 31, 34, 38, 42,
    47, 53, 58, 61, 66, 72, 
]

series_idade = pd.Series(idades)
#print(series_idade)

media_idades = series_idade.mean()
print("media das idades: ", media_idades)

variancia_idades = series_idade.var()
print("variancia idades: ", variancia_idades)
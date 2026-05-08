import pandas as pd

idades = [
    42, 33, 38, 18, 31, 39, 66,
    24, 48, 15, 27, 27, 38,
    22, 25, 21, 40, 34, 25
]

indexs = [
    "Carlos", "Ana", "Roberto", "Julia",
    "Fernando", "Larissa", "Marcelo",
    "Bianca", "Ricardo", "Vanessa", "Diego",
    "Tatiane", "Rodrigo", "Clara", "Paulo",
    "Aline", "Bruno", "Renata", "Tais" 
]


series_idade = pd.Series(idades, index=indexs)


series_idade = series_idade.sort_values()
"""Loc voce navega pelos indexs ja o iloc voce navega pela lista! 
    (direto pelas listas tambem funciona)
"""
print(series_idade.loc["Bruno"])
print(series_idade.iloc[:3])

#print(series_idade.iloc[1])
#print(series_idade.iloc[:8])
#print(series_idade.iloc[::-1])
import pandas as pd

idades = [
    42, 33, 38, 18, 31, 39, 66,
    24, 48, 15, 27, 27, 38,
    22, 25, 21, 40, 34, 25
]

nomes = [
    "Carlos", "Ana", "Roberto", "Julia",
    "Fernando", "Larissa", "Marcelo",
    "Bianca", "Ricardo", "Vanessa", "Diego",
    "Tatiane", "Rodrigo", "Clara", "Paulo",
    "Aline", "Bruno", "Renata", "Tais" 
]

#criacao de series
series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

#data frame

df = pd.DataFrame()
df["idades"] = series_idades
df['nomes'] = nomes
#print(df)

#pegar a idade da ultima pessoa do Dataframe
print(df.iloc[-1]["idades"])

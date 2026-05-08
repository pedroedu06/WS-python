import pandas as pd

url = "https://perfildaindustria.portaldaindustria.com.br/ranking"
dfs = pd.read_html(url)
print(dfs)
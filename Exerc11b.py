import pandas as pd

questao_11b = pd.read_csv("https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv", sep=',')

questao_11b_filtrado = questao_11b[(questao_11b['Genre'] == 'Action') | (questao_11b['Genre'] == 'Shooter') | (questao_11b['Genre'] == 'Platform')]

print(questao_11b_filtrado.groupby(['Publisher'])['Global_Sales'].sum().sort_values(ascending=False).head(3))
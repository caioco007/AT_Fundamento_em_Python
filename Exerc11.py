import pandas as pd

questao_11a = pd.read_csv("https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv", sep=',')

questao_11a_filtrado = questao_11a[(questao_11a['Genre'] == 'Action') | (questao_11a['Genre'] == 'Shooter') | (questao_11a['Genre'] == 'Platform')]

print(questao_11a_filtrado['Publisher'].value_counts().head(3))
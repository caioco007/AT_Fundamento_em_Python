import pandas as pd

questao_10a = pd.read_csv("https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv", sep=',')

questao_10a_filtrado = questao_10a[(questao_10a['Year'] >= 2001) & ((questao_10a['Sport'] == 'Curling') | (questao_10a['Sport'] == 'Skating') | (questao_10a['Sport'] == 'Skiing') | (questao_10a['Sport'] == 'Ice Hockey'))
             & (questao_10a['Medal'] == 'Gold') & ((questao_10a['NOC'] == 'NOR') | (questao_10a['NOC'] == 'SUI') | (questao_10a['NOC'] == 'DEN'))]

print(questao_10a_filtrado.groupby(['NOC'])['Medal'].count())
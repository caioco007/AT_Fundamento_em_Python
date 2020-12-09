import pandas as pd

questao_11d = pd.read_csv("https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv", sep=',')

questao_11d_filtrado1 = questao_11d[(questao_11d['Year_of_Release'] >= 2007)  & ((questao_11d['Genre'] == 'Action'))]
questao_11d_filtrado2 = questao_11d[(questao_11d['Year_of_Release'] >= 2007)  & ((questao_11d['Genre'] == 'Shooter'))]
questao_11d_filtrado3 = questao_11d[(questao_11d['Year_of_Release'] >= 2007)  & ((questao_11d['Genre'] == 'Platform'))]

acao=questao_11d_filtrado1.groupby(['Publisher'])['JP_Sales'].sum().sort_values(ascending=False).head(1)
tiro=questao_11d_filtrado2.groupby(['Publisher'])['JP_Sales'].sum().sort_values(ascending=False).head(1)
plataforma =questao_11d_filtrado3.groupby(['Publisher'])['JP_Sales'].sum().sort_values(ascending=False).head(1)

df = pd.concat([acao, tiro, plataforma], keys=['Action', 'Shooter', 'Platform'], names=['Gêneros ', 'Marcas'])

print(df)
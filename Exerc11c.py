import pandas as pd

questao_11c = pd.read_csv("https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv", sep=',')

questao_11c_filtrado1 = questao_11c[(questao_11c['Year_of_Release'] >= 2007)  & ((questao_11c['Genre'] == 'Action'))]
questao_11c_filtrado2 = questao_11c[(questao_11c['Year_of_Release'] >= 2007)  & ((questao_11c['Genre'] == 'Shooter'))]
questao_11c_filtrado3 = questao_11c[(questao_11c['Year_of_Release'] >= 2007)  & ((questao_11c['Genre'] == 'Platform'))]

acao=questao_11c_filtrado1['Publisher'].value_counts().head(1)
tiro=questao_11c_filtrado2['Publisher'].value_counts().head(1)
plataforma =questao_11c_filtrado3['Publisher'].value_counts().head(1)

df = pd.concat([acao, tiro, plataforma], keys=['Action', 'Shooter', 'Platform'], names=['Gêneros ', 'Marcas'])

print(df)
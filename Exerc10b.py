import pandas as pd

questao_10b = pd.read_csv("https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv", sep=',')

resposta = questao_10b.groupby(['NOC', 'Sport', 'Year', 'City'])['Medal'] \
            .value_counts() \
            .reset_index(name='Medal Count')
print(resposta)

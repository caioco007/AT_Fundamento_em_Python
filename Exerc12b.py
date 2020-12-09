import requests
from bs4 import BeautifulSoup

url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"
requisicao = requests.get(url)

# Testando se a conexão funcionou
if requisicao.status_code != 200:
  requisicao.raise_for_status()

#requisicao.encoding = 'utf-8' # Mudar o enconding (acentuação)
html = requisicao.text
soup = BeautifulSoup(html, "html")

titulo = []
linhas = []
for div_prev in soup.find_all('div', class_='tabela'):
    for div_titulo in div_prev.find_all('div', class_='titulo'):
        titulo.append(div_titulo.text.replace('\n','//')[2:-2].split('//'))

        for div_linha in div_prev.find_all('div', class_='linha'):
            linhas.append(div_linha.text.replace('\n','//')[2:-2].split('//'))


print('Estados da Região Centro-Oeste')
sigla = input("Digite a Sigla de um estado: ")


encontrado = False

for linha in linhas:
    if sigla.upper() in linha[0]:
        encontrado = True
        print(linha)
        break
    else:
        encontrado = False

if not encontrado:
    print("Estado não encontrado...")
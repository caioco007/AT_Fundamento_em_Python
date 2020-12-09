import requests
import re
from bs4 import BeautifulSoup

url = "http://brasil.pyladies.com/about"
requisicao = requests.get(url)

# Testando se a conexão funcionou
if requisicao.status_code != 200:
  requisicao.raise_for_status()

#requisicao.encoding = 'utf-8' # Mudar o enconding (acentuação)
html = requisicao.text
soup = BeautifulSoup(html, "html")

texto = []
for div_prev in soup.find_all('p', class_='about-text'):
  texto.append(div_prev.text.replace('\n', "").split())


palavras = []
for listas in texto:
    palavras += listas

dicionario = {}
for x in palavras:
    letra = re.sub(u'[^a-zA-Z0-9àáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', x).lower()

    if letra in dicionario:
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1

cont = 0
print("Palavras que aparecem apenas uma vez:")
for x, qtd in dicionario.items():
    if qtd == 1:
        cont += 1
        print(x)
print("Total ded palavras: ",cont)
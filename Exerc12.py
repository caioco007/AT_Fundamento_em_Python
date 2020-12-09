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
  print(div_prev.text)
import requests
from bs4 import BeautifulSoup

url = "http://brasil.pyladies.com/about"
requisicao = requests.get(url)

# Testando se a conexão funcionou
if requisicao.status_code != 200:
  requisicao.raise_for_status()

#requisicao.encoding = 'utf-8' # Mudar o enconding (acentuação)
html = requisicao.text
soup = BeautifulSoup(html, "html")

total=0
palavras = []
for div_prev in soup.find_all('p', class_='about-text'):
  total+=div_prev.text.lower().count(' ladies ')
print(total)
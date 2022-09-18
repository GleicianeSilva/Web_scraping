from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.wyden.com.br/unifbv")
bs = BeautifulSoup(html, 'html.parser')


linhas = bs.find_all('div', {'class':'container'})[0]
dados = linhas.find_all('li', {'class': 'leaf depth-4'})
for dado in dados:
    print(dado.text)
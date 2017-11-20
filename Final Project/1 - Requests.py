"""
Richiesta del contenuto html di un sito web.
"""
#pip3 install requests
import requests

response = requests.get('https://it.wikipedia.org/wiki/Pagina_principale')
#print(response.text)
#print(type(response.text))

"""
Vogliamo manipolare l'html ottenuto (come str) dalla request tramite una nuova
libreria html5lib
"""

html = response.text

#pip3 install beautifulsoup4
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

print(soup.title)



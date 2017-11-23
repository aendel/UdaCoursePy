import requests
from bs4 import BeautifulSoup

def find_first_link(url):
    #usiamo la libreria request per ottenere un oggetto dall'url
    response = requests.get(url)
    #response.text ci ritorna l'html
    html = response.text
    #sfruttiamo la libreria BeautifulSoup per leggere l'html
    soup = BeautifulSoup(html,"html.parser")

    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            first_relative_link = element.find("a", recursive=False).get('href')
            break
        
    if first_relative_link :
        return str(first_relative_link)
    else:
        return None

for i in range(50):
    print(find_first_link('https://it.wikipedia.org/wiki/Speciale:PaginaCasuale'))

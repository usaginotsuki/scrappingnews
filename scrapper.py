import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from title-news import sacarTitulo

def sacarLinks(url):
    # Getting the webpage, creating a Response object.
    response = requests.get(url)

    # Extracting the source code of the page.
    data = response.text

    # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
    soup = BeautifulSoup(data, 'lxml')

    # Extracting all the <a> tags into a list.
    tags = soup.find_all('a')

    # Extracting URLs from the attribute href in the <a> tags.
    for tag in tags:
        url = (urlparse(tag.get('href')))
        path = url.path
        if (
        url.netloc) == 'elmercio.com' and path != '/internacional/' and path != '' and path != '/?s=' and path != '/politica/' and path!='/sociedad/' and path!='/necflis/' and path!='/deportes/':
            tags = (tag.get('href'))
            print(tags)


for i in range(2, 4):
    (sacarLinks("https://elmercio.com/politica/page/" + str(i)))

sacarTitulo(https://elmercio.com/jorge-yunda-abandona-alcaldia-por-presidencia-el-nacional/)

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def sacarTitulo(url):
    #url="https://elmercio.com/jorge-yunda-abandona-alcaldia-por-presidencia-el-nacional/"
    # Getting the webpage, creating a Response object.
    response = requests.get(url)

    # Extracting the source code of the page.
    data = response.text

    # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
    soup = BeautifulSoup(data, 'lxml')

    # Extracting all the <a> tags into a list.
    tags = soup.find('h1',text=True)
    titulo=tags.text
    print(titulo)

    noticia=''
    notas= soup.find_all('p',text=True)
    for nota in notas:
        notas=nota.text

        if notas!= "Public collection title" and notas!= "Private collection title" and notas!= "Here you'll find all collections you've created before." and notas!="\nEnter your account data and we will send you a link to reset your password.	" and notas!=' To use social login you have to agree with the storage and handling of your data by this website.':
            noticia=noticia+notas

    print(noticia)


import requests
url = 'https://www.elcomercio.com/'
elcomercio = requests.get(url)
elcomercio
elcomercio.status_code
print(elcomercio.text)

elcomercio.content
elcomercio.headers
elcomercio.request.headers
elcomercio.request.method
elcomercio.request.url
from bs4 import BeautifulSoup
s = BeautifulSoup(elcomercio.text,'lxml')
type(s)
print(s.prettify())
lassecciones = s.find('div',attrs={'class':'container header-menu'}).find_all('li',)
# soup = BeautifulSoup(page.content, 'html.parser')
# project_href = [i['href'] for i in soup.find_all('a', href=True) if i['href'] != "#"]



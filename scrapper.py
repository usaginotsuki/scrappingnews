import requests
from selenium import webdriver
from bs4 import BeautifulSoup

URL = 'https://elmercio.com/politica/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
project_href = [i['href'] for i in soup.find_all('a', href=True)]
print(project_href)

for i in range(2,4):
    URL = 'https://elmercio.com/politica/page'+str(i)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    project_href = [i['href'] for i in soup.find_all('a', href=True)]
    print(project_href)

URL = 'https://elmercio.com/sociedad/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
project_href = [i['href'] for i in soup.find_all('a', href=True)]
print(project_href)

for i in range(2,3):
    URL = 'https://elmercio.com/sociedad/'+str(i)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    project_href = [i['href'] for i in soup.find_all('a', href=True)]
    print(project_href)

URL = 'https://elmercio.com/internacional/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
project_href = [i['href'] for i in soup.find_all('a', href=True)]
print(project_href)

for i in range(2,3):
    URL = 'https://elmercio.com/internacional/'+str(i)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    project_href = [i['href'] for i in soup.find_all('a', href=True)]
    print(project_href)
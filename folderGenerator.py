import os
from bs4 import BeautifulSoup
import requests

path = os.getcwd()

url = 'https://projecteuler.net/archives'
page = requests.get(url)
html = page.text

soup = BeautifulSoup(html,'html.parser')
table = soup.find('table')
rows = table.find_all('tr')

for i in range(1, len(rows)):
    id = '{0:03}'.format(int(rows[i].find('td', {'class' : 'id_column'}).contents[0]))
    title = rows[i].find('a').contents[0]

    newFolderPath = path + f'\{id} - {title}'

    if not os.path.exists(newFolderPath):
        os.mkdir(newFolderPath)
        open(newFolderPath + '\main.py', 'a').close()
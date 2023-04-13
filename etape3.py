import requests
from bs4 import BeautifulSoup 
import numpy
import pandas

#### Étape 3 : Extraire toutes les données des produits d’une catégorie ####

url = 'http://books.toscrape.com/'

response = requests.get(url)

if response.ok:
    links = []
    datapage = BeautifulSoup(response.text, 'lxml')
    sidedivcat = datapage.find('div', {'class':'side_categories'})
    dbs =  sidedivcat.find_all('li')
    for db in dbs:
        a = db.find('a')
        link = a['href']
        links.append(link)
        print(links)
        ####
        links.append('http://books.toscrape.com/' + link)

    print(links)




        

    



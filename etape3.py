import requests
from bs4 import BeautifulSoup 
import csv
import os
from functions import headersArray, modifiedLink

#### Étape 3 : Extraire toutes les données des produits d’une catégorie ####

url = 'https://books.toscrape.com/catalogue/category/books/art_25/index.html'

response = requests.get(url)

booksdata = []

if response.ok:
    links = []
    datapage = BeautifulSoup(response.text, 'lxml')
    singlebooklinks = datapage.find_all('h3')
    
    for singlebooklink in singlebooklinks:
      
        a = singlebooklink.find('a')
        modifiedLink(a)
        link = a['href']
        truncatelink = link.replace('../../..', 'catalogue')
        links.append('http://books.toscrape.com/' + truncatelink)
        for link in links:
            url = link.strip()
            response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'lxml')
            tds = soup.find_all('td')
            singlebookdata = []
        

            for td in tds:
                singlebookdata.append(td.text)
            data = dict(zip(headersArray, singlebookdata))
            booksdata.append(data)

with open('etape3.csv', 'w', newline='') as csvfile:
    fieldnames = headersArray
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for book in booksdata:
        writer.writerow(book)


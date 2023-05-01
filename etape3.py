import requests
from bs4 import BeautifulSoup 
import csv
import os
import functions
from functions import headersArray

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
    links = functions.catalogueLink(a)
    for link in links:
        singlebookdata = functions.retreiveAllTds(link)
    data = dict(zip(headersArray, singlebookdata))
    booksdata.append(data)

    fileNameForCsv = 'step3-csv-file'
    functions.generateCsv(fileNameForCsv, booksdata)


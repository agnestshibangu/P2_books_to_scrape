import requests
from bs4 import BeautifulSoup 
import csv
import os
import functionsOpti
import time
from functions import headersArray

timeStart = time.time()

#### Étape 3 : Extraire toutes les données des produits d’une catégorie ####
#### optimisée avec concurrent.futures ####

url = 'https://books.toscrape.com/catalogue/category/books/art_25/index.html'

response = requests.get(url)

booksdata = []

if response.ok:
    links = []
    datapage = BeautifulSoup(response.text, 'lxml')
    
singlebooklinks = datapage.find_all('h3')
    
for singlebooklink in singlebooklinks:
    a = singlebooklink.find('a')
    links =  functionsOpti.catalogueLink(a)
    for link in links:
        singlebookdata =  functionsOpti.retreiveAllTds(link)
    data = dict(zip(headersArray, singlebookdata))
    booksdata.append(data)

    fileNameForCsv = 'OPTI-step3-csv-file'
    functionsOpti.generateCsv(fileNameForCsv, booksdata)

timeFinish = time.time() - timeStart
print("temps d'execution :", timeFinish)

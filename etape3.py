import requests
from bs4 import BeautifulSoup 
import csv
import os
import functions
import time
from functions import headersArray

timeStart = time.time()

titleFile = functions.Horodatage() 

#### Étape 3 : Extraire toutes les données des produits d’une catégorie ####

path = 'STEP3/'
os.mkdir(path) 

url = 'https://books.toscrape.com/catalogue/category/books/sequential-art_5/page-1.html'

response = requests.get(url)

booksdata = []

if response.ok:
    links = []
    datapage = BeautifulSoup(response.text, 'lxml')


singlebooklinks = datapage.find_all('h3')
    
for singlebooklink in singlebooklinks:
    a = singlebooklink.find('a')
    links = functions.catalogueLink(a,links)
    for link in links:
        singlebookdata = functions.retreiveAllTds(link)
    data = dict(zip(headersArray, singlebookdata))
    booksdata.append(data)

    fileNameForCsv = path + titleFile + '-SingleCategoryBookData-file'
    functions.generateCsv(fileNameForCsv, booksdata)



    
# if datapage.find('li', {'class': 'next'}):  
#     pageCountTag = datapage.find('li', {'class': 'current'}).text.strip()
#     print(pageCountTag)
#     pageCountValue = pageCountTag[-1]
#     print(pageCountValue)

def clickNextLink():
    if datapage.find('li', {'class': 'next'}):
        next = BeautifulSoup(response.text, 'lxml').find('li', {'class': 'next'})
        NextA = next.find('a')
        NextAHref = NextA['href']
        nextLink = 'https://books.toscrape.com/catalogue/category/books/sequential-art_5/' + NextAHref
        print(nextLink)
        responseNext = requests.get(nextLink)
        if responseNext.ok:
            nextNext =  BeautifulSoup(responseNext.content, 'lxml').find('li', {'class': 'next'})
            print(nextNext)
            NextA = next.find('a')
            NextAHref = NextA['href']
            nextLink = 'https://books.toscrape.com/catalogue/category/books/sequential-art_5/' + NextAHref
            print(nextLink)            

clickNextLink()


import requests
from bs4 import BeautifulSoup 
import csv
import os
import functions
from functions import headersArray


print(headersArray)


titleFile = functions.Horodatage() 

#### Étape 3 : Extraire toutes les données des produits d’une catégorie ####

path = 'DATA/STEP3/'
os.mkdir(path) 

url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
response = requests.get(url)

booksdata = []
singlebooklinks = []

if response.ok:
    links = []
    datapage = BeautifulSoup(response.text, 'lxml')

#### functions to loop through all the pages of a category ####
if datapage.find('li', {'class': 'next'}):
    urlAllBooks = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
    if url != urlAllBooks:
        print('//////////// CETTE CATEGORIE A PLUSIEURS PAGES ///////////////')
        functions.clickNextLink(singlebooklinks, url)
        #print(singlebooklinks)
else:
    print('/////////// CETTE CATEGORIE N A QU UNE PAGE /////////////////')
    singlebooklinks = datapage.find_all('h3')
    #print(singlebooklinks)

            
#################################################################

print(singlebooklinks)

for singlebooklink in singlebooklinks:
    a = singlebooklink.find('a')
    links = functions.catalogueLink(a,links)
    for link in links:
        #singlebookdata = functions.retreiveAllTds(link, currentCategoy)
        singlebookdata = functions.retreiveAllTds(link)
    data = dict(zip(headersArray, singlebookdata))
    booksdata.append(data)

    fileNameForCsv = path + titleFile + '-SingleCategoryBookData-file'
    functions.generateCsv(fileNameForCsv, booksdata)


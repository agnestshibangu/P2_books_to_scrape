import requests
from bs4 import BeautifulSoup 
import csv
import os
import functions
from functions import headersArray

titleFile = functions.Horodatage() 

#### Étape 3 : Extraire toutes les données des produits d’une catégorie ####

path = 'STEP3/'
os.mkdir(path) 

url = 'https://books.toscrape.com/catalogue/category/books/sequential-art_5/page-1.html'
response = requests.get(url)

booksdata = []
singlebooklinks = []

if response.ok:
    links = []
    datapage = BeautifulSoup(response.text, 'lxml')

#### functions to loop through all the pages of a category ####

functions.clickNextLink(singlebooklinks, url)
            
#################################################################

# print(singlebooklinks)

# for singlebooklink in singlebooklinks:
#     a = singlebooklink.find('a')
#     links = functions.catalogueLink(a,links)
#     for link in links:
#         singlebookdata = functions.retreiveAllTds(link)
#     data = dict(zip(headersArray, singlebookdata))
#     booksdata.append(data)

#     fileNameForCsv = path + titleFile + '-SingleCategoryBookData-file'
#     functions.generateCsv(fileNameForCsv, booksdata)



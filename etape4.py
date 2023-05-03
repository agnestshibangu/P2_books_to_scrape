import requests
from bs4 import BeautifulSoup 
import numpy
import pandas
import time
import os
import functions
from functions import headersArray
from functions import currentDate

path = './blabka/'
os.mkdir(path)
 
url = 'http://books.toscrape.com/'

response = requests.get(url)

booksdata = []

if response.ok:
    linkscategory = []
    categoryName = []
    datapage = BeautifulSoup(response.text, 'lxml')
    sidedivcat = datapage.find('div', {'class':'side_categories'})
    # fonction pour extraire npm de la categorie
    dbs =  sidedivcat.find_all('li')
    for db in dbs:
        a = db.find('a')
        linkcategory = a['href']
        linkscategory.append('http://books.toscrape.com/' + linkcategory) # generating links for each CATEGORY
    #print(linkscategory)

### on strip chaque catégorie et on liste chaque livre, on transforme le titre de chaque livre en url

for linkcategory in linkscategory:
    url = linkcategory.strip()
    response = requests.get(url)
    if response.ok:
        links = []
        books = []
        datapage = BeautifulSoup(response.text, 'lxml') # single CATEGORY page
        titleCat = datapage.find('h1').text
        print(titleCat)
        
        singlebooklinks = datapage.find_all('h3') # retrieve all book titles from a category
                    
        for singlebooklink in singlebooklinks:
            a = singlebooklink.find('a')
        #     link = a['href']
        #     #global truncatelink
        #     truncatelink = link.replace('../../..', 'catalogue')
        #     links.append('http://books.toscrape.com/' + truncatelink)
        # print(links)
            links = functions.catalogueLink(links,a)

        '''
        for link in links:
            singlebookdata = functions.retreiveAllTds(link)
        data = dict(zip(headersArray, singlebookdata))
        booksdata.append(data)

        fileNameForCsv = 'step3-csv-file'
        functions.generateCsv(fileNameForCsv, booksdata)
        '''

        
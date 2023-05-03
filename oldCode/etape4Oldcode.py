import requests
from bs4 import BeautifulSoup 
import numpy
import pandas
import csv
import os
import functions
from functions import headersArray
from functions import currentDate

#### Étape 3 : Extraire tout les produits de toutes les catégorie ###
#### convention de nommage, plusieurs fichiers avec intitulé catégorie ####


path = './blabka/'
os.mkdir(path)

### data d'un seul item pour récuperer les headers pour pouvoir construire le csv ###

url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
response = requests.get(url)
data = BeautifulSoup(response.text, 'lxml') 

headersArray = []

headers = data.find_all('th')
for header in headers:
    headersArray.append(header.text)
print(headersArray)

### 

url = 'http://books.toscrape.com/'

### récupérer toutes les catégories depuis la page d'acceuil du site pour en faire des urls ###

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
            link = a['href']
            truncatelink = link.replace('../../..', 'catalogue')
            links.append('http://books.toscrape.com/' + truncatelink)
        print(singlebooklink)


        for link in links:
            url = link.strip()
            response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'lxml')


            tds = soup.find_all('td')
            singlebookdata = []

            for td in tds:
                singlebookdata.append(td.text)

            data = singlebookdata
            data = dict(zip(headersArray, singlebookdata))
            booksdata.append(data)
            #print(data)
        print(booksdata)

        fileNameForCsv = path + titleCat
        functions.generateCsv(fileNameForCsv, booksdata)





'''
# on strip le data pour chaque livre
for link in links:
    url = link.strip()
    response = requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')

    tds = soup.find_all('td')
    singlebookdata = []

    for td in tds:
        singlebookdata.append(td.text)

    data = singlebookdata
    data = dict(zip(headersArray, singlebookdata))
    booksdata.append(data)
    #print(data)
    #print(booksdata)
'''



### on strip le data de chaque livre

        # for link in links:
        #     url = link.strip()
        #     response = requests.get(url)age = 23

        # if response.ok:
        #     soup = BeautifulSoup(response.text, 'lxml')
        #     tds = soup.find_all('td')
        #     singlebookdata = []

        #     for td in tds:
        #         singlebookdata.append(td.text)
        #     data = singlebookdata
        #     data = dict(zip(headersArray, singlebookdata))
        #     booksdata.append(data)
        # print(booksdata)

        # with open('etape4.csv', 'w', newline='') as csvfile:
        #     fieldnames = headersArray
        #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #     writer.writeheader()
        #     for book in booksdata:
        #         writer.writerow(book)

            






        

    

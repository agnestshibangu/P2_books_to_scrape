import requests
from bs4 import BeautifulSoup 
#import numpy
#import pandas
import csv
import datetime
import os


x = datetime.datetime.now()
print(x.year)
print(x.month)
print(x.day)
year = str(x.year)
month = str(x.month)
day = str(x.day)
currentDate = year + '-' + month + '-' + day

# create a folder


path = './' + currentDate + '/'
os.mkdir(path)

#### si le dossier image n'existe pas, on le créé ####

path = './images/'
if not os.path.exists(path):
    os.makedirs(path)


#### Étape 4 : Extraire tout les produits de toutes les catégorie ###
#### convention de nommage, plusieurs fichiers avec intitulé catégorie ####


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

if response.ok:
    linkscategory = []
    linkCategoryName = []
    categoriesNameArray = []
    datapage = BeautifulSoup(response.text, 'lxml')
    sidedivcat = datapage.find('div', {'class':'side_categories'})
    # fonction pour extraire npm de la categorie

    dbs =  sidedivcat.find_all('li')
    for db in dbs:
        a = db.find('a')
        singleCategoryName = a.text
        linkcategory = a['href']
        linkscategory.append('http://books.toscrape.com/' + linkcategory) # generating links for each CATEGORY
        categoriesNameArray.append(singleCategoryName.strip()) # extract category name 
    print('************ CATEGORY NAMES ARRAY *************')
    print(categoriesNameArray)

### on strip chaque catégorie et on liste chaque livre, on transforme le titre de chaque livre en url

for linkcategory in linkscategory:
    url = linkcategory.strip()
    response = requests.get(url)
    if response.ok:
        links = []
        books = []
        datapage = BeautifulSoup(response.text, 'lxml') # single CATEGORY page
        titleCat = datapage.find('h1').text
        print('/////////////////////////////////////////////////')

        currentCategory = 'null' 

        globals()['currentCategory'] = titleCat
        print('The current category is:', currentCategory)
        currentCategoryArray = []
        booksdata = []
               
        # retrieve all book titles from a category
        singlebooklinks = datapage.find_all('h3') 
        for singlebooklink in singlebooklinks:
            a = singlebooklink.find('a')
            link = a['href']
            truncatelink = link.replace('../../..', 'catalogue')
            links.append('http://books.toscrape.com/' + truncatelink)
            
            
            
            
            
            for link in links:
                array = []
                url = link.strip()
            response = requests.get(url)
            if response.ok:
                soup = BeautifulSoup(response.text, 'lxml')
                singleBookTitle = soup.find('h1').text
                tds = soup.find_all('td')
                currentCategoryArray.append(singleBookTitle)
                singlebookdata = []
    
            



                for td in tds:
                    singlebookdata.append(td.text)
                data = dict(zip(headersArray, singlebookdata))
                booksdata.append(data)

            
    
    with open(path + titleCat +'.csv', 'w', newline='') as csvfile:
        print(booksdata)
        fieldnames = headersArray
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for book in booksdata:
                writer.writerow(book)

 
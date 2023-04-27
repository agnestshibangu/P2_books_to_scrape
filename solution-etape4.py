import requests
from bs4 import BeautifulSoup 
import numpy
import pandas
import csv

#### Étape 3 : Extraire tout les produits de toutes les catégorie ###
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
        categoriesNameArray.append(singleCategoryName.strip())                            # extract category name 
    # print('list category')
    # print(linkscategory)
    print('************ CATEGORY NAMES ARRAY *************')
    print(categoriesNameArray)

# for var in categoriesNameArray:
#         print(var) 
#         with open(var + '.csv', 'w', newline='') as csvfile:
#             fieldnames = headersArray

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
        #workingOnCategory = dict(zip(categoryHeaders, categorycontent))
        #print('im here')
        #print(currentCategory)        

        # retrieve all book titles from a category
        singlebooklinks = datapage.find_all('h3') 
        for singlebooklink in singlebooklinks:
            a = singlebooklink.find('a')
            link = a['href']
            truncatelink = link.replace('../../..', 'catalogue')
            links.append('http://books.toscrape.com/' + truncatelink)
            
            for link in links:
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

    # for var in categoriesNameArray:
    #     print(var) 
    with open(titleCat +'.csv', 'w', newline='') as csvfile:
        print(booksdata)
        fieldnames = headersArray
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for book in booksdata:
                writer.writerow(book)
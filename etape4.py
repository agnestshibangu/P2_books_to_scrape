import requests
from bs4 import BeautifulSoup 
import time
import os
import functions
from functions import headersArray
from functions import currentDate

timeStart = time.time()

# create a folder

path = str(functions.Horodatage()) + '/'
print(path)
os.mkdir(path)

url = 'http://books.toscrape.com/'

### récupérer toutes les catégories depuis la page d'acceuil du site pour en faire des urls ###

response = requests.get(url)

if response.ok:
    linkscategory = []
    linkCategoryName = []
    categoriesNameArray = []
    #singlebooklinks = []
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
    #print('************ CATEGORY NAMES ARRAY *************')


### on strip chaque catégorie et on liste chaque livre, on transforme le titre de chaque livre en url

for linkcategory in linkscategory:
    url = linkcategory.strip()
    #print(url)
    response = requests.get(url)
    if response.ok:
        links = []
        books = []
        singlebooklinks = []
        datapage = BeautifulSoup(response.text, 'lxml') # single CATEGORY page
        titleCat = datapage.find('h1').text
        currentCategory = 'null' 
        globals()['currentCategory'] = titleCat
        print('The current category is:', currentCategory)
        currentCategoryArray = []
        booksdata = []
        imagesData = []
               
        # retrieve all book titles from a category
        if datapage.find('li', {'class': 'next'}):
            urlAllBooks = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
            if url != urlAllBooks:
                print('//////////// CETTE CATEGORIE A PLUSIEURS PAGES ///////////////')
                functions.clickNextLink(singlebooklinks, url)
                print(singlebooklinks)
        else:
            print('/////////// CETTE CATEGORIE N A QU UNE PAGE /////////////////')
            singlebooklinks = datapage.find_all('h3')
            print(singlebooklinks)
        
        
        
        # for singlebooklink in singlebooklinks:
        #     a = singlebooklink.find('a')
        #     functions.catalogueLink(a,links)
        # print('LINKS')
        # print(links)

        '''        
        for link in links:
            singlebookdata = functions.retreiveAllTds(link)
            imagesData = functions.getSingleImageSrc(link, imagesData)
            #print(singlebookdata)
            if singlebookdata is None: 
                continue
            data = dict(zip(headersArray, singlebookdata))                  
            booksdata.append(data)
        print(len(booksdata))
        print(booksdata)
        booksdata = []
        links = []
        print(len(booksdata))
        print(booksdata)
        print('links empty')
        print(links)
        # print('///////// images data //////////////')
        # print(imagesData)
        # print('///////// length //////////')
        # print(len(imagesData))

        '''
        
        '''
        functions.saveImagesbyCat(imagesData, currentCategory)
        imagesData.clear()
        # print(len(imagesData))
        # print('image data after cleaning')
        # print(imagesData)
        fileNameForCsv = path + titleCat
        functions.generateCsv(fileNameForCsv, booksdata)
        '''

     

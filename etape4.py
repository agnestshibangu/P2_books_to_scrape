import requests
from bs4 import BeautifulSoup 
import numpy
import pandas

#### Étape 3 : Extraire toutes les données des produits d’une catégorie ####
#### convention de nommage, plusieurs fichiers avec intitulé catégorie #### 

url = 'http://books.toscrape.com/'

response = requests.get(url)

if response.ok:
    linkscategory = []
    datapage = BeautifulSoup(response.text, 'lxml')
    sidedivcat = datapage.find('div', {'class':'side_categories'})
    dbs =  sidedivcat.find_all('li')
    for db in dbs:
        a = db.find('a')
        linkcategory = a['href']
        linkscategory.append('http://books.toscrape.com/' + linkcategory) # generating links for each CATEGORY
    # print(linkscategory)
        for linkcategory in linkscategory:
            url = linkcategory.strip()
            response = requests.get(url)
            if response.ok:
                SingleBookSoup = BeautifulSoup(response.text, 'lxml') # single CATEGORY page
                singlebooklinks = SingleBookSoup.find_all('h3') # retrieve all books from a category
                print(singlebooklinks)
                for singlebooklink in singlebooklinks:
                    url = linkcategory.strip()
                    response = requests.get(url)
                    if response.ok:
                        SingleBookDataSoup = BeautifulSoup(response.text, 'lxml') # single BOOK page
                        # datas = data.find_all('td')
                        # print(datas)
                        # for data in datas:
                        # dataArray = numpy.append(dataArray, data.text)

                    

  
            






        

    



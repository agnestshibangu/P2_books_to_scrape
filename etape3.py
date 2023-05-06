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

# path = 'STEP3/'
# os.mkdir(path) 

#url = 'https://books.toscrape.com/catalogue/category/books/sequential-art_5/page-1.html'

# response = requests.get(url)

# booksdata = []

# if response.ok:
#     links = []
#     datapage = BeautifulSoup(response.text, 'lxml')


# currentPage = datapage

# def clickNext(currentPage):
#     if currentPage.find('li', {'class': 'next'}):
#         next = datapage.find('li', {'class': 'next'})
#         NextA = next.find('a')
#         NextAHref = NextA['href']
#         nextLink = 'https://books.toscrape.com/catalogue/category/books/sequential-art_5/' + NextAHref
#         print('i am here')
#         print(nextLink)
#         responseNext = requests.get(nextLink)
#         if responseNext.ok:
#             currentPage = BeautifulSoup(responseNext.text, 'lxml')
#             if currentPage.find('li', {'class': 'next'}):
#                 next = datapage.find('li', {'class': 'next'})
#                 NextA = next.find('a')
#                 NextAHref = NextA['href']
#                 nextLink = 'https://books.toscrape.com/catalogue/category/books/sequential-art_5/' + NextAHref
#                 print(nextLink)
#                 clickNext(currentPage)


# # clickNext(currentPage)
# response = requests.get(url)

# if response.ok:
#     links = []
#     datapage = BeautifulSoup(response.text, 'lxml')



def getNext(currentPage):
    if currentPage.find('li', {'class': 'next'}):
        next = currentPage.find('li', {'class': 'next'})
        NextA = next.find('a')
        NextAHref = NextA['href']
        nextLink = 'https://books.toscrape.com/catalogue/category/books/sequential-art_5/' + NextAHref
        print(nextLink)
        return nextLink
    
def getData(nextLink):
    resp = requests.get(nextLink)
    if resp.ok:
        currentPage = BeautifulSoup(resp.text, 'lxml')
        return currentPage
            

def clickNextLink():
    # on récupère le lien de la première page
    i = 1
    NextAHref = 'page-' + str(i) + '.html'
    currentPage = 'https://books.toscrape.com/catalogue/category/books/sequential-art_5/' + NextAHref
    resp = requests.get(currentPage)
    if resp.ok:
        currentPage = BeautifulSoup(resp.text, 'lxml')
    nextLink = getNext(currentPage)
    currentPage = getData(nextLink)
    nextLink = getNext(currentPage)
    currentPage = getData(nextLink)
    nextLink = getNext(currentPage)


    # currentPage = getData(nextLink)
    # nextLink = getNext(currentPage)

clickNextLink()




























'''

def clickNextLink():
    # on récupère le lien de la première page
    i = 1
    NextAHref = 'page-' + str(i) + '.html'
    resp = requests.get('https://books.toscrape.com/catalogue/category/books/sequential-art_5/' + NextAHref)
    currentPage = BeautifulSoup(resp.text, 'lxml')
    # on cherche le lien vers la deuxième page 
    if currentPage.find('li', {'class': 'next'}):
        next = currentPage.find('li', {'class': 'next'})
        print(next)
    nextLink = getNext(currentPage)
    print(nextLink)
    # on récupère data de la deuxième page 
    responseNext = requests.get(nextLink)
    if responseNext.ok:
            currentPage = BeautifulSoup(responseNext.text, 'lxml')
            # on récupère le data vers la troisième page 
            nextLink = getNext(currentPage)
        
            print('step2')
            print(nextLink) 
    clickNextLink()


clickNextLink()

'''






'''
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
'''


    
# if datapage.find('li', {'class': 'next'}):  
#     pageCountTag = datapage.find('li', {'class': 'current'}).text.strip()
#     print(pageCountTag)
#     pageCountValue = pageCountTag[-1]
#     print(pageCountValue)

# def clickNextLink():
#     if datapage.find('li', {'class': 'next'}):
#         next = BeautifulSoup(response.text, 'lxml').find('li', {'class': 'next'})
#         NextA = next.find('a')
#         NextAHref = NextA['href']
#         nextLink = 'https://books.toscrape.com/catalogue/category/books/sequential-art_5/' + NextAHref
#         print('//////////////nNEXT LINK ////////////')
#         print(nextLink)
#         # responseNext = requests.get(nextLink)
#         # if responseNext.ok:
#         #     nextNext =  BeautifulSoup(responseNext.content, 'lxml').find('li', {'class': 'next'})
#         #     print(nextNext)
#         #     NextA = next.find('a')
#         #     NextAHref = NextA['href']
#         #     nextLink = 'https://books.toscrape.com/catalogue/category/books/sequential-art_5/' + NextAHref
#         #     print(nextLink)            




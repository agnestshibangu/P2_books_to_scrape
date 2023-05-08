import requests
from bs4 import BeautifulSoup 
import datetime
import csv
import os

headersArray = []

def generateHeaders():
    url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
    response = requests.get(url)
    data = BeautifulSoup(response.text, 'lxml') 
    headers = data.find_all('th')
    for header in headers:
        headersArray.append(header.text)
    headersArray.append('title')
    print(headersArray)
    
generateHeaders()

currentDate = 'no horodatage'

def Horodatage():
    x = datetime.datetime.now()
    year = str(x.year)
    month = str(x.month)
    day = str(x.day)
    currentDate = year + '-' + month + '-' + day
    return str(currentDate)

Horodatage()

#### etape 3 ####

def getNext(currentPage, modifiedUrl):
    if currentPage.find('li', {'class': 'next'}):
        next = currentPage.find('li', {'class': 'next'})
        NextA = next.find('a')
        NextAHref = NextA['href']
        nextLink =  modifiedUrl + NextAHref
        print(nextLink)
        return nextLink
    
def getData(nextLink):
    resp = requests.get(nextLink)
    if resp.ok:
        currentPage = BeautifulSoup(resp.text, 'lxml')
        return currentPage
    
def getAllBooksTitleLoop(currentPage, singlebooklinks):
    AllBooksLoop = currentPage.find_all('h3')
    for book in AllBooksLoop:
        #print(book)
        singlebooklinks.append(book)
    return singlebooklinks

def clickNextLink(singlebooklinks, url):
    i = 1
    NextAHref = 'page-' + str(i) + '.html'
    print('i am here')
    print(url)
    modifiedUrl = url.replace('index.html', '')
    currentPage = modifiedUrl + NextAHref
    resp = requests.get(currentPage)
    if resp.ok:
        print('ok')
    '''
        currentPage = BeautifulSoup(resp.text, 'lxml')
    
        getAllBooksTitleLoop(currentPage, singlebooklinks)
    while currentPage.find('li', {'class': 'next'}):
        nextLink = getNext(currentPage, modifiedUrl)
        currentPage = getData(nextLink)
        getAllBooksTitleLoop(currentPage, singlebooklinks)
    '''

#################

#links = []

def catalogueLink(a,links):
    link = a['href']
    global truncatelink
    truncatelink = link.replace('../../..', 'catalogue')
    links.append('http://books.toscrape.com/' + truncatelink)
    return links


def retreiveAllTds(link): 
    url = link.strip()
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        tds = soup.find_all('td')
        singlebookdata = []
        title = soup.find('h1').text
        for td in tds:
            singlebookdata.append(td.text)
        singlebookdata.append(title)
        return singlebookdata
    
def getSingleImageSrc(link, imagesData):
    url = link.strip()
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        img = soup.find('img')
        toAddImgSrc = img['src']
        imgSrc = toAddImgSrc.replace('../../', 'http://books.toscrape.com/')
        imagesData.append(imgSrc)
    return imagesData
    
def saveImagesbyCat(imagesData, currentCategory):
    folder = str('DATA/booksillustrations/' + currentCategory + '/')
    if not os.path.exists(folder):
        os.makedirs(folder)
    print('i m in the saveimagesfunction')
    x = 1
    for image in imagesData:
        num = str(x)
        url = image
        image_source = requests.get(url)
        output = str('img-' + num + '.png')
        with open(f'{folder}{output}', 'wb') as file:
            file.write(image_source.content)
        x = x + 1
    
    

def generateCsv(fileNameForCsv, booksdata):
    with open(fileNameForCsv +'.csv', 'w', encoding="utf-8", newline='') as csvfile:
            fieldnames = headersArray
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for book in booksdata:
                writer.writerow(book)













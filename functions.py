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
    return currentDate

Horodatage()


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
    
def getSingleImage(link, imagesData):
    url = link.strip()
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        img = soup.find('img')
        toAddImgSrc = img['src']
        imgSrc = toAddImgSrc.replace('../../', 'http://books.toscrape.com/')
        imagesData.append(imgSrc)
    # print('/////////////////////// from functions')
    # print(imagesData)
    # print('/////////////////////// from functions')
    return imagesData
    


    
def saveImagesbyCat(imagesData, currentCategory):

    folder = str('images/' + currentCategory + '/')
    # Check first if folder exists, else create a new one
    if not os.path.exists(folder):
        os.makedirs(folder)

    for image in imagesData:
        url = image
        image_source = requests.get(url)
        output = 'img.png'
        
        with open(f'{folder}{output}', 'wb') as file:
            file.write(image_source.content)



    
def generateCsv(fileNameForCsv, booksdata):
    with open(fileNameForCsv +'.csv', 'w', encoding="utf-8", newline='') as csvfile:
            fieldnames = headersArray
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for book in booksdata:
                writer.writerow(book)










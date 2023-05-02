import requests
from bs4 import BeautifulSoup 
import concurrent.futures
import datetime
import csv

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
    print(currentDate)

Horodatage()

links = []

def catalogueLink(a):
    link = a['href']
    global truncatelink
    truncatelink = link.replace('../../..', 'catalogue')
    links.append('http://books.toscrape.com/' + truncatelink)
    return links

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(catalogueLink, links)


singlebookdata = []

def retreiveAllTds(link): 
    url = link.strip()
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml') 
    tds = soup.find_all('td')
    for td in tds:
        singlebookdata.append(td.text)
    # title = soup.find('h1').text 
    # singlebookdata.append(title)

    return singlebookdata

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(retreiveAllTds, singlebookdata) 

    
def generateCsv(fileNameForCsv, booksdata):
    with open(fileNameForCsv +'.csv', 'w', newline='') as csvfile:
            fieldnames = headersArray
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for book in booksdata:
                writer.writerow(book)











import requests
from bs4 import BeautifulSoup 
import numpy
import csv

#### Étape 3 : Extraire toutes les données des produits d’une catégorie ####

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

url = 'https://books.toscrape.com/catalogue/category/books/art_25/index.html'

response = requests.get(url)

# rowsArray = numpy.array([])
booksdata = []

if response.ok:
    links = []
    datapage = BeautifulSoup(response.text, 'lxml')
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
            tds = soup.find_all('td')
            singlebookdata = []
       
            for td in tds:
                singlebookdata.append(td.text)

            data = singlebookdata
            data = dict(zip(headersArray, singlebookdata))
            print(data)
            booksdata.append(data)
            #print(data)
    print(booksdata)

with open('etape3.csv', 'w', newline='') as csvfile:
    fieldnames = headersArray
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for book in booksdata:
        writer.writerow(book)
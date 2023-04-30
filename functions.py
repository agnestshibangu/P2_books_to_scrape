import requests
from bs4 import BeautifulSoup 
import datetime

### fonction pour générer un tableau de headers ###

headersArray = []

def generateHeaders():
    url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
    response = requests.get(url)
    data = BeautifulSoup(response.text, 'lxml') 

    headers = data.find_all('th')
    for header in headers:
        headersArray.append(header.text)
    print(headersArray)
    
generateHeaders()


### fonction pour avoir la date du jour ###

currentDate = 'no horodatage'

def Horodatage():
    x = datetime.datetime.now()
    year = str(x.year)
    month = str(x.month)
    day = str(x.day)
    currentDate = year + '-' + month + '-' + day
    print(currentDate)

Horodatage()




     



'''
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
            data = dict(zip(headersArray, singlebookdata))
            booksdata.append(data)
    

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


'''










'''
##### fonction pour écrire les csv ####

with open('etape3.csv', 'w', newline='') as csvfile:
    fieldnames = headersArray
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for book in booksdata:
        writer.writerow(book)


with open(path + titleCat +'.csv', 'w', newline='') as csvfile:
    print(booksdata)
    fieldnames = headersArray
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for book in booksdata:
            writer.writerow(book)

##### fonction pour l'horodatage ####


x = datetime.datetime.now()
print(x.year)
print(x.month)
print(x.day)
year = str(x.year)
month = str(x.month)
day = str(x.day)
currentDate = year + '-' + month + '-' + day

'''


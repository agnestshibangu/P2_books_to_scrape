import requests
from bs4 import BeautifulSoup 

def generateHeaders():
    url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
    response = requests.get(url)
    data = BeautifulSoup(response.text, 'lxml') 

    headersArray = []

    headers = data.find_all('th')
    for header in headers:
        headersArray.append(header.text)
    print(headersArray)     













'''
#### fonction pour récuperer les headers ####

url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
response = requests.get(url)
data = BeautifulSoup(response.text, 'lxml') 

headersArray = []

headers = data.find_all('th')
for header in headers:
    headersArray.append(header.text)
print(headersArray)


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


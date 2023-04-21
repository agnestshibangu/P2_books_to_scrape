import requests
from bs4 import BeautifulSoup 
import numpy
import pandas
import csv

#### Étape 3 : Extraire toutes les données des produits d’une catégorie ####

### data d'un seul item pour récuperer les headers pour pouvoir construire le csv ###

#Creating two 2D arrays
#arr1 = numpy.array([[1, 2, 3]])
#print(arr1)
#arr2 = numpy.array([[4,2,3]])
#print(arr2)

#arr3 = numpy.concatenate((arr1, arr2), axis=0)
#print(arr3)

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
# print(response)

rowsArray = numpy.array([])
booksdata = []

if response.ok:
    links = []
    datapage = BeautifulSoup(response.text, 'lxml')
    singlebooklinks = datapage.find_all('h3')
    # print(singlebooklinks)
    for singlebooklink in singlebooklinks:
        a = singlebooklink.find('a')
        link = a['href']
        truncatelink = link.replace('../../..', 'catalogue')
        links.append('http://books.toscrape.com/' + truncatelink)
        for link in links:
            # print(link)
            url = link.strip()
            response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'lxml')
            # print('title     ' + soup.find('h1').text)

            # ths = soup.find_all('th')
            # for th in ths:
            #     print(th.text)
            # #    headersArray = numpy.append(headersArray, th.text)

            tds = soup.find_all('td')
            singlebookdata = []
       
            for td in tds:
                singlebookdata.append(td.text)

            data = singlebookdata
            data = dict(zip(headersArray, singlebookdata))
            booksdata.append(data)
            #print(data)
print(booksdata)


with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = headersArray
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for book in booksdata:
        writer.writerow(book)




# table = {'headers' : headersArray, 'rows' : rowsArray }
# df = pandas.DataFrame(data=table)
# print(df)
# df.to_csv("df.csv", encoding='utf-8', sep=',', index=False)    

# df = pandas.DataFrame([rowsArray], columns=[headersArray])
# print(df)
# df.to_csv("etape3.csv", encoding='utf-8', sep=',', index=False)

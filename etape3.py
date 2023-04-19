import requests
from bs4 import BeautifulSoup 
import numpy
import pandas

#### Étape 3 : Extraire toutes les données des produits d’une catégorie ####

### data d'un seul item pour récuperer les headers pour pouvoir construire le csv ###

'''
url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
response = requests.get(url)
data = BeautifulSoup(response.text, 'lxml') 

headersArray = numpy.array([])

headers = data.find_all('th')
for header in headers:
    headersArray = numpy.append(headersArray, header.text)

print(headersArray) 
'''

###

url = 'https://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html'

response = requests.get(url)
# print(response)

headersArray = numpy.array([])
rowsArray = numpy.array([])

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
            for td in tds:
                # print(td.text)
                rowsArray = numpy.append(rowsArray, td.text)
print(rowsArray)
 
table = {'headers' : headersArray, 'rows' : rowsArray }
df = pandas.DataFrame(data=table)
print(df)
df.to_csv("df.csv", encoding='utf-8', sep=',', index=False)    



import requests
from bs4 import BeautifulSoup 
import numpy
import pandas

#### Étape 3 : Extraire toutes les données des produits d’une catégorie ####

url = 'https://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html'

response = requests.get(url)

headersArray = numpy.array([])
rowsArray = numpy.array([])

# if response.ok:
#     links = []
#     datapage = BeautifulSoup(response.text, 'lxml')
#     singlebooklinks = datapage.find_all('h3')
#     # print(singlebooklinks)
#     for singlebooklink in singlebooklinks:
#         a = singlebooklink.find('a')
#         link = a['href']
#         links.append('http://books.toscrape.com/' + link)
# print(len(links))

# with open('urls.csv', 'w') as file:
#     for link in links:
#         file.write(link + '\n')

if response.ok:
    links = []
    datapage = BeautifulSoup(response.text, 'lxml')
    singlebooklinks = datapage.find_all('h3')
    # print(singlebooklinks)
    for singlebooklink in singlebooklinks:
        a = singlebooklink.find('a')
        link = a['href']
        links.append('http://books.toscrape.com/' + link)
    for link in links:
        url = link.strip()
        response = requests.get(url)
        print(response)
    #         rows = data.find_all('td')
    #         for row in rows:
    #             rowsArray = numpy.append(rowsArray, row.text)
     


            # for header in headers:
            #     headersArray = numpy.append(headersArray, header.text)
            # datas = data.find_all('td')
            # for row in rows:
            # rowsArray = numpy.append(rowsArray, row.text)


        



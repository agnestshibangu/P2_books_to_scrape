import requests
from bs4 import BeautifulSoup 
import numpy
import pandas

url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
response = requests.get(url)
data = BeautifulSoup(response.text, 'lxml')
title = data.find('h1')
print(title.text)
price = data.find('p', {'class':'price_color'})
print(price.text)
instock = data.find('p', {'class':'instock'})
print(instock.text)

#### Étape 2 : Extraire les données d’un seul produit ####

headersArray = numpy.array([])
dataArray = numpy.array([])
# print(headersArray)

headers = data.find_all('th')
for header in headers:
    headersArray = numpy.append(headersArray, header.text)

datas = data.find_all('td')
print(datas)
for data in datas:
    dataArray = numpy.append(dataArray, data.text)

print(len(headersArray))
print(len(dataArray))

### méthode qui retourne le mauvais format ###

# table = {'headers' : headersArray, 'rows' : dataArray }
# df = pandas.DataFrame(dataArray, headersArray)
# print(df)
# df.to_csv("df.csv", encoding='utf-8', sep=',', columns=headersArray)

###


# df = pandas.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=header)
# avec mon code #
df = pandas.DataFrame([dataArray], columns=[headersArray])
#
print(df)
df.to_csv("df.csv", encoding='utf-8', sep=',', index=False)
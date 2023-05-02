import requests
from bs4 import BeautifulSoup 
import numpy
import pandas

url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
response = requests.get(url)
data = BeautifulSoup(response.text, 'lxml')
title = data.find('h1').text
print(title)
price = data.find('p', {'class':'price_color'})
print(price.text)
instock = data.find('p', {'class':'instock'})
print(instock.text)

#### Étape 2 : Extraire les données d’un seul produit ####

headersArray = []
dataArray = []

headers = data.find_all('th')
for header in headers:
    headersArray.append(header.text)
headersArray.append('title')

datas = data.find_all('td')
print(datas)
for data in datas:
    dataArray.append(data.text)
dataArray.append(title)


df = pandas.DataFrame([dataArray], columns=[headersArray])
#
print(df)
df.to_csv("etape2.csv", encoding='utf-8', sep=',', index=False)
import requests as rq
import os


# url = 'https://books.toscrape.com/media/cache/ee/cf/eecfe998905e455df12064dba399c075.jpg'
# output = 'blabla'
# image_source = rq.get(url)


# path = './images/'
# if not os.path.exists(path):
#     os.makedirs(path)

# with open(f'{path}{output}'+'.jpg', 'wb') as file:
#     file.write(image_source.content)
#     print(f'Successfully downloaded: {output}')



def other_function(parameter):
    return parameter + 5

def main_function():
    x = 10
    print(x)    
    x = other_function(x)
    print(x)

main_function()
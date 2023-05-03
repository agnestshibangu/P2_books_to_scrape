import requests 
import os
import pathlib


def save_image():

    url = 'https://books.toscrape.com/media/cache/d7/39/d73914232130fdf90d66f02fd9798f2b.jpg'
    image_source = requests.get(url)
    folder = 'images/'
    # Check first if folder exists, else create a new one
    if not os.path.exists(folder):
        os.makedirs(folder)
    output = 'image'
    # Create our output in the specified folder (wb = write bytes)
    with open(f'{folder}{output}', 'wb') as file:
        file.write(image_source.content)
        print(f'Successfully downloaded: {output}')

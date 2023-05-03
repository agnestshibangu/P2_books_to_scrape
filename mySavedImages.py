import requests 
import os
import pathlib
import functions



folder = 'folder/'
    # Check first if folder exists, else create a new one
if not os.path.exists(folder):
    os.makedirs(folder)


def save_image():

    url = 'https://books.toscrape.com/media/cache/3f/f6/3ff6fe5d0c5ca7ab2ed8b5971e299caa.jpg'
    image_source = requests.get(url)
    
    output = 'image.png'
    
    # Create our output in the specified folder (wb = write bytes)
    with open(f'{folder}{output}', 'wb') as file:
        file.write(image_source.content)
        print(f'Successfully downloaded: {output}')

save_image()



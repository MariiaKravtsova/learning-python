#!/usr/bin/env python3

import requests
import bs4
import os

def downloadImage(url, path):
    try:
        # setup
        os.makedirs('apod', exist_ok=True)

        # get
        res = requests.get(url)
        res.raise_for_status()

        # parse
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        image_element = soup.findAll('img')[0].get('src')

        # Get image url and download it
        image_url = url + image_element
        print('Downloading image: ', image_url)
        res = requests.get(image_url)
        res.raise_for_status

        # Saving the image into apod folder
        with open(os.path.join('apod', os.path.basename(image_url)), 'wb') as f:
            for chunk in res.iter_content(100000):
                f.write(chunk)

        print('Done.')
    except requests.exceptions.HTTPError as e:
        print('Error: {}'.format(e.message))
    except Exception as e:
        print('Error: {}'.format(e.message))

if __name__=='__main__':
    downloadImage('https://apod.nasa.gov/apod/', 'apod')

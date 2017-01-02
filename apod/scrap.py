import requests, bs4, os

url = 'https://apod.nasa.gov/apod/'

os.makedirs('apod', exist_ok=True)

# TODO: some condition here to have a loop, today's date?

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

imageElement = soup.findAll('img')[0].get('src')

if imageElement == []:
    print('No image found.')
else:
    # Get image url and download it
    imageUrl = url + imageElement
    print('Downloading image: ', imageUrl)
    res = requests.get(imageUrl)
    res.raise_for_status
    print(res)

    # Saving the image into apod folder
    imageFile = open(os.path.join('apod', os.path.basename(imageUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    print('Done.')

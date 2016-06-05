#! python3
# Downloads every single XKCD comic.

import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading %s' % urlNumber)
        res = requests.get(urlNumber)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, "lxml")
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Comic not found.')
        else:
            try:
                comicUrl = 'http:' + comicElem[0].get('src')
                print('Downloading image %s ...' % (comicUrl))
                res = requests.get(comicUrl)
                res.raise_for_status()
            # except requests.exceptions.MissingSchema:
            #     prevLink = soup.select('a[rel="prev"]')[0]
            #     url = 'http://xkcd.com' + prevLink.get('href')
            #     continue
                imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()

        # prevLink = soup.select('a[rel="prev"]')[0]
        # urlNumber = 'http://xkcd.com' + prevLink.get('href')

downloadThreads = []
for i in range(0, 1400, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()

print('Done.')

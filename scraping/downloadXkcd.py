#! python3

import requests, os, bs4

url = 'http://xdcd.com'
os.makedirs('xdcd', exist_ok=True)

while not url.endswith('#'):

    print('now downloading {}...'.format(url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('Nothing images')
    else:
        comic_url = 'http:' + comic_elem[0].get('src')

        print('downloading {}...'.format(comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()

        image_file = open(os.path.join('xdcd, os.path.basename(comic_url'), 'wb')
        for chunk in res.iter_content(1000000):
            image_file.write(chunk)
        image_file.close()
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')


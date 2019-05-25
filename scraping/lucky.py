#! python3

import requests, sys, webbrowser, bs4

print('Googling...')

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))

try:
    res.raise_for_status()
except Exception as ex:
    print(ex)

soup = bs4.BeautifulSoup(res.text)  # TODO
link_elems = soup.select('.r a')

num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))


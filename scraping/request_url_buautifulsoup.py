
import requests, bs4

res = requests.get('http://nostarch.com')
try:
    res.raise_for_status()
except:
    type(res)

no_starch_sorp = bs4.BeautifulSoup(res.text)
type(no_starch_sorp)
print(no_starch_sorp)

elems = no_starch_sorp.select('#node-496') # id='node-496'
type(elems)
print(elems)


print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

print('-' * 20)

p_elems = no_starch_sorp.select('p')
for p in p_elems:
    print(str(p.getText()))

print('-' * 20)

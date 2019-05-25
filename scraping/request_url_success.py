import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)

if res.status_code :
#    print(res.text[:250])
    for chunk in res.iter_content(1):
        print(chunk)



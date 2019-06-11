#! python3
# quicWeather.py

import json, requests, sys
import pprint

if len(sys.argv) < 2:
    print('Usage: {} location'.format(sys.args[0]))
    exit(code=1)

location = ' '.join(sys.argv[1:])

APPID='Weather APP ID'

url='https://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=3&appid={}'.format(
    location, APPID
)

response = requests.get(url)
response.raise_for_status()

weather_data = json.loads(response.text)

pprint.print(weather_data)

w = weather_data['list']

print('Today {}'.format(location))
print(w[0]['weather']['main'], '-', w[1]['weather'][0]['description'])

print('Tomorrow')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])

print('Next Tomorrow')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])


import requests
import json


getjoke = 'https://api.chucknorris.io/jokes/random'

try:
    thejoke = requests.get(getjoke)
    if thejoke.status_code == 200:
        json_thejoke = thejoke.json()
        print(f'Chuk Norris joke for you:\n{json_thejoke['value']}')

except requests.exceptions.RequestException as e:
    print('Hakua ei voitu suorittaa.')


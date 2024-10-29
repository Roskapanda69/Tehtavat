import requests
import json


getjoke = 'https://api.chucknorris.io/jokes/random'

thejoke = requests.get(getjoke).json()

print (f'Chuk Norris joke for you:\n{thejoke['value']}')

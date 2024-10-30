# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan
# tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi.
# Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import requests
import json

from keything import secretkey

kaupunki = input(f'Anna kaupungin nimi: ').capitalize()

# Change {secretkey} for your own api-key to this code to work.
haku = f'https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={secretkey}'


try:
    saatiedot = requests.get(haku)
    if saatiedot.status_code == 200:
        json_saatiedot = saatiedot.json()
        kelvin = int(json_saatiedot['main']['temp'])
        print(f'Sää tänään {kaupunki}:\n{json_saatiedot["weather"][0]["description"].capitalize()}.\nLämpötila {kelvin - 273.15:.2f} astetta.')

except requests.exceptions.RequestException as e:
    print('Hakua ei voitu suorittaa.')
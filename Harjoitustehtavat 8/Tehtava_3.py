# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
# Kirjoita hakukenttään geopy ja vie asennus loppuun.

import mysql.connector
import geopy

def lasku(icao):
    sql = (f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = "{icao}"')
    cursor = db_connection.cursor()
    cursor.execute(sql)
    airport_data = cursor.fetchall()
    return airport_data

db_connection = mysql.connector.connect(
    host="localhost", #host= "127.0.0.1"
    port=3306,
    database="flight_game",
    user='kakka',
    password="Hohojaa",
    autocommit=True
    )

icao_1 = input(f'Anna ensimmäisen lentokenttän ICAO-koodi: ')
icao_2 = input(f'Anna seuraavan lentokentän ICAO-koodi: ')
distance1 = lasku(icao_1)
distance2 = lasku(icao_2)


from geopy import distance
print(f'Etäisyys on {distance.distance(distance1, distance2).km:.2f}km. ')

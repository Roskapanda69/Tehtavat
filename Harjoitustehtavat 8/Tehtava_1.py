# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen
# sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

def hae_asema(icao):
    sql = (f'SELECT name, municipality FROM airport WHERE ident = "{icao}"')
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

icao=input("Anna lentoaseman ICAO-koodi: ")
theairport=hae_asema(icao)
print(f"{theairport[0][0]}, {theairport[0][1]}")
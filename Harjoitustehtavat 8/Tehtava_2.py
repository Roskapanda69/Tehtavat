# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja
# tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta,
# helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

def hae_asemat(iso):
    sql = (f'SELECT type, count(*) FROM airport WHERE iso_country = "{iso}" group by type')
    cursor = db_connection.cursor(dictionary=True)
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

country= input(f'Anna maan ISO-koodi: ')
airports = hae_asemat(country)
for airport in airports:
    print(f'Typpi: {airport["type"]} ja määrä: {airport["count(*)"]}')


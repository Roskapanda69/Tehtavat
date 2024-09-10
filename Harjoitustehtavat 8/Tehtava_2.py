# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja
# tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta,
# helikopterikenttiä on 15 kappaletta jne.

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
# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan
# lentokentän nimen ja kaupungin JSON-muodossa.
# Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
# Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa:
# http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa:
# {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask
import mysql.connector

app = Flask(__name__)

db_connection = mysql.connector.connect(
    host="localhost", #host= "127.0.0.1"
    port=3306,
    database="flight_game",
    user='kakka',
    password="Hohojaa",
    autocommit=True
    )

def hae_asema(icao):
    sql = (f'SELECT name, municipality FROM airport WHERE ident = "{icao}"')
    cursor = db_connection.cursor()
    cursor.execute(sql)
    airport_data = cursor.fetchall()
    return airport_data

@app.route('/kenttä/<icao>')

def kentta(icao):
    icao_code = icao
    the_asema = hae_asema(icao_code)
    oikea_asema = {
        'ICAO': icao_code,
        'Name': the_asema[0][0],
        'Municipality': the_asema[0][1],
    }
    return oikea_asema

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
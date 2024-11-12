# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask

app = Flask(__name__)


@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    luku = int(luku)
    jaot = 0
    is_prime = False
    for numero in range(2, luku):
        if luku % numero == 0:
            jaot += 1
    if jaot == 0:
        is_prime = True

    vastaus = {
        "Number": luku,
        "isPrime": is_prime
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
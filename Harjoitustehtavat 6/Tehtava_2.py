# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random
luku = 0

def noppa(d):
    global luku
    luku=random.randint(1, d)
    return luku

tahkot=int(input(f"Anna tahkojen määrä: "))
noppa(tahkot)

while noppa(tahkot)<tahkot:
    print(f"{luku} ")

print(f"{luku} ")

# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random
luku = 0

def noppa():
    global luku
    luku=random.randint(1, 6)
    return luku

while noppa()<6:
    print(f"{luku} ")

print(f"{luku} ")

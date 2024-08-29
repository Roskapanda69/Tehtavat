#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
#Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
#Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
#Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

luku = random.randint(1, 10)
arvaus = int(input(f"OwO arvaa luku väliltä 1-10: "))

while luku != arvaus:
    if luku < arvaus:
        print(f"Arvaus on aivan liian suuri OwO !")
        arvaus = int(input(f"OwO arvaa luku: "))
    if luku > arvaus:
        print(f"Arvaus on aivan liian pieni OwO !")
        arvaus = int(input(f"OwO arvaa luku: "))

print(f"Oikein UwU")
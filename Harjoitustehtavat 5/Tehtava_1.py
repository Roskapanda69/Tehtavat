#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
import random

noppat= int(input(f"Anna heitettävien noppien määrä: "))
luvut= []
heitot = 0

while heitot < noppat:
   heitto = random.randint(1,6)
   luvut.append(heitto)
   heitot += 1

print(luvut)
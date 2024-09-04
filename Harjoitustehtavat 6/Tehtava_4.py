#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
#Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot listan,
#kutsut funktiota ja tulostat sen palauttaman summan.

def summaaja():
    for n in listaa:
        summa=n+n
        return summa


listaa= []

while True:
    numero= input("Anna summattavat luvut: ")
    listaa.append(numero)
else:
    print(f"Lukjen summa on: {summaaja()}")
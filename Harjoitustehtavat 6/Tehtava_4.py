#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
#Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot listan,
#kutsut funktiota ja tulostat sen palauttaman summan.


def summaaja(listaa):
    summa=0
    summa=sum(listaa)
    return summa


listaa= []
numero= 0

while True:
    syotto= input("Anna summattavat luvut òwó : ")
    if syotto=="":
        break
    numero= int(syotto)
    listaa.append(numero)

print(f"Lukjen summa on UwU : {summaaja(listaa)}")

# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin
# parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def paritonpois(lista):
    for n in lista:
        if n%2==0:
            siisti.append(n)
        else:
            continue


lista= []
siisti= []
numero= 0

while True:
    syotto= input("Anna lukuja OwO : ")
    if syotto=="":
        break
    numero= int(syotto)
    lista.append(numero)

paritonpois(lista)
print(f"Alkuperäinen lista: {lista}")
print(f"Parillisija lukuja ovat UwU : {siisti}")

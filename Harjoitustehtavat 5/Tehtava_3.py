#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
# #onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.


luku = int(input(f"Anna luku :"))
jaot = 0

for numero in range(2, luku ):
    if luku % numero == 0 :
        jaot +=1

if jaot==0:
    print(f"Luku on alukuluku UwU")

else:
    print(f"Luku ei ole alkuluku òwó")







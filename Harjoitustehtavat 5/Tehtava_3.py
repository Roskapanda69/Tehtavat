#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
# #onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

#määritellään range, jolla kokeillaan jaollisuus 1:stä omaan lukuun yhden numeron välein
#jos jaollisuus == 0, luku on jaollinen kokeillulla luvulla. jos näitä on enemmän kuin kaksi, luku ei ole alkuluku

luku = int(input(f"Anna luku :"))
jakaa = 1
jaot = 0
jako = 0
while jakaa <= luku :
    for numero in range(jakaa, luku+1):
        jakaa += 1
        jako = luku/numero
        if luku%numero!=0 and not jako==1 and not jako==luku:
            jaot +=1


if jaot==(luku-2) :
    print(f"Luku on alukuluku")

else:
    print(f"Luku ei ole alkuluku")







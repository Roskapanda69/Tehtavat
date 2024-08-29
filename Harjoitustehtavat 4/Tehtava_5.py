#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
#Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
#Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
#Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
#(Oikea käyttäjätunnus on python ja salasana rules).

kayttajatunnus = "python"
salasana= "rules"
kerrat = 0

i_kayttajatunnus=input(f"Anna käyttäjä tunnus:")
if i_kayttajatunnus != kayttajatunnus:
    kerrat += 1

while i_kayttajatunnus != kayttajatunnus:
    kerrat += 1
    print(f"Väärä käyttäjätunnus. (•̀з•́)")
    i_kayttajatunnus = input(f"Anna käyttäjä tunnus:")
    if kerrat == 5:
        print(f"Pääsy evätty òwó")
        break

if i_kayttajatunnus == kayttajatunnus:
    i_salasana=input(f"Anna salasana:")
    if i_salasana != salasana:
        kerrat += 1
    while i_salasana != salasana:
        kerrat += 1
        print(f"Väärä salasana. (•̀з•́)")
        i_salasana = input(f"Anna salasana:")
        if kerrat == 5:
            print(f"Pääsy evätty òwó")
            break


if i_kayttajatunnus == kayttajatunnus and i_salasana==salasana:
    print(f"Tervetuloa! UwU ")
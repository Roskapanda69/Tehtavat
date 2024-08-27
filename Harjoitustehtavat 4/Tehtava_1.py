#Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

luku = 1
while luku<1000:
        while luku % 3 == 0:
            print(f"{luku}")
            break
        luku = luku+1
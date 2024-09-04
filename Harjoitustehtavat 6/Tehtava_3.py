# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan
# vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.


#siistitty

def gallitra(gall):
    return gall * 3.785

while True:
    maara= float(input(f"Anna bensan määrä gallonina: "))
    if maara < 0:
        print(f"Error >_<")
        break
    else:
        litraa=gallitra(maara)
        print(f"{maara} gallonaa on litroina {litraa:.5} ")
"""
eka versio koodista

def lasku(gall):
    global tulos
    tulos = gall * 3.785
    return tulos

maara= float(input(f"Anna bensan määrä gallonina: "))
lasku(maara)


else:
    print(f"{maara} on litroina {tulos:.5} ")

while maara>=0:
    maara=float(input(f"Anna bensan määrä gallonina: "))
    lasku(maara)
    if maara < 0:
        print(f"Error >_<")
        break
    else:
        print(f"{maara} on litroina {tulos:.5} ")
"""
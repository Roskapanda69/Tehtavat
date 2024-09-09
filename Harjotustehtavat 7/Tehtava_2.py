# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
# kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi, sen mukaan
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
# Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = set()

def tsekaaja(nimi):
    if nimi in nimet:
        print(f"Aienmmin syötetty nimi UwU.")
    if nimi not in nimet:
        nimet.add(nimi)
        print(f"Uusi nimi UwU ")
    return

while True:
    nimi = input(f"Anna nimi : ")
    tsekaaja(nimi)
    if nimi == "":
        print(f"{nimet}")
        break
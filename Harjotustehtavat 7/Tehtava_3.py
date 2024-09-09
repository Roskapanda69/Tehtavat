# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
# ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
# kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
# Löydät koodeja helposti selaimen avulla.)

asemat = {"EFHK", "Helsinki-Vantaan"
          "EFIV", "Ivalo Airport"
          "EFJO", "Joensuu Airport"
          "EFJY", "Jyväskylä Airport"
          }
def lisaa():
    koodi= input("Anna asemana koodi: ")
    nimi= input("Anna aseman nimi: ")
    asemat[koodi] = nimi
    return

def hae():
    haku= input("Anna aseman ICAO-koodi: ")
    if haku in asemat:
        print(f"")

while True:
    syote=input("Haluatko syöttää uuden kentän (Y), vai hakea asemia (S) vai lopetta (jätä tyhjäksi): ")
    if syote=="y" or syote=="Y":
        lisaa()
    if syote=="s" or syote=="S":

    if syote=="":
        break


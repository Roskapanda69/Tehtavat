#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# #(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
#Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
#käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

kaupunki = []

for nimet in range(5):
    nimet =input(f"Anna kaupungin nimi: ")
    kaupunki.append(nimet)

for nimet in kaupunki:
    print(nimet)
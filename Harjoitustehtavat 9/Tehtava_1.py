#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
#tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja,
#joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
#Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
#Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
#Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus_nyt = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = nopeus_nyt
        self.kuljettu_matka = kuljettu_matka

auto1=Auto("ABC - 123", "142 km/h")

print(f'Auton rekisterinumero on: {auto1.rekisteritunnus} \nAuton huippunopeus on: {auto1.huippunopeus}\nAuton nopeus nyt on: {auto1.nopeus_nyt}\nAuton kulkema matka on: {auto1.kuljettu_matka}')

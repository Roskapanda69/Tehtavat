# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto
# ja Polttomoottoriauto. Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
# Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen,
# huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä
# asettaa oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja
# yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus,
# käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus_nyt = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = nopeus_nyt
        self.kuljettu_matka = kuljettu_matka

    def kiihdytys(self, kiihtyy):
        if self.nopeus_nyt <= self.huippunopeus:
            self.nopeus_nyt += kiihtyy
            if self.nopeus_nyt > self.huippunopeus:
                self.nopeus_nyt = self.huippunopeus
            elif self.nopeus_nyt < 0 :
                self.nopeus_nyt = 0
        return self.nopeus_nyt

    def kulje(self, aika):
       self.kuljettu_matka += (self.nopeus_nyt * aika)
       return self.kuljettu_matka

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, nopeus_nyt, kuljettu_matka, akkukapasitetti):
        self.akkukapasitetti = f' {akkukapasitetti} kwh'
        super().__init__(rekisteritunnus, huippunopeus, nopeus_nyt, kuljettu_matka)

class Polttomoottori(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, nopeus_nyt, kuljettu_matka, bensatankki):
        self.bensatankki = f'  {bensatankki} l'
        super().__init__(rekisteritunnus, huippunopeus, nopeus_nyt, kuljettu_matka)

autot = []
autot.append(Sahkoauto('ABC-15', 150, 0, 0, 52.2))
autot.append(Polttomoottori('ABC-123', 165, 0, 0, 32.3))

for a in autot:
    a.kiihdytys(random.randint(50, a.huippunopeus))

for a in autot:
    a.kulje(3)
    print (f'Auto: {a.rekisteritunnus},\nkulki {a.kuljettu_matka} km.\n')
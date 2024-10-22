#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
# joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa.
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h,
# sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

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



auto1=Auto("ABC - 123", 142)
auto1.kiihdytys(30)
print(f'Auton nopeus nyt on: {auto1.nopeus_nyt}\n')
auto1.kiihdytys(70)
print(f'Auton nopeus nyt on: {auto1.nopeus_nyt}\n')
auto1.kiihdytys(50)
print(f'Auton nopeus nyt on: {auto1.nopeus_nyt}\n')

#Hätäjarru
auto1.kiihdytys(-200)
print(f'HÄTÄJARRUTUS!!\nAuton nopeus nyt on: {auto1.nopeus_nyt}\n')
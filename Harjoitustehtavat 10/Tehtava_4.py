# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka,
# jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
# Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.
# Luokassa on seuraavat metodit:

# tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli
# arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.

# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.

# kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän.
# Muussa tapauksessa palautetaan False.

# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina
# tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin
# avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

from random import randint, random

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


class Kilpailu:
    def __init__(self, nimi, pituus , autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = []
        for name in range(1, 11):
            rekisteritunnus = 'ABC - ' + str(name)
            huippunopeus = randint(100, 200)
            self.autot.append(Auto(rekisteritunnus, huippunopeus))

    def tunti_kuluu(self):
        for autoliikkuva in self.autot:
            vauhtimuutos = randint(-10, 15)
            autoliikkuva.kiihdytys(vauhtimuutos)
            autoliikkuva.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.autot:
            print(f'Auto rekisterillä: {auto.rekisteritunnus}, huippunopeus oli: {auto.huippunopeus}, Auton nopeus maalissa oli: {auto.nopeus_nyt}, Auto ajoi {auto.kuljettu_matka} km. ')


















'''
valmis = False

while True:
    for auto in kilpaautot:
        if auto.kuljettu_matka<10000:
            vauhtimuutos = randint(-10,15)
            auto.kiihdytys(vauhtimuutos)
            auto.kulje(1)
        if auto.kuljettu_matka>=10000:
            for auto in kilpaautot:
                print(f'Auto rekisterillä: {auto.rekisteritunnus}, huippunopeus oli: {auto.huippunopeus}, Auton nopeus maalissa oli: {auto.nopeus_nyt}, Auto ajoi {auto.kuljettu_matka} km. ')
            valmis = True
            break
    if valmis == True:
        break

'''

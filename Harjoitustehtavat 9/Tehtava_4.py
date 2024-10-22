#Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti
# "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.Kaikkia autoja käsketään liikkumaan yhden tunnin ajan.
# Tämä tehdään kutsumalla kulje-metodia.Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään
# 10000 kilometriä. Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

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

kilpaautot = []

for name in range(1,11):
    rekisteritunnus = 'ABC - ' + str(name)
    huippunopeus = randint(100, 200)
    kilpaautot.append(Auto(rekisteritunnus, huippunopeus))

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










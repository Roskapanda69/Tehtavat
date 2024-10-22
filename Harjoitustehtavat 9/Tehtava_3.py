# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5)
# kasvattaa kuljetun matkan lukemaan 2090 km.

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

auto1=Auto("ABC - 123", 142, 0, 2000)
auto1.kiihdytys(60)
auto1.kulje(1.5)

print(f'Auto on kulkenut : {auto1.kuljettu_matka} km.')

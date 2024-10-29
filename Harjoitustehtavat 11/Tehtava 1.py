# Toteuta seuraava luokkahierarkia Python-kielellä:
# Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
# Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot,
# joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja
# Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.
from time import process_time


class Julkaisu:
    def __init__(self,name):
        self.name = name

    def tulosta_tiedot(self):
        print(f'{self.name}')

class Kirja(Julkaisu):
    def __init__(self,name, kirjoittaja, sivunumero ):
        self.kirjoittaja = kirjoittaja
        self.sivunumero = f'{sivunumero} sivua'
        super().__init__(name)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'{self.kirjoittaja}')
        print(f'{self.sivunumero}')
        print()

class Lehti(Julkaisu):
    def __init__(self,name, paatoimittaja ):
        self.paatoimittaja = paatoimittaja
        super().__init__(name)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'{self.paatoimittaja}')
        print()

jannatjulkasut = []

jannatjulkasut.append(Lehti('Aku Ankka', 'Aki Hyypä'))
jannatjulkasut.append(Kirja('Hytti n:o 6 ', 'Rosa Linksom', 200))

for i in jannatjulkasut:
    i.tulosta_tiedot()
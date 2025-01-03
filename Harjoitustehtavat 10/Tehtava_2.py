# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

class Hissi:
    def __init__(self, name, kerros, alin, ylin):
        self.name = name
        self.kerros = 1
        self.alin = alin
        self.ylin = ylin

    def kerros_ylos(self):
        self.kerros += 1
        return

    def kerros_alas(self):
        self.kerros -= 1
        return

    def siirry_kerrokseen(self, kerrokseen):
        if kerrokseen > self.kerros:
            for i in range(kerrokseen-self.kerros):
                self.kerros_ylos()
                #if self.kerros > self.ylin:
                    #self.kerros = self.ylin
                print(f'*ding* {self.kerros}')


        if kerrokseen < self.kerros:
            for i in range(self.kerros-kerrokseen):
                self.kerros_alas()
                #if self.kerros < self.alin:
                    #self.kerros = self.alin
                print(f'*ding* {self.kerros}')

class Talo:
    def __init__(self, name, hissimaara, alintalossa, ylintalossa ):
        self.name = name
        self.hissimaara = hissimaara
        self.alintalossa = alintalossa
        self.ylintalossa = ylintalossa
        self.hissit = []
        for i in range(hissimaara):
            self.hissit.append(Hissi(i, kerros = 1, alin = alintalossa, ylin = ylintalossa))

    def aja_hissia(self, hissii, kerros):
        self.hissit[hissii-1].siirry_kerrokseen(kerros)




talo1= Talo("talola1", 2, 1, 10)
talo1.aja_hissia(1, 2)
talo1.aja_hissia(2, 5)
talo1.aja_hissia(2, 3)
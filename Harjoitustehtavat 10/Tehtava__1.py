#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman
# ja ylimmän kerroksen numeron. Hissillä on metodit
# siirry_kerrokseen, kerros_ylös ja kerros_alas.
# Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
# että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä yhden kerroksen
# ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen
# ja sen jälkeen takaisin alimpaan kerrokseen.

class Hissi:
    def __init__(self,name , kerros = 1 , alin = 1, ylin = 10 ):
        self.name = name
        self.kerros = kerros
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


hissi = Hissi('H')
hissi.siirry_kerrokseen(9)
hissi.siirry_kerrokseen(7)
hissi.siirry_kerrokseen(2)

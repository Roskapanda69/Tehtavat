# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math


def cheappizza(hinta, halkaisi,):
    return hinta/((math.pi*((halkaisi/2)**2))/100)


halkaisi1= float(input("Anna ekan pizzan halkaisija senttimetreinä OwO: "))
hinta1= float(input("Anna ekan pizzan hinta OwO: "))
halkaisi2= float(input("Anna tokan pizzan halkaisija senttimetreinä OwO: "))
hinta2= float(input("Anna tokan pizzan hinta OwO: "))


pizza1=cheappizza(hinta1,halkaisi1)
pizza2=cheappizza(hinta2,halkaisi2)

if pizza1<pizza2:
    print(f"Eka pitsa {pizza1:0.2f} e/m ja se on {pizza2-pizza1:0.2f} e halvempi.")
if pizza2<pizza1:
    print(f"Tokan pitsa {pizza2:0.2f} e/m ja se on {pizza1-pizza2:0.2f} e halvempi.")
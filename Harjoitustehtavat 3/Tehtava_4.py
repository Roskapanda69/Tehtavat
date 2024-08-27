#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä.
#Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi = int(input(f"Anna vuosiluku: "))

if vuosi%100 == 0 and vuosi%400 == 0 and not vuosi%4==0:
    print(f"{vuosi} on karkausvuosi")

elif vuosi%4 ==0 and not (vuosi%100 == 0 and vuosi%400):
    print(f"{vuosi} on karkausvuosi")


else:
    print(f"{vuosi} ei ole karkausvuosi")
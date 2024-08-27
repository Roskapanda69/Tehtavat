#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä
#antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuumat=float(input("Anna tuumat: "))
while tuumat>=0:
    print(f"{tuumat} tuumaa on {tuumat*2.54}cm.")
    tuumat = float(input("Anna tuumat: "))
print(f"Negatiivinen tuuma :'( end")
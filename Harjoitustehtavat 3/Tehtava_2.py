
#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen
# kuvauksen alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.
    #LUX on parvekkeellinen hytti yläkannella.
    #A on ikkunallinen hytti autokannen yläpuolella.
    #B on ikkunaton hytti autokannen yläpuolella.
    #C on ikkunaton hytti autokannen alapuolella.
#Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

hyttiluokka = input(f"Anna hyttiluokka: ")

if hyttiluokka== "LUX":
    print(f"LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka== "A":
    print(f"A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka== "B":
    print(f"B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka== "C":
    print(f"C on ikkunaton hytti autokannen alapuolella.")
else:
    print(f"Virheellinen hyttiluokka.")
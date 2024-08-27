#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
    #Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
    #Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input(f"Anna sukupuoli: ")


if sukupuoli == "Nainen":
    hemo = int(input(f"Anna hemoglobiiniarvo (g/l): "))
    if 117<= hemo <=175:
        print(f"Hemoglobiiniarvo on normaali.")
    elif hemo<117:
        print(f"Hemoglobiiniarvo on alhainen.")
    elif hemo>175:
        print(f"Hemoglobiiniarvo on korkea.")

if sukupuoli == "Mies":
    hemo = int(input(f"Anna hemoglobiiniarvo (g/l): "))
    if 134<= hemo <=195:
        print(f"Hemoglobiiniarvo on normaali.")
    elif hemo<134:
        print(f"Hemoglobiiniarvo on alhainen.")
    elif hemo>195:
        print(f"Hemoglobiiniarvo on korkea.")

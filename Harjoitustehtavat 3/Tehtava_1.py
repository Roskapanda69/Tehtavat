#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

pituus= float(input(f"Anna kuhan pituus sentteinä: "))
if pituus<37:
              print(f"Laske kuha järveen. Kuha on {37-pituus}cm liian lyhyt.")
else:
    print(f"Kuha on täysimittainen.")
#Arvotaan neliön B sisälle suuri määrä satunnaisissa kohdissa olevia pisteitä, esimerkiksi miljoona.
#Olkoon N tämä pisteiden kokonaismäärä. Jokaisesta neliön B sisään arvotusta pisteestä testataan vuorollaan,
#jääkö se myös yksikköympyrän A sisälle. Olkoon n ympyrän sisälle jäävien pisteiden kokonaismäärä. Nyt pätee n/N≈π/4,
#josta saadaan π≈4n/N. Kirjoita ohjelma, joka kysyy arvottavien pisteiden määrän käyttäjältä ja toteuttaa piin likiarvon
#laskennan edellä kuvatulla menetelmällä. Lopuksi ohjelma tulostaa piin likiarvon käyttäjälle. (Huomaa, että jokaisesta
#arvotusta pisteestä (x,y) on helppoa testata onko se yksikköympyrän A sisällä:
#riittää testata, toteuttaako piste epäyhtälön x^2+y^2<1.)

import random
import math

kokonaismaara = int(input(f"Anna arvottavien pisteiden määrä: "))
sisa=0
koko = kokonaismaara


while (4 * sisa / koko <= math.pi ):
    x_dot = random.uniform( -1, 1)
    y_dot = random.uniform(-1, 1)
    if (x_dot**2+y_dot**2<2):
        sisa += 1
else:
    print(f"Piin likiarvo on {4*sisa/koko} UwU")






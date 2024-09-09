# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.

vuodenajat=("kevät", "kesä", "syks", "talvi")

kuukausi = int(input("Anna kuukauden numero UwU : "))

def vuodenajatus():
    if kuukausi <=2 or kuukausi ==12:
        print(f"{kuukausi} kuuluu vuodenaikaan {vuodenajat[3]} ")
    if kuukausi <=5 and not kuukausi <=2:
        print(f"{kuukausi} kuuluu vuodenaikaan {vuodenajat[0]} ")
    if kuukausi <= 8 and not kuukausi <=5:
        print(f"{kuukausi} kuuluu vuodenaikaan {vuodenajat[1]} ")
    if kuukausi <= 11 and not kuukausi <= 8:
        print(f"{kuukausi} kuuluu vuodenaikaan {vuodenajat[2]} ")
    return

vuodenajatus()



#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luku = input(f"Anna luku: ")

if luku !="":
    iso = luku
    pieni = luku
    if luku > iso:
        iso = luku
    elif luku < pieni:
        pieni = luku

    while luku !="":
        luku = input(f"Anna luku: ")
        if luku =="":
            break
        if luku > iso:
            iso = luku
        elif luku < pieni:
            pieni = luku

    print(f"{iso} on suurin luku ja {pieni} on pienin luku.")

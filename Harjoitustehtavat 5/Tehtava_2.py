#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi
# suurinta suuruusjärjestyksessä suurimmasta alkaen.
#Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

lukuja = []

syote= input(f"Anna lukku tai paina Enter lopettaaksi UwU : ")

while syote.isdigit():
    lukuja.append(int(syote))
    syote= input(f"Anna lukku tai paina Enter lopettaaksi UwU : ")

if syote=="":
    lukuja.sort(reverse=True)
    print(f"{lukuja[:5]}")
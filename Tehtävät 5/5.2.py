#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää
# tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi
# suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden lajittelujärjestyksen
# voi kääntää antamalla sort-metodille argumentiksi reverse=True.

syote = int(input("Syötä haluamiasi lukuja. Kun et halua enää syöttää lukuja, paina Enter.: "))
luvut = []

while syote != "":
    syote = int(syote)
    if syote != "":
        luvut.append(syote)
        syote = input("Anna uusi luku tai paina Enter: ")
    if syote == "":
        break

tulos = sorted(luvut, reverse=True)
print(f"Syöttämäsi luvut viiden ensimmäisen luvun osalta suuruutsjärjestyksessä ovat: {tulos[:5]}")

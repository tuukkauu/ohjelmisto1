nimet = set()
syote = input("Syötä haluamiasi nimiä. Kun haluat lopettaa, paina pelkkä Enter.: ")

while syote != "":
    if syote not in nimet:
        nimet.add(syote)
        print("Uusi nimi")
    syote = input("Anna nimi: ")
    if syote in nimet:
        print("Aiemmin syötetty")

if syote == "":
    for syote in nimet:
        print(syote)

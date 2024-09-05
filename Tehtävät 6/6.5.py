kaikki = []
list = []

luvut = int(input("Syötä haluamiasi kokonaislukuja, ohjelma palauttaa listan parilliset luvut.: "))

def parilliset(lista):
    for i in lista:
        if i % 2 == 1:
            lista.remove(i)
    return lista

while luvut:
    if luvut != "":
        luvut = int(luvut)
        list.append(luvut)
        kaikki.append(luvut)
    luvut = input("Syötä uusi luku: ")

tulos = parilliset(list)
print(f"Alkuperäinen lista: {kaikki}")
print(f"Parillisten lukujen lista: {tulos}")

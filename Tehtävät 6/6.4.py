list = []

luvut = int(input("Syötä kokonaislukuja, joiden summan ohjelma tulostaa: "))

def summa(lista):
    sum = 0
    for i in lista:
        sum += i
    return sum

while luvut:
    if luvut != "":
        luvut = int(luvut)
        list.append(luvut)
    luvut = input("Syötä uusi luku: ")

tulos = summa(list)
print(tulos)

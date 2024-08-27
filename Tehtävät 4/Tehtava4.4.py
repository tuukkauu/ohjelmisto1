import random

arvaus = int(input("Syötä arvaus: "))
arvo = random.randint(1, 10)

while arvo:
    if arvaus > arvo:
        print("Liian suuri arvaus.")

    elif arvaus < arvo:
        print("Liian pieni arvaus.")

    elif arvaus == arvo:
        print("Oikein.")
        break

    arvaus = int(input("Syötä uusi arvaus: "))
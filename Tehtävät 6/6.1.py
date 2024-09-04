import random

def arpa():
    ran = random.randint(1, 6)
    return ran

while arpa:
    tulos = arpa()

    if tulos == 6:
        print(tulos)
        break
    elif tulos < 6:
        print(tulos)
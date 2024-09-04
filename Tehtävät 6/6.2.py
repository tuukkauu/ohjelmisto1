import random

def arpa(numero):
    run = random.randint(1, numero)
    return run

tahko = int(input("Montako tahkoa haluat noppaan? "))

while True:
    num = arpa(tahko)

    if num == tahko:
        print(num)
        break

    else:
        print(num)
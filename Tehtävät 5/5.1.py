import random

maara = int(input("Anna heitettävien arpakuutioiden lukumäärä: "))
summa = 0
for n in range (maara):
    num = random.randint(1, 6)
    summa = summa + num

print(f"Silmälukujen summa on: {summa}")
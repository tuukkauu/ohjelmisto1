import math

vuosi = int(input("Anna vuosiluku: "))

if vuosi % 4 == 0 and vuosi % 100 != 0:
    print("Antamasi vuosi on karkausvuosi.")
elif vuosi % 100 == 0 and vuosi % 400 == 0 and vuosi % 4 == 0:
    print("Antamasi vuosi on karkausvuosi.")
else:
    print("Antamasi vuosi ei ole karkausvuosi.")
import math

def pizza(muunnin, hinta):
    metri = muunnin / 100
    r = metri / 2
    ala = math.pi * r ** 2
    eur_nelio = hinta / ala
    return eur_nelio

print("Verrataan kahden pizzan hintoja.")
sentit1 = float(input("Syötä ensimmäisen pizzan halkaisija senttimetreinä: "))
eurot1 = float(input("Syötä ensimmäisen pizzan hinta euroina: "))

pizza1 = pizza(sentit1, eurot1)
print(f"Ensimmäisen pizzan heliöhinta on {pizza1:.2f} euroa.")

sentit2 = float(input("Syötä toisen pizzan halkaisija senttimetreinä: "))
eurot2 = float(input("Syötä toisen pizzan hinta euroina: "))

pizza2 = pizza(sentit2, eurot2)
print(f"Toisen pizzan neliöhinta on {pizza2:.2f} euroa.")

if pizza1 < pizza2:
    print("Siispä ensimmäinen pizza antaa enemmän vastinetta rahalle.")

if pizza2 < pizza1:
    print("Siispä toinen pizza antaa enemmän vastinetta rahalle.")

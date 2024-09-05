maara = int(input("Syötä luku gallonoissa, saat vastauksen litroina: "))

def muunnin(gallona):
    bensa = float(gallona) * 3.785
    return bensa

while muunnin(maara) > 0:
        print(f"Antamasi luku gallonoissa on {muunnin(maara):.3f} litraa.")
        maara = int(input("Syötä uusi luku gallonoissa: "))
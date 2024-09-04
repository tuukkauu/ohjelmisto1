maara = int(input("Syötä luku gallonoissa, saat vastauksen litroina: "))

def muunnin(gallona):
    bensa = gallona / 3.785
    return bensa

arvo = muunnin(maara)
print(f"Antamasi luku gallonoissa on {arvo:.2f} litraa.")
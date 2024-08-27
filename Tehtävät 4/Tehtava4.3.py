luku = input("Syötä luku tai jätä tyhjäksi. Tällöin ohjelma antaa syöttämistäsi luvuista pienimmän ja suurimman.: ")
if not luku:
    print("Ohjelma tarvitsee lukuja toimiakseen.")

lukumin = luku
lukumax = luku

while luku:
    lukumax = float(lukumax)
    lukumin = float(lukumin)
    luku = float(luku)
    if luku < lukumin:
        lukumin = luku
    elif luku > lukumax:
        lukumax = luku


    luku = input("Syötä uusi luku: ")
    if not luku:
        print(f"Suurin ja pienin antamasi luvut ovat: {lukumin} ja {lukumax}")
        break

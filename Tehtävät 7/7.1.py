vuodenajat = ("talvi", "kevat", "kesa", "syys")

syote = int(input("Syötä kuukausi numeroina (1 - 12): "))

if syote >= 3 and syote <= 5:
    print(f"{syote}. kuukausi kuuluu {vuodenajat[1]}-kuukausiin.")

if syote >=6 and syote <= 8:
    print(f"{syote}. kuukausi kuuluu {vuodenajat[2]}-kuukausiin.")

if syote >= 9 and syote <= 11:
    print(f"{syote}. kuukausi kuuluu {vuodenajat[3]}-kuukausiin.")

if syote >= 1 and syote <= 2 or syote == 12:
    print(f"{syote}. kuukausi kuuluu {vuodenajat[0]}-kuukausiin.")


"""
talvi = 12, 1, 2
kevat = 3, 4, 5
kesa = 6, 7, 8
syksy = 9, 10, 11
"""
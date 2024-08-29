user = input("Syötä käyttäjätunnus: ")
password = input("Syötä salasana: ")

kayttis = "python"
salis = "rules"
kerrat = 1

while user:
    kayttis = "python"
    salis = "rules"

    if kayttis == user and salis == password:
        print("Tervetuloa")
        break
    if user != kayttis and password != salis:
        print("Käyttäjätunnus tai salasana on virheellinen.")
    elif password != salis and user == kayttis:
        print("Käyttäjätunnus tai salasana on virheellinen.")
    elif password == salis and user != kayttis:
        print("Käyttäjätunnus tai salasana on virheellinen.")

    kerrat = kerrat + 1
    if kerrat > 5:
        print("Pääsy evätty")
        break
    user = input("Syötä käyttäjätunnus: ")
    password = input("Syötä salasana: ")




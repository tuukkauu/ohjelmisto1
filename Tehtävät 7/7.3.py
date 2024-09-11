def uusiasema(lentoasemat):
    uusiI = input("Kirjoita lentoaseman ICAO-tunnus: ")
    uusiL = input("Kirjoita lentoaseman nimi: ")
    return uusiI, uusiL

#11 randomia lentoasemaa Suomessa
lentoasemat = {"EFHK":"Helsinki-Vantaan lentoasema",
               "EFNU":"Nummelan lentokeskus",
               "EFIV":"Ivalon lentoasema",
               "EFET":"Enontekilön lentoasema",
               "EFJO":"Joensuun lentoasema",
               "EFKI":"Kajaanin lentoasema",
               "EFKT":"Kittilän lentoasema",
               "EFKS":"Kuusamon lentoasema",
               "EFTU":"Turun lentoasema",
               "EFVA":"Vaasan lentoasema",
               "EFOU":"Oulun lentoasema"}


print("OHJEET: Tämä ohjelma on lentoasematietojen hakemista ja tallentamista varten.")
print("OHJEET: Voit syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tietoja tai lopetta painamalla Enter.")
kysymys = input("Kirjoita 'lentoasema', jos haluat syöttää uuden lentoaseman tiedot. Kirjoita 'haku', jos haluat hakea valmiiden lentoasemien tietoja. ")

while kysymys != "":
    if kysymys == "lentoasema":
        avain, arvo = uusiasema(lentoasemat)
        lentoasemat[avain] = arvo
        kysymys = input("Kirjoita 'lentoasema', jos haluat syöttää uuden lentoaseman tiedot. Kirjoita 'haku', jos haluat hakea valmiiden lentoasemien tietoja. ")
    if kysymys == "haku":
        tunnus = input("Kirjoita lentoaseman ICAO-tunnus: ")
        if tunnus in lentoasemat:
            print(lentoasemat[tunnus])
        kysymys = input("Kirjoita 'lentoasema', jos haluat syöttää uuden lentoaseman tiedot. Kirjoita 'haku', jos haluat hakea valmiiden lentoasemien tietoja. ")
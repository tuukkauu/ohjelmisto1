import mysql.connector

def lentoasema_nimi_sijainti(ICAO_koodi):
    sql = f"SELECT name, municipality FROM airport WHERE ident = %s"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql, (ICAO_koodi,))
    tulos = kursori.fetchall()

    if tulos:
        for asema in tulos:
            print(asema)
    else:
        print("Lentokenttää ei löytynyt kyseisellä ICAO-tunnuksella.")


#pääohjelma
yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="tuukka",
    passwd="Muumilaakso",
    autocommit=True,
    collation = "utf8mb4_general_ci",
)


ICAO = input("Syötä ICAO-tunnus: ")
lentoasema_nimi_sijainti(ICAO)
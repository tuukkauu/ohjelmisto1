import mysql.connector

def all_airport_types_in_count(code):
    sql = f"SELECT airport.type AS airport_type, COUNT(*) AS count FROM airport JOIN country ON airport.iso_country = country.iso_country WHERE country.iso_country = %s GROUP BY airport.type, country.iso_country"
    kursori = yhteys.cursor()
    kursori.execute(sql, (code,))
    tulos = kursori.fetchall()

    if tulos:
        for tunnus in tulos:
            print(tunnus)
    else:
        print("Maata ei tunnistettu kyseisellä maatunnuksella.")


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

country_code = input("Syötä maatunnus, kuten FI: ")
all_airport_types_in_count(country_code)
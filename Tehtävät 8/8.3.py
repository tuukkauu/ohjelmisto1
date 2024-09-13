import mysql.connector
import geopy.distance
from geopy.distance import geodesic

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

def input_country(ICAO):
    sql = f"SELECT airport.latitude_deg, airport.longitude_deg FROM airport where airport.ident = %s;"
    kursori = yhteys.cursor()
    kursori.execute(sql, (ICAO,))
    tulos = kursori.fetchall()
    return tulos

def distance(point_1, point_2):
    distance = geodesic(point_1, point_2).kilometers
    return distance

ICAO1 = input("Syötä ensimmäisen vertailtavan lentokentän ICAO-tunnus: ")
ICAO2 = input("Syötä toisen vertailtavan lentokentän ICAO-tunnus: ")

point1 = input_country(ICAO1)
point2 = input_country(ICAO2)

etaisyys = distance(point1, point2)
print(f"Lentokenttien välinen etäisyys on {etaisyys:.1f}")

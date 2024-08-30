#Kirjoita ohjelma, joka kysyy arvottavien pisteiden määrän käyttäjältä ja toteuttaa
# piin likiarvon laskennan edellä kuvatulla menetelmällä. Lopuksi ohjelma tulostaa piin likiarvon
# käyttäjälle. (Huomaa, että jokaisesta arvotusta pisteestä (x,y) on helppoa testata onko se
# yksikköympyrän A sisällä: riittää testata, toteuttaako piste epäyhtälön x^2+y^2<1.)

import random
import math

maara_N = int(input("Syötä arvottavien pisteiden määrä: "))
count = 0
maara_n = 0

# satunnaispisteiden arpominen:#
# Arvotaan N kappaletta satunnaisia pisteitä neliön B sisään, jonka koordinaatit
# vaihtelevat välillä (-1, -1) ja (1, 1). Jokainen piste voidaan luoda arpomalla kaksi satunnaislukua
# väliltä [-1, 1], jotka edustavat pisteen x- ja y-koordinaatteja.

while count < maara_N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    xy = x ** 2 + y ** 2

    if xy < 1:
        maara_n = maara_n + 1
    count = count + 1
    if count == maara_N:
        print(f"Piin lukuarvo on laskennallisesti: {(4*maara_n)/maara_N}")


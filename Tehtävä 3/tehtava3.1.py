import math

pituus = float(input("Kuhan pituus senttimetreinä: "))

alamitta = 37 - pituus

if pituus < 37:
    print(f"Laske kuha takaisin järveen. Kuha on {alamitta} senttimetriä alamittainen.")
tuuma = float(input("Syöta luku tuumissa: "))

while tuuma >= 0:
    sentti = 2.54
    mitta = float(tuuma) * float(sentti)
    print(f"Luku on {mitta} senttimetriä.")

    tuuma = float(input("Syötä luku tuumissa: "))


sukupuoli = input("Biologinen sukupuoli: ")
arvo = input("hemoglobiiniarvo (g/l): ")
arvo = float(arvo)

if sukupuoli == "mies" and 134<=arvo<=195:
    print("Hemoglobiiniarvo on normaali.")
elif sukupuoli == "mies" and arvo<134:
    print("Hemoglobiiniarvo on alhainen.")
elif sukupuoli == "mies" and arvo>195:
    print("Hemoglobiiniarvo on korkea.")

if sukupuoli == "nainen" and 117<=arvo<=175:
    print("Hemoglobiiniarvo on normaali.")
elif sukupuoli == "nainen" and arvo<117:
    print("Hemoglobiiniarvo on alhainen.")
elif sukupuoli == "nainen" and arvo>175:
    print("Hemoglobiiniarvo on korkea.")


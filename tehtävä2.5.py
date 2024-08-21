import math

leiviskät = input("Anna leiviskät. ")
naulat = input("Anna naulat. ")
luodit = input("Anna luodit. ")

leiviskät = float(leiviskät)*20*32*13.3
naulat = float(naulat)*13.3*32
luodit = float(luodit)*13.3

kokonaismassa = float(leiviskät)+float(naulat)+float(luodit)
kilot = int((float(leiviskät)+float(naulat)+float(luodit))/1000)
grammat = float(kokonaismassa - (kilot*1000))

print("Massa nykymittojen mukaan:")
print(f"{kilot} kilograammaa ja {grammat:.2f} grammaa.")
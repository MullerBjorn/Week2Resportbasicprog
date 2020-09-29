from math import ceil, floor
#floor --> afronden naar beneden
#ceil --> afronden naar boven

score = float(input("Geef uw score op: "))

if round(score) < 10:
    print("Helaas, u bent niet geslaagd")
else:
    print("U bent geslaagd")
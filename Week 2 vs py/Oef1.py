#vraag 2 getallen aan gebruiker

getal_a = int(input("Wat is uw eerste getal?: "))
getal_b = int(input("Wat is uw tweede getal?: "))

if getal_a == getal_b:
    print(f"Beide getallen ({getal_a}) zijn gelijk")
else:
    print(f"Beide getallen ({getal_a}) en ({getal_b}) zijn niet gelijk")

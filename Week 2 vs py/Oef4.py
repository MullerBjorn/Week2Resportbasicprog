#week 2 oef 4

leeftijd_hond = int(input("Geef de leeftijd van de hond op: "))

if leeftijd_hond < 0:
    print("Ongeldige leeftijd")
elif leeftijd_hond == 0:
    print("De hond is tussen de 0 en 12 maanden oud in mensenmaanden")
elif leeftijd_hond == 1:
    print("Deze leeftijd komt overeen met 14 mensenjaren")
elif leeftijd_hond == 2:
    print("Deze leeftijd komt overeen met 22 mensenjaren")
else:
    print(f"Deze leeftijd komt overeen met {22 + (leeftijd_hond - 2) *5} mensenjaren")

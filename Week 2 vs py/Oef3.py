#geboortejaar opvragen
#indien 18 of meer --> Alcohol, anders niet
from datetime import datetime

geboortejaar = int(input("Wat is uw geboortejaar? "))
geboortemaand = int(input("Wat is uw geboortemaand (in cijfers)?"))

huidig_maand = datetime.now().month
huidig_jaar = datetime.now().year

# print(f"{huidig_jaar}")

leeftijd = huidig_jaar - geboortejaar

if leeftijd > 18:
    #Je bent sowieso ouder dan 18 dit jaar.
    print("Je bent volwassen! Geniet, maar drink met mate(n)")
    
elif leeftijd == 18:
    #Je bent nog geen 18
    if geboortemaand < huidig_maand:
        #Ben je al jarig geweest? Drinken!
        print("Je bent volwassen! Geniet, maar drink met mate(n)")
         #Not niet jarig geweest? Nuchter avondje..
    else:
        print("Je bent te jong, gelieve terug te keren als u volwassen bent")
    
else:
     print("Je bent te jong, gelieve terug te keren als u volwassen bent")

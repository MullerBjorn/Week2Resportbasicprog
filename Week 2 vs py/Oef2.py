#vraag een geheel getal op
#is dit even of oneven + boodschap

getal_c = int(input("Geef een geheel getal op: "))
rest_na_deling = getal_c % 2
# ook mogelijk
# if getal % 2 != 0:


if rest_na_deling == 0:
    print(f"Het getal {getal_c} is een even getal")
else: 
    print(f"Het getal {getal_c} is een oneven getal")


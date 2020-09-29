#deze functie heeft 1 parameter, nl naam
def print_welkom (naam):
    print(f"Welkom {naam}!")
    print("Neem een plaats in het lokaal.")

naam_student = input("Wat is uw naam?: ")
print_welkom(naam_student)
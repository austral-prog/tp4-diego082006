def leap_year():
    year = int(input("Ingrese un año: "))

    # Un año es bisiesto si es divisible por 4, excepto si es divisible por 100
    # A menos que también sea divisible por 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")


leap_year()

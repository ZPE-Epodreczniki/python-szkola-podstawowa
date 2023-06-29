# Przykład 1
liczba = 16
czy_parzysta = liczba % 2
if czy_parzysta == 0:
    print("Liczba jest parzysta")
    if liczba > 20:
        print("Liczba jest większa niż 20")
    if liczba > 15:
        print("Liczba jest większa niż 15")
    if liczba > 10:
        print("Liczba jest większa niż 10")

# Efekt wykonania
# Liczba jest parzysta
# Liczba jest większa niż 15
# Liczba jest większa niż 10



# Przykład 2
liczba = 16
czy_parzysta = liczba % 2
if czy_parzysta == 0:
    print("Liczba jest parzysta")
    if liczba > 20:
        print("Liczba jest większa niż 20")
        if liczba > 15:
            print("Liczba jest większa niż 15")
            if liczba > 10:
                print("Liczba jest większa niż 10")

# Efekt wykonania
# Liczba jest parzysta
from random import randint
liczba = randint(3, 300)
czy_parzysta = liczba % 2
if czy_parzysta == 0:
    print("To liczba parzysta")
else:
    if liczba > 150:
        print("Liczba w drugiej połówce")
    else:
        print("Liczba w pierwszej połówce")
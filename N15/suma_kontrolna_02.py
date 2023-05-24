def wartosc_znaku(znak, pozycja):
    wartosc = ord(znak) * pozycja
    if znak in ("eęyuioóaąEĘYUIOÓAĄ"):
        wartosc += 1
    return wartosc

informacja = input("Podaj informację: ")
suma_kontrolna = 0
pozycja = 1

for znak in informacja:
    suma_kontrolna += wartosc_znaku(znak, pozycja)
    pozycja += 1

print(f"Obliczona suma kontrolna wynosi {suma_kontrolna}")

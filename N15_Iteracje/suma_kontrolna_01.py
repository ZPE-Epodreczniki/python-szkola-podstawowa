def wartosc_znaku(znak, pozycja):
    return ord(znak) * pozycja

informacja = input("Podaj informację: ")
suma_kontrolna = 0
pozycja = 1

for znak in informacja:
    suma_kontrolna += wartosc_znaku(znak, pozycja)
    pozycja += 1

print(f"Obliczona suma kontrolna wynosi {suma_kontrolna}")

def oblicz_nwd(a, b):
    licznik = 0
    while b > 0:
        r = a % b
        a = b
        b = r
        print(r, a, b)
        licznik = licznik + 1
    print("Liczba powtórzeń:", licznik)
    return a


def oblicz_nww(a, b):
    # NWW(a, b) to największa wspólna wielokrotność liczb a i b
    # NWW = a * b / NWD(a, b)
    nww = a * b / oblicz_nwd(a, b)
    return nww

# pobierz liczbę całkowitą a
a = int(input("Podaj liczbę a: "))

# pobierz liczbę całkowitą b
b = int(input("Podaj liczbę b: "))

# wywołanie funkcji i przypisanie zwróconego wyniku
d = oblicz_nwd(a, b)

# wydrukowanie tekstu: NWD( a , b ) = d
#print("NWD(", a, ",", b,") = ", d)
print(a, b, d)

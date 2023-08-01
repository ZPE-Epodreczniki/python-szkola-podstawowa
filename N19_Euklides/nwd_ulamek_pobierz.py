def pobierz_liczbe(komunikat):
    liczba = int(input(komunikat))
    while liczba <= 0:
        print("Błąd: podaj liczbę dodatnią większą od 0.")
        liczba = int(input(komunikat))
    return liczba

def oblicz_nwd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
        print("r =", r, "a =", a, "b =", b)
    return a

# pobierz licznik
licznik = pobierz_liczbe("Podaj licznik: ")

# pobierz mianownik
mianownik = pobierz_liczbe("Podaj mianownik: ")

# wywołanie funkcji i przypisanie zwróconego wyniku
d = oblicz_nwd(licznik, mianownik)

# wypisanie tekstu: NWD( licznik , mianownik ) = d
print("NWD(", licznik, ",", mianownik,") = ", d)

# wypisanie ułamka przed i po skróceniu
print("Ułamek:", licznik, "/", mianownik, "po skróceniu:", licznik//d, "/", mianownik//d)

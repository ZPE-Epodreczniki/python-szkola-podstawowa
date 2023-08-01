def oblicz_nwd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
        print("r =", r, "a =", a, "b =", b)
    return a


# pobierz licznik
while (licznik := int(input("Podaj licznik: "))) <= 0:
    print("Błąd: licznik powinien być większy od 0.")

# pobierz mianownik
while mianownik := int(input("Podaj mianownik: ")) <= 0:
    print("Błąd: mianownik powinien być większy od 0.")

# wywołanie funkcji i przypisanie zwróconego wyniku
d = oblicz_nwd(licznik, mianownik)

# wypisanie tekstu: NWD( licznik , mianownik ) = d
print("NWD(", licznik, ",", mianownik, ") = ", d)

# wypisanie ułamka przed i po skróceniu
if d > 1:
    print("Ułamek:", licznik, "/", mianownik)
    print("Po skróceniu:", licznik//d, "/", mianownik//d)
else:
    print("Ułamka nie da się skrócić.")

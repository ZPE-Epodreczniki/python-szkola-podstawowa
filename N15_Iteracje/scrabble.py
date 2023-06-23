def licz_scrabble(slowo):
    punkty = 0
    litery = len(slowo)
    for znak in slowo:

        if znak in "ęóąśłżźćń":
            punkty += 5
        elif znak in "eyuioa":
            punkty += 2
        else:
            punkty += 1

    if litery > 10:
        punkty += 10

    if litery > 15:
        punkty += 20

    return f"{slowo} - {punkty} pkt"


print(licz_scrabble("apartamentowiec"))
print(licz_scrabble("żaba"))
print(licz_scrabble("ząbkowanie"))
print(licz_scrabble("przykładowe"))

# przykładowe wyniki
# apartamentowiec - 32 pkt
# żaba - 10 pkt
# ząbkowanie - 18 pkt
# przykładowe - 29 pkt

################################################################

def szukaj_element_for(lista, szukana):
    indeks = -1
    i = 0

    for element in lista:
        if element == szukana and indeks == -1:
            indeks = i
        i += 1

    return f"Liczba {szukana} - indeks {indeks} / {i}"
print("Wersja for")
print(szukaj_element_for([2, 3, 3, 3, 2, 4, 6, 7, 7, 8, 2, 4], 4))
print(szukaj_element_for([2, 3, 3, 3, 2, 4, 6, 7, 7, 8, 2, 4], 9))

def szukaj_element_while(lista, szukana):
    indeks = -1
    i = 0
    dlugosc = len(lista) - 1

    while indeks == -1:
        if lista[i] == szukana:
            indeks = i
        i += 1
        if i == dlugosc:
            break


    return f"Liczba {szukana} - indeks {indeks} / {i}"

print("Wersja while")
print(szukaj_element_while([2, 3, 3, 3, 2, 4, 6, 7, 7, 8, 2, 4], 4))
print(szukaj_element_while([2, 3, 3, 3, 2, 4, 6, 7, 7, 8, 2, 4], 9))

# przykładowe wyniki
# Wersja for
# Liczba 4 - indeks 5
# Liczba 9 - indeks -1
# Wersja while
# Liczba 4 - indeks 5
# Liczba 9 - indeks -1

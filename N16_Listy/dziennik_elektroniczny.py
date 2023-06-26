# definiujemy pustą listę przedmiotów i ocen w tych przedmiotach
lista_przedmiotow = []
oceny_przedmiotow = []

def dodaj_oceny(nazwa_przedmiotu):
    # tworzymy zmienną zawierającą pustą listę
    oceny = []
    print(f"Dodajemy oceny dla przedmiotu: {nazwa_przedmiotu}.")

    # uruchamiamy pętlę warunkową
    # wykona się zawsze, aż do podania oceny 0
    while True:
        # element wczytamy z klawiatury
        ocena = input("Podaj ocenę (1-6): ")
        if ocena == "0":
            break
        elif ocena in ["1", "2", "3", "4", "5", "6"]:
            # dodamy tylko oceny z zakresu 1-6
            oceny.append(int(ocena))
            # wewnątrz dodamy do listy kolejny element,
            # zamienimy wprowadzoną ocenę z typy str na int
            # używamy wbudowanego w Pythnie sposobu - metody LISTA.append()

    # tutaj po słowie kluczowym break będzie wykonywana instrukcja poza pętlą
    return oceny


## ===== GŁÓWNY blok kodu programu ======

# uruchamiamy pętlę warunkową
# wykona się zawsze, aż do podania nazwy przedmiotu KONIEC, wielkość liter
# nie ma tu znaczenia, metoda upper() zamienia wprowadzone znaki na wielkie litery
while True:
    # element wvczytamy z klawiatury
    przedmiot = input("Podaj nazwę przedmiotu: ")
    if przedmiot.upper() == "KONIEC":
        break
    # wewnątrz dodamy do listy kolejny element
    # używamy wbudowanego w Pythnie sposobu - metody LISTA.append()
    lista_przedmiotow.append(przedmiot)
    # oraz dodamy oceny, wykorzystując funkcję
    oceny_przedmiotow.append(dodaj_oceny(przedmiot))


# tutaj po słowie kluczowym break będzie wykonywana instrukcja poza pętlą
print(f"Wprowadzone przedmioty: {lista_przedmiotow}.")

# sprawdzimy ilość wprowadzonych przedmiotów
ilosc_przedmiotow = len(lista_przedmiotow)

# i wyświetlamy wprowadzone informacje
for kolejny_indeks in range(ilosc_przedmiotow):
    nazwa_przedmiotu = lista_przedmiotow[kolejny_indeks]
    oceny_przedmiotu = oceny_przedmiotow[kolejny_indeks]
    print(f"Dla przedmiotu {nazwa_przedmiotu} zapamiętane oceny to: {oceny_przedmiotu}")

"""
Podaj nazwę przedmiotu: matematyka
Dodajemy oceny dla przedmiotu: matematyka.
Podaj ocenę (1-6): 2
Podaj ocenę (1-6): 3
Podaj ocenę (1-6): 4
Podaj ocenę (1-6): 9
Podaj ocenę (1-6): 3
Podaj ocenę (1-6): 0
Podaj nazwę przedmiotu: informatyka
Dodajemy oceny dla przedmiotu: informatyka.
Podaj ocenę (1-6): 6
Podaj ocenę (1-6): 5
Podaj ocenę (1-6): 6
Podaj ocenę (1-6): 6
Podaj ocenę (1-6): 5
Podaj ocenę (1-6): 0
Podaj nazwę przedmiotu: koniec
Wprowadzone przedmioty: ['matematyka', 'informatyka'].
Dla przedmiotu matematyka zapamiętane oceny to: [2, 3, 4, 3]
Dla przedmiotu informatyka zapamiętane oceny to: [6, 5, 6, 6, 5]
"""

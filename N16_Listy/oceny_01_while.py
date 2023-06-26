# tworzymy zmienną zawierającą pustą listę
oceny_przedmiotu = []
print(f"Początkowo lista jest pusta: {oceny_przedmiotu}.")

# uruchamiamy pętlę warunkową
# wykona się zawsze, aż do podania oceny 0
while True:
    # element wczytamy z klawiatury
    ocena = input("Podaj ocenę (1-6): ")
    if ocena == "0":
        break
    elif ocena in ["1", "2", "3", "4", "5", "6"]:
        # dodamy tylko oceny z zakresu 1-6
        oceny_przedmiotu.append(int(ocena))
        # wewnątrz dodamy do listy kolejny element,
        # zamienimy wprowadzoną ocenę z typy str na int
        # używamy wbudowanego w Pythnie sposobu - metody LISTA.append()

# tutaj po słowie kluczowym break będzie wykonywana instrukcja poza pętlą
print(f"Wprowadzone oceny to: {oceny_przedmiotu}.")


"""
Początkowo lista jest pusta: [].
Podaj ocenę (1-6): 2
Podaj ocenę (1-6): 8
Podaj ocenę (1-6): 4
Podaj ocenę (1-6): 4
Podaj ocenę (1-6): 5
Podaj ocenę (1-6): 3
Podaj ocenę (1-6): 5
Podaj ocenę (1-6): 0
Wprowadzone oceny to: [2, 4, 4, 5, 3, 5].
"""

# tworzymy zmienną zawierającą pustą listę
lista_przedmiotow = []
print(f"Początkowo lista jest pusta: {lista_przedmiotow}.")

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
    # wyświetlimy za każdym razem jej zawartość
    print(f"Elementy listy to: {lista_przedmiotow}.")

# tutaj po słowie kluczowym break będzie wykonywana instrukcja poza pętlą
print(f"Końcowe elementy listy to: {lista_przedmiotow}.")

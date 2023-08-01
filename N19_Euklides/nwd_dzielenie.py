# pobierz liczbę całkowitą a
a = int(input("Podaj liczbę a: "))

# pobierz liczbę całkowitą b
b = int(input("Podaj liczbę b: "))

licznik = 0
# pętla obliczająca NWD
while b > 0:
    licznik += 1
    r = a % b
    print(f"Powtórzenie {licznik}: r = {a} % {b} =", r, ", a =", b, ", b =", r)
    a = b
    b = r

# wypisanie wyniku
print("NWD(a, b) =", a, "Liczba powtórzeń:", licznik)

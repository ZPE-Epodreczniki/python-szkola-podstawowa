from turtle import *


def wielokat(dlugosc, ilosc):
    if ilosc > 360:
        return False

    # jeśli warunek nie jest spełniony, a więc ilosc <= 360
    kat = 360 / ilosc
    for x in range(ilosc):
        fd(dlugosc)
        lt(kat)


dlugosc = int(numinput("Podaj wartość liczby całkowitej.", "Podaj długość boku."))
ilosc = int(numinput("Podaj wartość liczby całkowitej.", "Podaj ilość kątów."))

if 5 <= ilosc <= 20:
    wielokat(dlugosc, ilosc)

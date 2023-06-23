def dziel_lista(lista):
    parzyste = []
    nieparzyste = []
    for element in lista:
        if element % 2 == 0:
            parzyste.append(element)
        else:
            nieparzyste.append(element)
    dl_parzyste = len(parzyste)
    dl_nieparzyste = len(nieparzyste)

    if dl_parzyste == dl_nieparzyste:
        return [0]

    if dl_parzyste > dl_nieparzyste:
        return parzyste
    else:
        return nieparzyste


print(dziel_lista([43, 82, 60, 14, 4, 31]))
print(dziel_lista([35, 79, 47, 31, 81, 76, 53, 55, 86, 66, 48, 27, 68, 75, 25]))
print(dziel_lista([43, 82, 60, 13, 4, 31]))
print(dziel_lista([45, 36, 11, 11, 71, 79, 33, 11, 86, 10, 47]))

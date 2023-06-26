def ile_samoglosek(lista):
    samogloski = "aeiouy"
    ile_sam = 0
    for element in lista:
        if element in samogloski:
            ile_sam += 1

    return ile_sam

print(ile_samoglosek(["a", "x", "g", "e"]))
print(ile_samoglosek(["a", "i", "o", "e"]))
print(ile_samoglosek(["p", "x", "g", "c"]))

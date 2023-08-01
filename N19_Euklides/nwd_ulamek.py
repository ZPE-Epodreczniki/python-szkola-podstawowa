def oblicz_nwd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

a = int(input("Podaj licznik: "))
b = int(input("Podaj mianownik: "))

if a < 1 or b < 1:
    print("Błędne dane!")
    exit()

d = oblicz_nwd(a, b)
print("NWD(", a, ",", b,") = ", d)

if d > 1:
    print("Ułamek:", a, "/", b)
    print("Po skróceniu:", a // d, "/", b // d)
else:
    print("Ułamka nie da się skrócić.")

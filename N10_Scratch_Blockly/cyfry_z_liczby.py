liczba = int(input("Podaj zawartość zmiennej: "))
while liczba > 0:
  cyfra = liczba % 10
  print("Kolejna cyfra to:", cyfra)
  liczba = liczba // 10

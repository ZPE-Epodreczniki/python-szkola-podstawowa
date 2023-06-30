liczba = int(input("Podaj liczbę naturalną: "))
while liczba > 0:
    cyfra = liczba % 10  # modulo, reszta z dzielenia
    print("Najmniej znacząca cyfra liczby", liczba, "to:", cyfra)
    liczba = liczba // 10  # dzielenie całkowite

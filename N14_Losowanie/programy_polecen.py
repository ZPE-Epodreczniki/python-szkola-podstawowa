def losuj():
    from random import randint
    ile_liczb = int(input("Podaj ilość liczb do losowania (od 5 do 10): "))
    for _ in range(ile_liczb):
        print(f"Wartość to {randint(1, ile_liczb)}")

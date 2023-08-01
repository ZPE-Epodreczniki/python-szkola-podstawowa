import math

liczba = None
cyfra = None

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


liczba = text_prompt('Podaj liczbę')
while liczba > 0:
  cyfra = liczba % 10
  print(cyfra)
  liczba = math.floor(liczba / 10)



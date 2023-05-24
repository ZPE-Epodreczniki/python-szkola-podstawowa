from turtle import *

def czesc_szlaczka(dlugosc):   
    pencolor('blue')
    forward(dlugosc)
    right(90)
    pencolor('red')
    forward(dlugosc)
    left(90)
    pencolor('yellow')
    forward(dlugosc)
    left(90)
    pencolor('green')
    forward(dlugosc)
    right(90)


penup()
width(10)
goto(-800,0)
pendown()
for kolejny in range(2, 13):
    czesc_szlaczka(10*kolejny)
        

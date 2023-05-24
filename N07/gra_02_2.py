from random import randint, choice
from turtle import *

def ptak(color):   
    penup()
    poz_x = randint(-200, 200)
    poz_y = randint(-200, 200)
    goto(poz_x, poz_y)
    pencolor(color)
    pendown()
    stamp()
    

for ile in range(60):
    colors = ['orange', 'red', 'pink', 'yellow', 'blue', 'green']
    color = choice(colors)
    ptak(color)

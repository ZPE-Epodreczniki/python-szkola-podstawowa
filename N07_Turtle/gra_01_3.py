from random import choice
from turtle import *

setup(width=900, height=600)
# title("WĄŻ - rysunek pomocniczy")

colors = ['orange', 'red', 'pink', 'yellow', 'blue', 'green']
for x in range(15, 90):
    color = choice(colors)
    pencolor(color)
    width(x / 2)
    forward(x)
    left(20)


exitonclick()

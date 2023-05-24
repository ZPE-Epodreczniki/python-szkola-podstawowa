from random import randint, choice
from turtle import *

def obrecz(x, y, color):   
    penup()
    goto(x, y)
    pencolor(color)
    pendown()
    circle(100)
    
pensize(30)
circles = [
    (-200, 0, 'blue'),
    (-40, 0, 'black'),
    (120, 0, 'red'),
    (-120, -90, 'yellow'),
    (10, -90, 'green')]

for circle_ in circles:
    obrecz(circle_[0], circle_[1], circle_[2])
    

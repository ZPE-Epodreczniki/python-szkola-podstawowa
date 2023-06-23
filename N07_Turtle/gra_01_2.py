from turtle import *

setup(width=900, height=600)
# title("Wielokąt - rysunek pomocniczy")
pu()
goto(0,120)
pd()

width(25)
for bok in range(10):
    forward(60)
    right(360/10)

exitonclick()

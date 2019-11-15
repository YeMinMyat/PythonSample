import turtle
from turtle import *

window = turtle.Screen()
window.bgcolor("green")

color('blue', 'black')
# begin_fill()
while True:
    forward(180)
    left(90)
    right(25)
    # backward(30)
    if abs(pos()) < 1:
        break

# end_fill()
done()
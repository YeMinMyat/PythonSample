import turtle
from turtle import *
window = turtle.Screen()
window.bgcolor("green")

color('blue', 'black')
begin_fill()
while True:
    forward(300)
    left(190)
    backward(190)
    if abs(pos()) < 2:
        break

end_fill()
done()
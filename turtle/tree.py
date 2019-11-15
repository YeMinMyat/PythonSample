import random
import turtle

def tree(size, myTurtle):
	myTurtle.pensize(size / 10)

	if size < random.randint(0,1) * 30:
		myTurtle.color("green")
	else:
		myTurtle.color("brown")

	if size > 5:
		myTurtle.forward(size)
		myTurtle.left(25)
		tree(size - random.randint(10, 20 ), myTurtle)
		myTurtle.right(50)
		tree(size - random.randint(10, 20 ), myTurtle)
		myTurtle.left(25)
		# tree(size - random.randint(10, 20 ), myTurtle)
		# myTurtle.right(50)
		# tree(size - random.randint(10, 20 ), myTurtle)
		# myTurtle.right(25)
		myTurtle.penup()
		myTurtle.backward(size)
		myTurtle.pendown()


window = turtle.Screen()
window.bgcolor("black")

myTurtle = turtle.Turtle()
myTurtle.color("brown", "blue")
myTurtle.left(90)
myTurtle.speed(0)
myTurtle.penup()
myTurtle.setpos(-100,-250)
myTurtle.pendown()

myTurtle2 = turtle.Turtle()
myTurtle2.color("brown", "blue")
myTurtle2.left(90)
myTurtle2.speed(0)
myTurtle2.penup()
myTurtle2.setpos(300,-250)
myTurtle2.pendown()

tree(80, myTurtle)
tree(80, myTurtle2)
window.exitonclick()
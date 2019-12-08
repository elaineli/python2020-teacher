
import turtle
from random import randint


# making the background
turtle.bgcolor('midnight blue')


# code for making a rectangle
def makeRectangle(turtle, color, x, y, width, length):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)


    # fill the above shape
    turtle.end_fill()
    # Reset the orientation of the turtle
    turtle.setheading(0)


# code for making a circle
def makeCircle(turtle, color, x, y, radius):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


# code for making a star
def makeStar(side, color, x, y):
    angle = 139
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()

    for i in range(5):
        turtle.forward(side)
        turtle.right(angle)
        turtle.forward(side)
        turtle.right(72 - angle)

    turtle.end_fill()



stuff = turtle.Turtle()


# making the grass
stuff.speed(7)
makeRectangle(stuff, 'dark sea green', -350, -420, 720, 300)


# making the tree trunk
makeRectangle(stuff, 'saddle brown', -15, -160, 30, 60)


# making the leaves
y = -100
width = 240
stuff.speed(100)
while width > 10:
    width = width - 10
    length = 10
    x = 0 - width/2
    makeRectangle(stuff, "green", x, y, width, length)
    y = y + length
    makeRectangle(stuff, "dark green", x, y, width, length)


# making the star on the tree
stuff.speed(2)
makeStar(15, "yellow", 4, 150)


# making ornaments
stuff.speed(15)
makeCircle(stuff, "magenta", 0, -30, 9)
makeCircle(stuff, "red", 9, -70, 5)
makeCircle(stuff, "light cyan", 0, 0, 7)
makeCircle(stuff, "yellow", -19, 30, 6)
makeCircle(stuff, "hot pink", -40, -90, 7)
makeCircle(stuff, "blue", 20, 60, 8)
makeCircle(stuff, "aquamarine", 50, -80, 4)
makeCircle(stuff, "purple", 53, 20, 4)
makeCircle(stuff, "orange", -43, -50, 4)
makeCircle(stuff, "sky blue", -10, 80, 4)


# making presents
stuff.speed(7)
makeRectangle(stuff, "red", -130, -180, 90, 70)
makeRectangle(stuff, "yellow", -95, -180, 20, 70)
makeRectangle(stuff, "yellow", -130, -150, 90, 20)
makeRectangle(stuff, "spring green", 50, -190, 80, 110)
makeRectangle(stuff, "red", 75, -190, 20, 110)
makeRectangle(stuff, "red", 50, -150, 80, 20)


turtle.done()
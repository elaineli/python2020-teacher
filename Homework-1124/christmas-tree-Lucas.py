import turtle
import random

t = turtle.Turtle()
turtle.speed(15)
t.speed(15)


t.penup()
t.goto(000,-200)
t.pendown()

turtle.bgcolor('Midnight Blue')

t.fillcolor('Saddle Brown')
t.begin_fill()

t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.fillcolor('brown')

t.fillcolor('green')
t.begin_fill()

t.pencolor('green')
t.goto(150,-200)
t.left(120)
t.forward(260)
t.left(120)
t.forward(260)
t.left(120)
t.forward(150)
t.fillcolor('green')
t.begin_fill()



t.pencolor('green')
t.penup()
t.goto(150,-50)
t.pendown()
t.left(120)
t.forward(260)
t.left(120)
t.forward(260)
t.left(120)
t.forward(260)
t.fillcolor('green')
t.begin_fill()

t.pencolor('white')
t.fillcolor('white')
t.penup()
t.goto(150,250)
t.pendown()
t.circle(50)
t.begin_fill()

t.fillcolor('Midnight Blue')
t.penup()
t.goto(140,250)
t.circle(50)
t.begin_fill()

t.fillcolor('Dark Orange')
t.goto(60,-20)
t.circle(20)
t.begin_fill()

t.fillcolor('Medium Blue')
t.goto(20,100)
t.circle(20)
t.begin_fill()
turtle.penup()
turtle.goto(-30,200)
turtle.pendown()
turtle.pencolor('white')

t.fillcolor('Orange Red')
t.goto(30,-100)
t.circle(19)
t.begin_fill()

t.fillcolor('Navy')
t.penup()
t.goto(-45,-150)
t.pendown
t.circle(14)
t.begin_fill()

t.fillcolor('Gold')
t.pencolor('Gold')
t.penup()
t.goto(000,20)
t.pendown()
t.circle(20)
t.begin_fill()

t.fillcolor('Dark Violet')
t.penup()
t.goto(70,-170)
t.pendown()
t.pencolor('Dark Violet')
t.circle(25)
t.begin_fill()

t.pencolor('Light Sea Green')
t.fillcolor('Light Sea Green')
t.penup()
t.goto(-50,-30)
t.circle(15)
t.begin_fill()

def draw_star(size,color):
    count = 0
    angle = 144
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(angle)
    turtle.end_fill()


t.pencolor('yellow')
draw_star(100,"yellow")

t.fillcolor('yellow')
t.penup()
t.goto(20,165)
t.pendown()
t.circle(20)
t.begin_fill()

t.pencolor('red')
t.penup()
t.goto(-200,270)
t.pendown()
t.write("Merry ",font=("Comic Sans MS", 30, "normal"))
t.pencolor('green')
t.penup()
t.goto(-110,270)
t.pendown()
t.write("Christmas! ",font=("Comic Sans MS", 30, "normal"))
t.ht()
turtle.ht()

#not sure if this is good. It's just for the stars.

"""for i in range(40,50):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.begin_fill()
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    turtle.pendown()
    draw_star(10, "yellow")
    turtle.penup()
    turtle.fd(50)

turtle.penup
turtle.goto(-300,200)
turtle.pendown()

for i in range(40,50):
    def draw_star(size, color):
        count = 0
        angle = 144
        turtle.fillcolor(color)
        turtle.begin_fill()
        for _ in range(5):
            turtle.forward(size)
            turtle.right(angle)
        turtle.end_fill()

    turtle.pendown()
    draw_star(10, "yellow")
    turtle.penup()
    turtle.fd(random.randint(30,50))
    turtle.right(random.randint(5,6))
"""
turtle.done()






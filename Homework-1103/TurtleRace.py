"""
Turtle 400 pixel race
"""

import turtle
import random

bob = turtle.Turtle()
bob.shape('turtle')
bob.color('purple')
bob.speed(3)
bob.penup()
bob.goto(-300, 200)
bob.pendown()

liam = turtle.Turtle()
liam.shape('turtle')
liam.color('red')
liam.speed(3)
liam.penup()
liam.goto(-300, -200)
liam.pendown()

jason = turtle.Turtle()
jason.shape('turtle')
jason.color('green')
jason.speed(3)
jason.penup()
jason.goto(-300, 0)
jason.pendown()

bob.write('Bob')
#bob.write(bob.pos())
jason.write('Jason')
#jason.write(jason.pos())
liam.write('Liam')
#liam.write(liam.pos())

ending = turtle.Turtle()
ending.penup()
ending.goto(100, 300)
ending.write('400 Pixel Finishing Line')
ending.right(90)
ending.pendown()
ending.forward(600)

# Steal the circle function we made in Homework-1027/ex-4.3.4.py file
def circle(t, r):
    c = 22 / 7 * r * 2
    for i in range(360):
        t.fd(c / 360)
        t.rt(1)

# initialize variable 'winner' to be a string
winner = 'secret'

# for loop to make turtle start and move forward concurrently - well sort of
for i in range(0, 250):
    jason.fd(random.randint(0, 5))
    liam.fd(random.randint(0, 5))
    bob.fd(random.randint(0, 5))

    # if winner is not declared yet, it will go into this if clause to check if anyone has moved 400 pixel yet
    if winner == 'secret':
        pos_jason = jason.pos()[0]
        pos_liam = liam.pos()[0]
        pos_bob = bob.pos()[0]

        if pos_jason >= 100:
            winner = jason

        if pos_liam >= 100:
            winner = liam

        if pos_bob >= 100:
            winner = bob

        if winner != 'secret':
            winner.write("I'm the first to reach 400 pixels")
            circle(winner, 10) #call the circle function to mark it

bob.write(bob.pos())
jason.write(jason.pos())
liam.write(liam.pos())

turtle.done()

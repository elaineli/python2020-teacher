import turtle
import random

bob = turtle.Turtle()
bob.shape('turtle')
bob.color('purple')
bob.speed(1)
bob.penup()
bob.goto(0, 200)
bob.pendown()

for i in range(0, 100):
    bob.fd(random.randint(0, 5))

elaine = turtle.Turtle()
elaine.shape('turtle')
elaine.color('red')
elaine.speed(1)
elaine.penup()
elaine.goto(0, -200)
elaine.pendown()

for i in range(0, 100):
    elaine.fd(random.randint(0, 5))

jason = turtle.Turtle()
jason.shape('turtle')
jason.color('green')
jason.speed(1)

for i in range(0, 100):
    jason.fd(random.randint(0, 5))

turtle.done()
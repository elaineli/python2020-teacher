"""
Write a function called circle that takes a turtle, t, and radius, r, as parameters and that draws an approximate circle
by calling polygon with an appropriate length and number of sides. Test your function with a range of values of r.
Hint: figure out the circumference of the circle and make sure that length * n = circumference.
"""

import turtle
import math

def circle(t, r):
    c = 22 / 7 * r * 2
    for i in range(360):
        t.fd(c / 360)
        t.rt(1)


bob = turtle.Turtle()

circle(bob, 150)
circle(bob, 100)


turtle.done()

"""
Make a more general version of circle called arc that takes an additional parameter angle,
which determines what fraction of a circle to draw. angle is in units of degrees, so when angle=360, arc should draw a complete circle.
"""

import turtle
import math

def arc(t, r, angle,):
    c = math.pi * r * 2
    for i in range(angle):
        t.fd(c / 360)
        t.rt(1)

bob = turtle.Turtle()

#arc(bob, 200, 90)
arc(bob, 100, 180)

turtle.done()

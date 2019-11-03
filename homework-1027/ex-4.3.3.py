"""
Make a copy of square and change the name to polygon.
Add another parameter named n and modify the body so it draws an n-sided regular polygon.
 Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.
"""

import turtle

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.rt(360 / n)

bob = turtle.Turtle()
polygon(bob, 100, 5)

turtle.done()

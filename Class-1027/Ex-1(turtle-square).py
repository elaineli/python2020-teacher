"""
Write a function called square that takes a parameter named t, which is a turtle. It should use the turtle to draw a square.
Write a function call that passes bob as an argument to square, and then run the program again.
Add another parameter, named length, to square.
Modify the body so length of the sides is length,
and then modify the function call to provide a second argument.
Run the program again. Test your program with a range of values for
length.
"""

import turtle


def square(t, length):
    for i in range(4):
        t.forward(length)
        t.right(90)


bob = turtle.Turtle()
square(bob, 200)

turtle.done()
import turtle

t = turtle.Turtle()
t.color('red')
t.fillcolor('green')

t.begin_fill()
for i in range(6):
    t.fd(100)
    t.right(60)
t.end_fill()

turtle.done()
import turtle

turtle.speed(0)
centerx = 0


turtle.penup()
turtle.goto(-170, 100)
turtle.pendown()
turtle.write("Happy Thanksgiving!", font=("Comic Sans MS", 50, "normal"))

colors = ["salmon", "darksalmon", "brown", "orange", "darkred", "burlywood", "goldenrod", "peru", "pink"]

def draw_feathers(x,y):
    pos = []

    turtle.goto(x + 170, y)
    sx = turtle.xcor()
    turtle.setheading(0)
    pos.append(turtle.position())
    for e in range (9):
        turtle.pencolor(colors[e])
        turtle.fillcolor(colors[e])

        turtle.begin_fill()
        turtle.circle(30, 200)
        turtle.end_fill()

        a = turtle.heading()
        turtle.setheading(a + 180)
        pos.append(turtle.position())

    x = turtle.xcor()
    cx = (sx + x) /2

    for i in range(9):
        turtle.pencolor(colors[i])
        turtle.fillcolor(colors[i])
        turtle.goto(cx, -200)
        turtle.begin_fill()
        turtle.goto(pos[i])
        turtle.goto(pos[i+1])
        turtle.goto(cx, -200)
        turtle.end_fill()
    return cx

def draw_body(x,y):
    turtle.goto(x,y)
    turtle.pencolor("saddlebrown")
    turtle.fillcolor("saddlebrown")
    turtle.setheading(0)

    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x,-110)
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()

    turtle.fillcolor("white")
    turtle.goto(x-7, -90)
    turtle.begin_fill()
    turtle.circle(6)
    turtle.end_fill()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()

    turtle.fillcolor("white")
    turtle.goto(x + 7, -90)
    turtle.begin_fill()
    turtle.circle(6)
    turtle.end_fill()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()

    turtle.goto(x + 5, -95)
    turtle.pencolor("red")
    turtle.fillcolor("red")

    turtle.begin_fill()
    turtle.setheading(180)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(10)
    turtle.end_fill()

    turtle.hideturtle()


def draw_feet(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pencolor("black")
    turtle.pendown()
    turtle.showturtle()

    turtle.setheading(270)
    turtle.forward(20)

    turtle.right(30)
    turtle.forward(5)
    turtle.backward(5)

    turtle.setheading(270)
    turtle.forward(5)
    turtle.backward(5)

    turtle.left(30)
    turtle.forward(5)
    turtle.backward(5)



def turkey (x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    cx = draw_feathers(x,y)
    draw_body(x,y)
    draw_feet(x-7, -200)
    draw_feet(x + 7, -200)

turkey(0, -200)
turkey(-380, -200)
turkey(380, -200)



turtle.mainloop()

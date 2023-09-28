import turtle
a = turtle.Turtle()
a.getscreen().bgcolor("black")

a.speed(1000)
a.penup()
a.goto(-300,-100)
a.pendown()
a.color("green")


def star(turtle,size):
    if size<=10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle,size/3)
            turtle.left(216)
            turtle.end_fill()
star(a,200)
turtle.done()
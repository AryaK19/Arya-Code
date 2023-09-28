import turtle
import math

bob = turtle.Turtle()



bob.speed(15)
bob.color("green","cyan")

i = 1


while True:
    bob.forward(10)
    bob.left(math.sin(i/10)*25)
    bob.left(20)
    pos = bob.pos()
    i = i + 1

    if int(pos[0])==0 and int(pos[1])==0:
        break




turtle.done()


turtle.done()
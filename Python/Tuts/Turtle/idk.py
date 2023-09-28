import turtle
import random as rn
import math

bob = turtle.Turtle()
bob.hideturtle()
bob.getscreen().bgcolor("black")

bob.speed(50)
color = [0.225,0.225,0.225]
bob.color(color)

bob.penup()
bob.goto(-250,0)
bob.pendown()


for i in range(500):

    bob.forward(math.sin(i)*30)
    # bob.left(137)
    bob.left(math.sqrt(i)-math.sin(i))

    nor = rn.random()
    nog = rn.random()
    nob= rn.random()

    color[0] = color[0] + i%nor
    color[1] = color[1] + i%nog
    color[2] = color[2] + i%nob

    if color[0]>1 or color[1]>1 or color[2]>1:
        color[0] = 0.50
        color[1] = 0.100
        color[2] = 0.30
        
    bob.color(color)    

    pos = bob.pos()
    
    
    



turtle.done()

import turtle

bob = turtle.Turtle()

screen = bob.getscreen()
screen.bgcolor("black")
bob.color("white")
bob.speed(10)
i = 0
size = 400


while True:
    bob.forward(size)
    bob.left(216)
    i = i + 1
    if i%5==0:
        size = size/3
        continue
    pos = bob.pos()
    # if int(pos[0])==0 and int(pos[1])==0:
    #     break






turtle.done()
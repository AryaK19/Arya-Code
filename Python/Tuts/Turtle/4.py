import turtle

bob = turtle.Turtle()
bob.speed(20)
bob.color("red","orange")

bob.begin_fill()
while True:
    bob.forward(250)
    bob.left(170)
    pos = bob.pos()
    print(pos)
    if int(pos[0])==0 and int(pos[1])==0:
        break
bob.end_fill()


turtle.done()
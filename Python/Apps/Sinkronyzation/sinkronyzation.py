import pygame
import pymunk
import pymunk.pygame_util
from pymunk import Vec2d

pygame.init()

width , height = 1000 , 700
window = pygame.display.set_mode([width,height])

def Draw(window,space,draw_options):
    window.fill("black")
    space.debug_draw(draw_options)

def Create_Boundaries(space,width,height):
    rects = [
        [(width/2 , height - 10),(width+1000 , 350)]  
    ]
    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body,size)
        shape.friction = 1
        space.add(body,shape) 

def CreateBall(space,pos):
    white = [225,225,225,100]
    body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body,15)
    shape.mass = 1000
    shape.color = white
    shape.friction = 1
    space.add(body,shape)
    return shape

def Create_structures(space,pos):
    BROWN = (139,69,19,100)
    rects = [
        [pos,(1500,10),BROWN,600]
    ]

    for pos ,size ,color,mass in rects:
        body = pymunk.Body()
        body.position = pos
        shape = pymunk.Poly.create_box(body,size)
        shape.color = color
        shape.mass = 1000
        shape.friction = 1
        space.add(body,shape)


def pendulum(space,pos):
    body = pymunk.Body(body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    l1 = pymunk.Segment(body, (-190, 0), (-110, 0), 5) 
    l2 = pymunk.Segment(body, (-150, 0), (-150, -170), 5)
    l3 = pymunk.Segment(body, (-150, -170), (-350, -170), 5)
    l4 = pymunk.Segment(body, (-350, -170), (-350, 0), 5) 
    l5 = pymunk.Segment(body, (-390, 0), (-310, 0), 5)
    l1.friction = 1 
    l1.mass = 100
    l2.friction = 1
    l2.mass = 100
    l3.friction = 1
    l3.mass = 300
    l4.friction = 1
    l4.mass = 100
    l5.friction = 1
    l5.mass = 100

    pen = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
    pen.position = (pos[0] - 250,pos[1] - 65)
    circle = pymunk.Circle(pen,15,(0,0))
    
    circle.friction = 1
    circle.mass = 200

    joint = pymunk.PinJoint(body,pen,(-250,-170),(0,0))

    space.add(body, l1, l2, l3, l4, l5,pen,circle,joint) 
    return l1,l2

def run (window,width,height):
    run = True
    selected = None
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps

    space = pymunk.Space()

    space.gravity = (0,1000)

    
    Create_Boundaries(space,width,height)
    CreateBall(space,[200,500])
    CreateBall(space,[800,500])
    Create_structures(space,(500 , 475))
    pendulum(space,(450,465))
    pendulum(space,(750,465))
    pendulum(space,(1050,465))
    
    pendulum(space,(450,280))
    pendulum(space,(750,280))
    pendulum(space,(1050,280))

    mouse_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    

    draw_options = pymunk.pygame_util.DrawOptions(window) 

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            elif event.type == pygame.MOUSEBUTTONDOWN :
                if selected != None:
                    space.remove(selected)
                p = (Vec2d(*event.pos))
                hit = space.point_query_nearest(p, 0, pymunk.ShapeFilter())
                if hit != None:
                    shape = hit.shape
                    rest_length = mouse_body.position.get_distance(shape.body.position)
                    ds = pymunk.DampedSpring(
                        mouse_body, shape.body, (0, 0), (0, 0), rest_length, 1000, 10
                    )
                     
                    selected = ds
                    space.add(ds)
                    

            elif event.type == pygame.MOUSEBUTTONUP:
                if selected != None:
                    space.remove(selected)
                    selected = None

        mpos = pygame.mouse.get_pos()
        p = (Vec2d(*mpos))
        mouse_body.position = p
        
        Draw(window,space,draw_options)
        space.step(dt)
        clock.tick(fps)
        pygame.display.update()

    pygame.quit()



run(window,width,height)
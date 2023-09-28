import pygame
import pymunk
import pymunk.pygame_util
import math

pygame.init()

width , height = 1000 , 700
window = pygame.display.set_mode([width,height])

def cal_distance(p1,p2):
    return math.sqrt((p1[1] - p2[1])**2 + (p2[0] - p1[0])**2) 

def cal_angle(p1,p2):
    return math.atan2( (p2[1] - p1[1]) , (p2[0] - p1[0]))


def Draw(window,space,draw_options,line):
    window.fill("grey")
    space.debug_draw(draw_options)
    if line:
        pygame.draw.line(window,"black",line[0],line[1],3)
    pygame.display.update()
    

def Create_Boundaries(space,width,height):
    rects = [
        [(width/2 , height - 10),(width , 20)],
        [(width/2 , 10),(width , 20)],
        [(10 , height/2),(20 , height)],
        [(width-10 , height/2),(20 , height)],
    ]
    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body,size)
        shape.elasticity = 0.9
        shape.friction = 0.3
        space.add(body,shape) 

def CreateBall(space,radius,mass,pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body,radius)
    shape.mass = mass
    shape.colour = (222,0,0)
    shape.elasticity = 0.8
    shape.friction = 0.3
    space.add(body,shape)
    return shape

def Create_structures(space,width,height):
    BROWN = (139,69,19,100)
    rects = [
        [(590 , height - 110),(30,180),BROWN,100],
        [(850 , height - 110),(30,180),BROWN,100],
        [(720 , height - 220),(290,30),BROWN,150]
    ]

    for pos ,size ,color,mass in rects:
        body = pymunk.Body()
        body.position = pos
        shape = pymunk.Poly.create_box(body,size,radius = 2)
        shape.color = color
        shape.mass = mass
        shape.elasticity = 0.4
        shape.friction = 0.6
        space.add(body,shape)

def Create_pendulum(space):
    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = (300,270)

    body = pymunk.Body()
    body.position = (300,400)

    # line = pymunk.Segment(body,(0,0),(255,0),5)
    circle = pymunk.Circle(body,30,(0,0))
    circle.elasticity = 0.4
    # line.friction = 0.3
    circle.friction = 0
    # line.mass = 8
    circle.mass = 30 
    rotation_center_joint = pymunk.PinJoint(body,rotation_center_body,(0,0),(0,0))
    space.add(circle,body,rotation_center_joint)


def run (window,width,height):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps

    space = pymunk.Space()

    space.gravity = (0,1000)

    
    
    Create_Boundaries(space,width,height)
    Create_structures(space,width,height)
    Create_pendulum(space)

    draw_options = pymunk.pygame_util.DrawOptions(window) 

    pressed_pos = None 
    ball = None

    while run:

        line = None
        if ball  and pressed_pos :
            line = [pressed_pos , pygame.mouse.get_pos()]


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not ball :
                    pressed_pos = pygame.mouse.get_pos()
                    ball = CreateBall(space,30,30,pressed_pos)

                elif pressed_pos:
                    ball.body.body_type = pymunk.Body.DYNAMIC

                    angle = cal_angle(line[0],line[1])
                    force = cal_distance(line[0],line[1]) * 200
                    fx = - (math.cos(angle)) * force
                    fy = - (math.sin(angle)) * force

                    ball.body.apply_impulse_at_local_point((fx , fy),(0 , 0)) #look documentation :)
                   
                    pressed_pos = None

                else:
                    space.remove(ball,ball.body)
                    ball = None

        Draw(window,space,draw_options,line)
        space.step(dt)
        clock.tick(fps)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    run(window,width,height)        
        

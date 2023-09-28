import pygame
import pymunk
import pymunk.pygame_util
import math
import random

pygame.init()

width , height = 1000 , 700
window = pygame.display.set_mode([width,height])

def Text_screen(text,colour,x,y,size):
    font = pygame.font.SysFont(None,size)
    screen_text = font.render(text,True,colour)
    window.blit(screen_text,[x,y])

def ColPic():
    r = random.randint(70,230)
    g = random.randint(70,230)
    b = random.randint(70,230)
    return (r,g,b,100)

def Radius(event,radius):
    if event.type == pygame.MOUSEWHEEL:
            if event.y == -1:
                radius += 2 
            elif event.y == 1:
                radius -= 2 
    return radius

def Mass(event,mass):
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PERIOD:
                mass += 2 
            elif event.key == pygame.K_COMMA:
                mass -= 2 
    return mass

def Fps(event,fps):
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                fps += 2 
            elif event.key == pygame.K_LEFT:
                fps -= 2 
    return fps

def cal_distance(p1,p2):
    return math.sqrt((p1[1] - p2[1])**2 + (p2[0] - p1[0])**2) 

def cal_angle(p1,p2):
    return math.atan2( (p2[1] - p1[1]) , (p2[0] - p1[0]))


def Draw(window,space,draw_options,line,ball_len,radius,fps,force,mass,gravity):
    grey = (20,20,20,100)
    window.fill(grey)
    space.debug_draw(draw_options)
    if line:
        pygame.draw.line(window,"white",line[0],line[1],3)
    Text_screen(f"Balls - {len(ball_len)} | Radius - {radius} | FPS-{fps} | Speed - {int(force/100)} | Mass - {mass} | Gravity - {gravity}","black",20,7,37)
    pygame.display.update()
    

def Create_Boundaries(space,width,height):
    rects = [
        [(width/2 , height + 10),(width , 20)],
        [(width/2 , 40/2),(width , 40)],
        [(-11 , height/2),(20 , height)],
        [(width+10 , height/2),(20 , height)],
    ]
    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body,size)
        shape.elasticity = 1
        shape.friction = 0.3
        space.add(body,shape) 

def CreateBall(space,radius,mass,pos,color):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body,radius)
    shape.mass = mass
    shape.color = color
    shape.elasticity = 0.98
    shape.friction = 0.3
    space.add(body,shape)
    return shape


def App (window,width,height):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps
    radius = 30
    force = 0
    mass = 30
    ball_len = []
    gravity = "OFF"
    
    space = pymunk.Space()

    
    space.gravity = (0,0)
    Create_Boundaries(space,width,height)
    

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

            radius = Radius(event,radius)
            mass = Mass(event,mass)
            fps = Fps(event,fps)

            

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not ball :
                    color = ColPic()
                    pressed_pos = pygame.mouse.get_pos()
                    ball = CreateBall(space,radius,mass,pressed_pos,color)
                    ball_len.append(ball)
                                                                                                        

                elif pressed_pos:
                    ball.body.body_type = pymunk.Body.DYNAMIC

                    angle = cal_angle(line[0],line[1])
                    force = cal_distance(line[0],line[1]) * 200
                    fx = - (math.cos(angle)) * force
                    fy = - (math.sin(angle)) * force
                    

                    ball.body.apply_impulse_at_local_point((fx , fy),(0 , 0)) #look documentation :)
                   
                    pressed_pos = None
                    ball = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:

                    App(window,width,height)

                if event.key == pygame.K_RETURN and space.gravity == (0,1300) :
                    gravity = "OFF"
                    space.gravity = (0,0)
                elif event.key == pygame.K_RETURN and space.gravity == (0,0) :
                    gravity = "ON"
                    space.gravity = (0,1300)

                if event.key == pygame.K_SPACE and dt != 0:
                    dt = 0
                elif event.key == pygame.K_SPACE and dt == 0:
                    dt = 1 / fps

        Draw(window,space,draw_options,line,ball_len,radius,fps,force,mass,gravity)
        

        space.step(dt)
        clock.tick(fps)
        pygame.display.update()

    pygame.quit()


App(window,width,height)



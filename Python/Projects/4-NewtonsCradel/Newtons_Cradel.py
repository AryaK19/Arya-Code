
import pygame
import pymunk
import pymunk.pygame_util

from pymunk import Vec2d

pygame.init()

width , height = 1000 , 700
window = pygame.display.set_mode([width,height])

def to_pygame(p):
    """Small hack to convert pymunk to pygame coordinates"""
    return int(p.x), int(-p.y + height)

def from_pygame(p):
    return to_pygame(p)

def Draw(window,space,draw_options):
    window.fill("black")
    space.debug_draw(draw_options)
    
    pygame.display.update()
     



def Create_pendulum(space,posix,posiy):
    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = (posix,posiy)

    body = pymunk.Body()
    body.position = (posix,posiy+400)

    shape = pymunk.Circle(body,30,(0,0))
    shape.elasticity = 1
    shape.mass = 100
     
    shape.color = (194,194,194,100)
    rotation_center_joint = pymunk.PinJoint(body,rotation_center_body,(0,0),(0,0))

    space.add(shape,body,rotation_center_joint)
    

def run (window,width,height):
    exit_ = False
    selected = None
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps
    t = 0

    space = pymunk.Space()

    mouse_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    space.gravity = (0,2000)

    
    pendulems = 1
    
    for i in range(0,(pendulems*2),2):
        Create_pendulum(space, 500 - (30*pendulems - 30) + (i*30) , 50) 

    

    draw_options = pymunk.pygame_util.DrawOptions(window) 


    while not exit_:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_ = True
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
                    
                    # ds = pymunk.PinJoint(mouse_body, shape.body, (0, 0), (0, 0)) 
                    selected = ds
                    space.add(ds)
                    

            elif event.type == pygame.MOUSEBUTTONUP:
                if selected != None:
                    space.remove(selected)
                    selected = None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:

                    run(window,width,height)
                if event.key == pygame.K_LALT:

                    space.gravity = (0,0)
                if event.key == pygame.K_RALT:

                    space.gravity = (0,2000)

                elif event.key == pygame.K_SPACE and dt != 0:
                    dt = 0
                elif event.key == pygame.K_SPACE and dt == 0:
                    dt = 1 / fps

        mpos = pygame.mouse.get_pos()
        p = (Vec2d(*mpos))
        mouse_body.position = p

        Draw(window,space,draw_options)
        
        space.step(dt)
        clock.tick(fps)
        pygame.display.update()

    pygame.quit()

run(window,width,height)
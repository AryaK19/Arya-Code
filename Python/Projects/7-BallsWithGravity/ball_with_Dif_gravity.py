import pygame
import pymunk
import pymunk.pygame_util

pygame.init()

width,height = 1000,700

window = pygame.display.set_mode([width,height])

def floor(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (width/2,height+400)
    wall = pymunk.Poly.create_box(body,(width+100,800))
    wall.elasticity = 1
    space.add(body,wall)

def balls(space,pos,radius,mass,elastisity):
    white = (255,255,255,100)
    body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    ball = pymunk.Circle(body,radius)
    ball.color = white
    ball.mass = mass
    ball.elasticity = elastisity
    
    space.add(body,ball)
    return ball

def Draw(window,space,draw_options):
    grey = (0,0,10,10)
    window.fill(grey)
    space.debug_draw(draw_options)
    pygame.display.update()

def main(window):
    run = True
    clock = pygame.time.Clock()
    gravity = 1000
    k = 0

    radius = 1
    slop = 2
    elasticity = 0.89
    fps = 120
    
    dt = 1/fps

    space = pymunk.Space()
    space.gravity = (0,0)

    floor(space)

    for i in range(radius,(radius*width)+1,radius*2): 
        k = k + slop
        balls(space,(i,(k)-400),radius,i,elasticity)
        
    
    draw_options = pymunk.pygame_util.DrawOptions(window)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    main(window)
                if event.key == pygame.K_RETURN and space.gravity == (0,0):
                    space.gravity = (0,gravity)
                        
                elif event.key == pygame.K_RETURN and space.gravity == (0,gravity):
                    space.gravity = (0,0)
                if event.key == pygame.K_SPACE and dt == 1/fps:
                    dt = 0
                elif event.key == pygame.K_SPACE and dt == 0:
                    dt = 1/fps

        Draw(window,space,draw_options)
        
        space.step(dt)
        clock.tick(fps)
        pygame.display.update()

    

main(window)
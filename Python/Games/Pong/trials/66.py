from json.encoder import py_encode_basestring_ascii
import pygame 
import pymunk
import pymunk.pygame_util
import math
import random
pygame.init()


# Colours
white = (255,255,255,100)
red = (255,0,0,100)
black = (0,0,0,100)
green = (0,255,0,100)
grey = (100,100,100,100)
brown = (139,69,19,100)

screen_width = 1000
screen_height = 550


# creating Window
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong")

def CreateBall(space,radius,mass,color):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (screen_width/2,screen_height/2)
    shape = pymunk.Circle(body,radius)
    shape.mass = mass
    shape.color = color
    shape.elasticity = 1
    space.add(body,shape)
    return shape

def Text_Screen(text,colour,x,y,size):
    font = pygame.font.SysFont(None,size)
    screen_text = font.render(text,True,colour)
    gameWindow.blit(screen_text,[x,y])

def Create_Bar_L(space,screen_width,screen_height):
    rects = [
        [(55 , screen_height/2),(20,130),white,100],
    ]

    for pos ,size ,color,mass in rects:
        body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body,size,radius = 1.3)
        shape.color = color
        shape.mass = mass
        shape.elasticity = 1
        space.add(body,shape)
        return shape

def Create_Bar_R(space,screen_width,screen_height):
    rects = [
        [(screen_width - 55  , screen_height/2),(20,130),white,100],
    ]

    for pos ,size ,color,mass in rects:
        body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body,size,radius = 1.3)
        shape.color = color
        shape.mass = mass
        shape.elasticity = 1
        space.add(body,shape)
        return shape

def Create_Boundaries(space,screen_width,screen_height):
    rects = [
        [(screen_width/2 , screen_height + 10),(screen_width , 20)],
        [(screen_width/2 , 20/2),(screen_width , 40)],
        # [(-11 , screen_height/2),(20 , screen_height)],
        # [(screen_width+10 , screen_height/2),(20 , screen_height)],
    ]
    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body,size)
        shape.color = grey
        shape.elasticity = 1
        space.add(body,shape) 



def  Ran_Speed():
    ball_speed = 40
    vx = random.randint(5,35)
    vy = int(math.sqrt( ball_speed**2 - vx**2 ))
    vx = vx*170
    vy = vy*170

    a = random.randint(1,4)
    
    if a==1 :
        vx =  -vx 
    elif a==2 :
        vy =  -vy
    elif a==3 :
        vx =  -vx 
        vy =  -vy   

    return vx,vy
    

def Draw(gameWindow,space,draw_options,score1,score2):
    gameWindow.fill(black)
    space.debug_draw(draw_options)
    pygame.draw.rect(gameWindow,white,[screen_width/2,0,1,screen_height])
    Text_Screen(f"{score1} : Player 1",white,(screen_width/2)-140,5,30)
    Text_Screen(f"Player 2 : {score2}",white,(screen_width/2)+30,5,30)
    pygame.display.update()

# Creating a gameloop
def gameloop():

    # Game Specific variables
    exit_game = False
    game_over = False
    fps = 60
    dt = 1 / fps
    space = pymunk.Space()

    draw_options = pymunk.pygame_util.DrawOptions(gameWindow)
    
    ball = CreateBall(space,12,20,red)

    Create_Boundaries(space,screen_width,screen_height)
    bar_L = Create_Bar_L(space,screen_width,screen_height)
    bar_R = Create_Bar_R(space,screen_width,screen_height)

    player1_press_U = False
    player1_press_D = False
    player2_press_W = False
    player2_press_S = False

    vx,vy = 0,0

    #other
    with open("player1s.txt") as f :
            p1 = f.read()
            s1 = p1.split()
    with open("player2s.txt") as f :
            p2 = f.read()
            s2 = p2.split()
    score1=int(s1[0])
    score2=int(s2[0])

    clock = pygame.time.Clock()

    while not exit_game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True 
                break
            if vx == 0 and vy == 0:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    ball.body.body_type = pymunk.Body.DYNAMIC
                    vx,vy = Ran_Speed()
                    ball.body.apply_impulse_at_local_point((vx , vy),(0 , 0))
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player1_press_U = True
                    elif event.key == pygame.K_DOWN:
                        player1_press_D = True

                    if event.key == pygame.K_w:
                        player2_press_W = True
                    elif event.key == pygame.K_s:
                        player2_press_S = True
                
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        player1_press_U = False
                    elif event.key == pygame.K_DOWN:
                        player1_press_D = False

                    if event.key == pygame.K_w:
                        player2_press_W = False
                    elif event.key == pygame.K_s:
                        player2_press_S = False



        if player1_press_U:
            bar_R.body.velocity = (0,-90)


        with open("player1s.txt") as f :
            p1 = f.read()
            s1 = p1.split()
        with open("player2s.txt") as f :
            p2 = f.read()
            s2 = p2.split()

        with open("player1s.txt","w") as f :
            f.write(p1)
        with open("player2s.txt","w") as f :
            f.write(p2)
        
            
        
        Draw(gameWindow,space,draw_options,score1,score2)
    
        space.step(dt)
        clock.tick(fps)

    pygame.quit()

gameloop()
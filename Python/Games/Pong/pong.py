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

screen_width = 1300
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
        [(55 , screen_height/2),(20,130),white],
    ]

    for pos ,size ,color in rects:
        body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body,size,radius = 1.3)
        shape.color = color
        shape.mass = 0.3
        shape.elasticity = 1
        space.add(body,shape)
        return shape

def Create_Bar_R(space,screen_width,screen_height):
    rects = [
        [(screen_width - 55  , screen_height/2),(20,130),white],
    ]

    for pos ,size ,color in rects:
        body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body,size,radius = 1.3)
        shape.color = color
        shape.mass = 0.3
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
    vx = vx*1700
    vy = vy*1700

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
def gameloop(gameWindow):

    # Game Specific variables
    exit_game = False
    game_over = False
    game_restart = False
    fps = 120
    dt = 1 / fps

    #rotate
    rotate = 40
    rotate_U = False 
    rotate_W = False 
    space = pymunk.Space()

    draw_options = pymunk.pygame_util.DrawOptions(gameWindow)
    
    ball = CreateBall(space,12,100,red)


    Create_Boundaries(space,screen_width,screen_height)

    bar_L = Create_Bar_L(space,screen_width,screen_height)
    bar_R = Create_Bar_R(space,screen_width,screen_height)

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
                if event.key == pygame.K_UP :
                    bar_R.body.velocity = (0,-900)     
                if event.key == pygame.K_DOWN :
                    bar_R.body.velocity = (0,900)
                if event.key == pygame.K_RIGHT :
                    rotate_U = True
                if event .key == pygame.K_LEFT:
                    bar_R.body.velocity = (-300,0)
        
                    
 


                if event.key == pygame.K_w:
                    bar_L.body.velocity = (0,-900)
                if event.key == pygame.K_s:
                    bar_L.body.velocity = (0,900)
                if event.key == pygame.K_a :
                    rotate_W = True 
                if event .key == pygame.K_d: 
                    bar_L.body.velocity = (300,0)
              
                

                if event.key == pygame.K_BACKSPACE:
                    gameloop(gameWindow)
                if event.key == pygame.K_ESCAPE:
                    p1 = p1.replace(s1[0],'0')
                    p2 = p2.replace(s2[0],'0')
                    with open("player1s.txt","w") as f :
                        f.write(p1)
                    with open("player2s.txt","w") as f :
                        f.write(p2)
                    gameloop(gameWindow)
                
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    bar_R.body.velocity = (0,0)
                if event.key == pygame.K_RIGHT :
                    rotate_U = False
                    bar_R.body.angle = 0
                if event.key == pygame.K_LEFT :
                    bar_R.body.velocity = (0,0)
                    bar_R.body.position = (screen_width - 55,bar_R.body.position[1])
      
                
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    bar_L.body.velocity = (0,0)
                if event.key == pygame.K_a :
                    bar_L.body.angle = 0
                    rotate_W = False
    


        ball_pos = ball.body._get_position()

        if abs(ball_pos[0] <= 0):
            score2+=1
            p1.replace(p1[0],s1[0])
            game_restart = True
        elif abs(ball_pos[0] >= screen_width):
            score1+=1
            p2.replace(p2[0],s2[0])
            game_restart = True

        if score1 > int(s1[0]):
            p1 = p1.replace(s1[0],str(score1))
        elif score2 > int(s2[0]):
            p2 = p2.replace(s2[0],str(score2))

        with open("player1s.txt","w") as f :
            f.write(p1)
        with open("player2s.txt","w") as f :
            f.write(p2)
        
        if rotate_U:
            bar_R.body.angle+=rotate
        if rotate_W:
            bar_L.body.angle-=rotate

        if abs(bar_L.body.position[0] >= 80):
            bar_L.body.velocity =(0,0)
            bar_L.body.position = (55,bar_L.body.position[1])
        if abs(bar_R.body.position[0] <= screen_width - 80 ):
            bar_R.body.velocity = (0,0)
            bar_R.body.position = (screen_width - 55,bar_R.body.position[1])

        if game_restart:
            gameloop(gameWindow)  
        
        Draw(gameWindow,space,draw_options,score1,score2)
    
        space.step(dt)
        clock.tick(fps)

    pygame.quit()

gameloop(gameWindow)
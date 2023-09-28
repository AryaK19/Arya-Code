import pygame 
import random
pygame.init()


# Colours
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
greyesh = (70,70,70)

screen_width = 500 
screen_height = 600
bar_thic = 40
clock = pygame.time.Clock()


# creating Window
appWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Bounce")



def text_screen(text,colour,x,y,font):
    Font = pygame.font.SysFont(None,font)
    screen_text = Font.render(text,True,colour)
    appWindow.blit(screen_text,[x,y])



def Cc(colour,ball_x,ball_y,ball_r):
    pygame.draw.circle(appWindow,colour,[ball_x,ball_y],ball_r)

def ColPic():
    r = random.randint(40,222)
    g = random.randint(40,222)
    b = random.randint(40,200)
    return (r,g,b)

def Collision(positions,velocities,ball_ra,i,j):

    if abs((positions[i][0]-positions[j][0])**2 + (positions[i][1]-positions[j][1])**2- (ball_ra[i]+ball_ra[j])**2 <= 90):
        

        if ((velocities[i][0] < 0 and velocities[i][1] > 0) and (velocities[j][0] < 0 and velocities[j][1] < 0)) or ((velocities[i][0] > 0 and velocities[i][1] > 0) and (velocities[j][0] > 0 and velocities[j][1] < 0)):       
            velocities[i][1] = - velocities[i][1]
            velocities[j][1] = - velocities[j][1]
        
        elif ((velocities[i][0] > 0 and velocities[i][1] > 0) and (velocities[j][0] < 0 and velocities[j][1] > 0)) or ((velocities[i][0] > 0 and velocities[i][1] < 0) and (velocities[j][0] < 0 and velocities[j][1] < 0)) :
            velocities[i][0] = - velocities[i][0]
            velocities[j][0] = - velocities[j][0]

        elif ((velocities[i][0] < 0 and velocities[i][1] > 0) and (velocities[j][0] > 0 and velocities[j][1] < 0)) or ((velocities[i][0] > 0 and velocities[i][1] > 0) and (velocities[j][0] < 0 and velocities[j][1] < 0)):
            velocities[i][0] = - velocities[i][0]
            velocities[i][1] = - velocities[i][1]
            velocities[j][0] = - velocities[j][0]
            velocities[j][1] = - velocities[j][1]
            
        
        elif ((velocities[i][0] > 0 and velocities[i][1] > 0) and (velocities[j][0] > 0 and velocities[j][1] > 0)) or  ((velocities[i][0] < 0 and velocities[i][1] < 0) and (velocities[j][0] < 0 and velocities[j][1] < 0)):
            a = velocities[i][0]
            b = velocities[i][1]

            velocities[i][0] = velocities[j][0]
            velocities[i][1] = velocities[j][1]

            velocities[j][0] = a
            velocities[j][1] = b

        elif ((velocities[i][0] < 0 and velocities[i][1] > 0) and (velocities[j][0] < 0 and velocities[j][1] > 0)) or ((velocities[i][0] > 0 and velocities[i][1] < 0) and (velocities[j][0] > 0 and velocities[j][1] < 0)):
            a = velocities[i][0]
            b = velocities[i][1]

            velocities[i][0] = velocities[j][0]
            velocities[i][1] = velocities[j][1]

            velocities[j][0] = a
            velocities[j][1] = b

        elif ((velocities[j][0] < 0 and velocities[j][1] > 0) and (velocities[i][0] < 0 and velocities[i][1] < 0)) or ((velocities[j][0] > 0 and velocities[j][1] > 0) and (velocities[i][0] > 0 and velocities[i][1] < 0)):
            velocities[j][1] = - velocities[j][1]
            velocities[i][1] = - velocities[i][1]
        
        elif ((velocities[j][0] > 0 and velocities[j][1] > 0) and (velocities[i][0] < 0 and velocities[i][1] > 0)) or ((velocities[j][0] > 0 and velocities[j][1] < 0) and (velocities[i][0] < 0 and velocities[i][1] < 0)) :
            velocities[j][0] = - velocities[j][0]
            velocities[i][0] = - velocities[i][0]

        elif ((velocities[j][0] < 0 and velocities[j][1] > 0) and (velocities[i][0] > 0 and velocities[i][1] < 0)) or ((velocities[j][0] > 0 and velocities[j][1] > 0) and (velocities[i][0] < 0 and velocities[i][1] < 0)):
            velocities[j][0] = - velocities[j][0]
            velocities[j][1] = - velocities[j][1]
            velocities[i][0] = - velocities[i][0]
            velocities[i][1] = - velocities[i][1]
            
        
        elif ((velocities[j][0] > 0 and velocities[j][1] > 0) and (velocities[i][0] > 0 and velocities[i][1] > 0)) or  ((velocities[j][0] < 0 and velocities[j][1] < 0) and (velocities[i][0] < 0 and velocities[i][1] < 0)):
            a = velocities[j][0]
            b = velocities[j][1]

            velocities[j][0] = velocities[i][0]
            velocities[j][1] = velocities[i][1]

            velocities[i][0] = a
            velocities[i][1] = b

        elif ((velocities[j][0] < 0 and velocities[j][1] > 0) and (velocities[i][0] < 0 and velocities[i][1] > 0)) or ((velocities[j][0] > 0 and velocities[j][1] < 0) and (velocities[i][0] > 0 and velocities[i][1] < 0)):
            a = velocities[j][0]
            b = velocities[j][1]

            velocities[j][0] = velocities[i][0]
            velocities[j][1] = velocities[i][1]

            velocities[i][0] = a
            velocities[i][1] = b
     

def AppLoop():
    appWindow.fill(greyesh)
    exit_app = False 
    make_ball = False
    start = False
    velo = True
    change = False
    positions=[]
    velocities=[]
    pause_vel=[]
    ball_ra=[]
    ball_col=[]

    #ball 
    balls = 0
    ball_r = 25
    ball_speed = 5
    ball_vec = 120

    ball_velocity_x = random.randint(1 ,100)
    ball_velocity_y = int(( ball_vec**2 - ball_velocity_x**2 )**0.5)

    # constants
    a = random.randint(1,4)
    div_ratio = ball_vec/ball_speed
    if a==1 :
        ball_velocity_x =  -ball_velocity_x/div_ratio 
        ball_velocity_y =  ball_velocity_y/div_ratio
    elif a==2 :
        ball_velocity_x =  ball_velocity_x/div_ratio 
        ball_velocity_y =  -ball_velocity_y/div_ratio
    elif a==3 :
        ball_velocity_x =  -ball_velocity_x/div_ratio 
        ball_velocity_y =  -ball_velocity_y/div_ratio   
    else :
        ball_velocity_x =  ball_velocity_x/div_ratio 
        ball_velocity_y =  ball_velocity_y/div_ratio

    fps = 50


    while not exit_app: 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_app = True
            
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    AppLoop()

                if event.key == pygame.K_RIGHT:
                    fps+=5
                if event.key == pygame.K_LEFT:
                    fps-=5
                if event.key == pygame.K_UP:
                    ball_speed+=0.7
                if event.key == pygame.K_DOWN:
                    ball_speed-=0.7
                if event.key == pygame.K_RETURN:
                    start = True

            
                if event.key == pygame.K_COMMA:
                    ball_r-=3
                if event.key == pygame.K_PERIOD:
                    ball_r+=3

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                balls += 1
                rand_col = ColPic()
                if not make_ball:
                    positio = list(pygame.mouse.get_pos())
                    positions.append(positio)
                make_ball = True
                if balls >= 2: 
                    position = list(pygame.mouse.get_pos())
                    positions.append(position)

                ball_velocity_x = random.randint(1 ,100)
                ball_velocity_y = int(( ball_vec**2 - ball_velocity_x**2 )**0.5)

                # constants
                a = random.randint(1,4)
                div_ratio = ball_vec/ball_speed
                if a==1 :
                    ball_velocity_x =  -ball_velocity_x/div_ratio 
                    ball_velocity_y =  ball_velocity_y/div_ratio
                elif a==2 :
                    ball_velocity_x =  ball_velocity_x/div_ratio 
                    ball_velocity_y =  -ball_velocity_y/div_ratio
                elif a==3 :
                    ball_velocity_x =  -ball_velocity_x/div_ratio 
                    ball_velocity_y =  -ball_velocity_y/div_ratio   
                else :
                    ball_velocity_x =  ball_velocity_x/div_ratio 
                    ball_velocity_y =  ball_velocity_y/div_ratio
                if  velo or velocities[0][0]!=0:
                    velocities.append([ball_velocity_x,ball_velocity_y])
                    velo = False
                elif velocities[0][0]==0:
                    velocities.append([0,0])
                    pause_vel.append([ball_velocity_x,ball_velocity_y])

                ball_ra.append(ball_r)
                ball_col.append(rand_col)
            
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE  and (velocities[i][0] != 0 and velocities[i][1] != 0):
                    for i in range(0,balls):
                        pause_vel.insert(i,[velocities[i][0],velocities[i][1]])
                        velocities[i][0] = 0
                        velocities[i][1] = 0
                       
                if (event.key == pygame.K_LALT or event.key == pygame.K_RALT) and (velocities[i][0] == 0 and velocities[i][1] == 0) :
                    for i in range(0,balls):
                        velocities[i][0] = pause_vel[i][0]
                        velocities[i][1] = pause_vel[i][1]
                    j=0
                    while j<balls:
                        del pause_vel[0]
                        j+=1   
        
        if balls > 1:
            for i in range(0,balls-1):
                for j in range(1,balls):
                    if i != j :
                        Collision(positions,velocities,ball_ra,i,j)
                        
        
                        

        for i in range(0,balls):
            if start :
                if velocities[0][0]!=0:
                    positions[i][0] = positions[i][0]+ velocities[i][0]
                    positions[i][1] = positions[i][1]- velocities[i][1]
                    Cc(greyesh,positions[i][0]-velocities[i][0],positions[i][1]+velocities[i][1],ball_ra[i])

            if make_ball:

                if abs(positions[i][0] <= ball_ra[i]) or abs(positions[i][0] >= (screen_width) - ball_ra[i]) :
                    velocities[i][0] = - velocities[i][0]
                if abs(positions[i][1] <= ball_ra[i] + bar_thic) or abs(positions[i][1] >= screen_height - ball_ra[i]) :
                    velocities[i][1] = - velocities[i][1]
                Cc(ball_col[i],positions[i][0],positions[i][1],ball_ra[i])

        pygame.draw.rect(appWindow,black,[0,0,screen_width, bar_thic])
        text_screen(f"Balls-{balls} | Radius-{ball_r} | FPS-{fps} | Speed-{ball_speed}",white,0,7,37)


        clock.tick(fps)
        pygame.display.update()

    pygame.quit()
    quit()

AppLoop()
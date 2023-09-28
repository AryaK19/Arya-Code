from asyncio import constants
import pygame 
import random
pygame.init()


# Colours
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)

screen_width = 600
screen_height = 500

# creating Window
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong")

# Game Specific variables
exit_game = False
game_over = False

#bar
bar_L_x = 40
bar_L_y = 250
bar_R_x = 550
bar_R_y = 250
bar_x = 15
bar_y = 130

fast = 10
fast_L = fast
fast_R = fast
velocity_L_y = 0
velocity_R_y = 0

#ball
ball_x = 300
ball_y = 250
ball_Ra = 8

ball_speed = 40
ball_velocity_x = random.randint(5,35)

ball_velocity_y = int(( ball_speed**2 - ball_velocity_x**2 )**0.5)

# constants
a = random.randint(1,4)
div_ratio = ball_speed/5

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

    

a = False


#other
fps = 50
clock = pygame.time.Clock()

def rect_create(colour,x,y,size_x,size_y):
    pygame.draw.rect(gameWindow,colour,[x,y, size_x, size_y])

# Creating a gameloop
while not exit_game:

    if abs(bar_R_y <= 0):
        velocity_R_y = fast
    elif abs(bar_R_y >= 500 - bar_y):
        velocity_R_y = -fast
    if abs(bar_L_y <= 0):
        velocity_L_y = fast
    elif abs(bar_L_y >= 500 - bar_y):
        velocity_L_y = -fast
    
    else :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game=True

                
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_w :
                    velocity_L_y = - fast
                elif event.key == pygame.K_s :
                    velocity_L_y = fast
                elif event.key == pygame.K_d:
                    velocity_L_y = 0

                if event.key == pygame.K_UP :
                    velocity_R_y = - fast
                elif event.key == pygame.K_DOWN :
                    velocity_R_y = fast
                elif event.key == pygame.K_LEFT:
                    velocity_R_y = 0

    if abs(ball_x == ball_Ra):
        ball_velocity_x = ball_velocity_x
        ball_velocity_y = -ball_velocity_y
    elif abs(ball_x == 500 - ball_Ra):
        ball_velocity_x = ball_velocity_x
        ball_velocity_y = -ball_velocity_y

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RETURN:
                a = True

    bar_L_y = bar_L_y + velocity_L_y
    bar_R_y = bar_R_y + velocity_R_y

    if a :
        ball_x = ball_x + ball_velocity_x
        ball_y = ball_y + ball_velocity_y




    gameWindow.fill(black)
    rect_create(white,bar_L_x,bar_L_y,bar_x,bar_y)
    rect_create(white,bar_R_x,bar_R_y,bar_x,bar_y)
    pygame.draw.circle(gameWindow,red,[ball_x,ball_y],ball_Ra)

            
    pygame.display.update()

    clock.tick(fps)
pygame.quit()
quit()
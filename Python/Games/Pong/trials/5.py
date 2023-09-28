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



font = pygame.font.SysFont(None,30)
def text_screen(text,colour,x,y,font):
    screen_text = font.render(text,True,colour)
    gameWindow.blit(screen_text,[x,y])

def rect_create(colour,x,y,size_x,size_y):
    pygame.draw.rect(gameWindow,colour,[x,y, size_x, size_y])

# Creating a gameloop
def gameloop():

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
    list_L = []
    list_R = []

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
    fps = 60
    with open("C:\\Users\\Aryak\\Arya Code\\Python Arya\\Games\\Pong\\player1s.txt") as f :
            p1 = f.read()
            s1 = p1.split()
    with open("C:\\Users\\Aryak\\Arya Code\\Python Arya\\Games\\Pong\\player2s.txt") as f :
            p2 = f.read()
            s2 = p2.split()
    score1=int(s1[0])
    score2=int(s2[0])

    clock = pygame.time.Clock()

    while not exit_game:

        list_L = []
        list_R = []
        for i in range(0,65):
            list_L.append(bar_L_y + i*2)
            list_R.append(bar_R_y + i*2)

        with open("C:\\Users\\Aryak\\Arya Code\\Python Arya\\Games\\Pong\\player1s.txt") as f :
            p1 = f.read()
            s1 = p1.split()
        with open("C:\\Users\\Aryak\\Arya Code\\Python Arya\\Games\\Pong\\player2s.txt") as f :
            p2 = f.read()
            s2 = p2.split()


        if abs(ball_x <= ball_Ra) or abs(ball_x >= screen_width - ball_Ra) :
            game_over = True
            if abs(ball_x <= ball_Ra) :
                score2 = score2 +1
            if abs(ball_x >= screen_width - ball_Ra):
                score1 = score1 +1
            if score1 > int(s1[0]):
                p1 = p1.replace(s1[0],str(score1))
            elif score2 > int(s2[0]):
                p2 = p2.replace(s2[0],str(score2))

            with open("C:\\Users\\Aryak\\Arya Code\\Python Arya\\Games\\Pong\\player1s.txt","w") as f :
                f.write(p1)
            with open("C:\\Users\\Aryak\\Arya Code\\Python Arya\\Games\\Pong\\player2s.txt","w") as f :
                f.write(p2)
            gameloop()
            

        else:
            if abs(ball_y <= ball_Ra) or abs(ball_y >= screen_height - ball_Ra) :
                ball_velocity_y = - ball_velocity_y
            
            for items in list_L:
                if abs(ball_y - items) ==0 and abs(ball_x - (bar_L_x + bar_x))<12:
                    ball_velocity_x = -ball_velocity_x
            for items in list_R:
                if abs(items - ball_y)==0 and abs((bar_R_x - bar_x + 10) - ball_x)<12:
                    ball_velocity_x = -ball_velocity_x


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


        text_screen(f"{score1} : Player 1",white,170,5,pygame.font.SysFont(None,30))
        text_screen(f"Player 2 : {score2}",white,320,5,pygame.font.SysFont(None,30))
                
        pygame.display.update()

        clock.tick(fps)
    pygame.quit()
    quit()

gameloop()
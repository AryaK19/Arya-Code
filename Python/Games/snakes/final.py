from tkinter import EventType
import pygame
import random as rn

pygame.init()
pygame.mixer.init()# to initiate the audio thing in pygame


# Colours
white = (222,222,222)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
colour = (12,187,150)

screen_width = 600
screen_height = 400

# creating Window
gameWindow = pygame.display.set_mode((screen_width,screen_height))

#Background Image
bgimg = pygame.image.load("C:\\Users\\Aryak\\Arya Code\\Python Arya\\Games\\snakes\\files\\ground.png")
bgimg = pygame.transform.scale(bgimg, (screen_width,screen_height)).convert_alpha()

snk_texU = pygame.image.load("C:\\Users\\Aryak\\Arya Code\\Python Arya\\Games\\snakes\\files\\textureU.png")
snk_texR = pygame.image.load("C:\\Users\\Aryak\\Arya Code\\Python Arya\\Games\\snakes\\files\\textureR.png")
snk_texD = pygame.image.load("C:\\Users\\Aryak\\Arya Code\\Python Arya\\Games\\snakes\\files\\textureD.png")
snk_texL = pygame.image.load("C:\\Users\\Aryak\\Arya Code\\Python Arya\\Games\\snakes\\files\\textureL.png")


# Game title
pygame.display.set_caption("SnakesWithArya")
pygame.display.update()

clock = pygame.time.Clock()

font = pygame.font.SysFont(None,30)
def text_screen(text,colour,x,y,font):
    screen_text = font.render(text,True,colour)
    gameWindow.blit(screen_text,[x,y])

def plot_snk(snk_tex,snake_size,snk_list):
    for x,y in snk_list:
        tex = pygame.transform.scale(snk_tex,(snake_size,snake_size)).convert_alpha()
        gameWindow.blit(tex,[x,y])


def welcome():
    exit_game = False

    while not exit_game:
        gameWindow.fill(colour)
        text_screen("Welcome to Snakes",black,130,100,pygame.font.SysFont(None,50))
        text_screen("Press Space to Continue ",black,89,170,pygame.font.SysFont(None,50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)

# game loop
def gameloop():

    # Game Specific variables
    exit_game = False
    game_over = False
    snake_x = 55
    snake_y = 584/2
    snake_size = 30
    fps=60
    
    snk_list = []
    snk_len = 1

    food_size = 10
    food_x = rn.randint(20,screen_width/2)
    food_y = rn.randint(20,screen_height/2)

    score = 0

    velocity_x = 0
    velocity_y = 0
    init_velocity = 3.4

    while not exit_game:
        with open("C:\\Users\\Aryak\\Arya Code\\Python Arya\\Games\\snakes\\files\\score.txt") as f:
            h_score = f.read()

        if score > int(h_score):
            with open("C:\\Users\\Aryak\\Arya Code\\Python Arya\\Games\\snakes\\files\\score.txt","w") as f:
                f.write(str(score))

        if game_over:
            gameWindow.fill(white)
            text_screen(f"Game Over!!, Press Enter to continue ",red,screen_width/7,screen_height/2.5,pygame.font.SysFont(None,35))
            text_screen(f"Score : {score}",black,screen_width/2.6,screen_height/2,pygame.font.SysFont(None,35))
            text_screen(f"High Score : {h_score}",black,screen_width/3.1,screen_height/1.7,pygame.font.SysFont(None,35))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RETURN :
                        gameloop()
            

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if score != 0:
                    if event.type == pygame.KEYDOWN:
                        if velocity_x != -init_velocity and event.key == pygame.K_RIGHT :
                            velocity_y = 0
                            velocity_x = init_velocity
                        if velocity_x != init_velocity and event.key == pygame.K_LEFT :
                            velocity_y = 0
                            velocity_x = -init_velocity
                            
                        if velocity_y != -init_velocity and event.key == pygame.K_DOWN :
                            velocity_x = 0
                            velocity_y = init_velocity
                        if velocity_y != init_velocity and event.key == pygame.K_UP :
                            velocity_x = 0
                            velocity_y = -init_velocity
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            velocity_y = 0
                            velocity_x = init_velocity
                        if event.key == pygame.K_LEFT:
                            velocity_y = 0
                            velocity_x = -init_velocity
                            
                        if event.key == pygame.K_DOWN:
                            velocity_x = 0
                            velocity_y = init_velocity
                        if event.key == pygame.K_UP:
                            velocity_x = 0
                            velocity_y = -init_velocity

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<18 and abs(snake_y - food_y)<18:# abs gives the absolute value
                score +=10
                food_x = rn.randint(70,screen_width/2)
                food_y = rn.randint(70,screen_height/2)
                snk_len +=7.5
                pygame.mixer.music.load("C:\\Users\\Aryak\\Arya Code\\Python Arya\\Games\\snakes\\files\\Beep.mp3")
                pygame.mixer.music.play()

            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen(f"Score : {score}",black,5,5,font)
            text_screen(f"High Score : {h_score}",black,430,5,pygame.font.SysFont(None,29))
            pygame.draw.rect(gameWindow,red,[food_x, food_y, food_size, food_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>(snk_len):
                del snk_list[0]
                if snk_list.index([snake_x,snake_y]) != (len(snk_list)-1):
                    game_over = True
                    pygame.mixer.music.load("C:\\Users\\Aryak\\Arya Code\\Python Arya\\Games\\snakes\\files\\deadsnk.mp3")
                    pygame.mixer.music.play()

                # if head in snk_list[:-1]:  # harry's code
                #     game_over = True


            if snake_x<0 or snake_y<0 or snake_x>screen_width or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load("C:\\Users\\Aryak\\Arya Code\\Python Arya\\Games\\snakes\\files\\deadsnk.mp3")
                pygame.mixer.music.play()
            if velocity_y == init_velocity:
                plot_snk(snk_texD,snake_size,snk_list)
            elif velocity_y == -init_velocity:
                plot_snk(snk_texU,snake_size,snk_list)
            elif velocity_x == init_velocity:
                plot_snk(snk_texR,snake_size,snk_list)
            elif velocity_x == -init_velocity:
                plot_snk(snk_texL,snake_size,snk_list)
            else:
                plot_snk(snk_texU,snake_size,snk_list)

        pygame.display.update()# to apply the changes 
        clock.tick(fps)


    pygame.quit()
    quit()

welcome()
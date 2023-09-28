import pygame
import random as rn
pygame.init()

# Colours
white = (222,222,222)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)

screen_width = 600
screen_height = 400

# creating Window
gameWindow = pygame.display.set_mode((screen_width,screen_height))

# Game title
pygame.display.set_caption("SnakesWithArya")
pygame.display.update()

clock = pygame.time.Clock()

font = pygame.font.SysFont(None,30)
def text_screen(text,colour,x,y,font):
    screen_text = font.render(text,True,colour)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,colour,snk_list,size,):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,colour,[x,y, size, size])


# game loop
def gameloop():

    # Game Specific variables
    exit_game = False
    game_over = False
    snake_x = 55
    snake_y = 584/2
    snake_size = 15
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
        with open("C:\Users\Aryak\Arya Code\Python Arya\Games\snakes\\files\score.txt") as f:
            h_score = f.read()

        if score > int(h_score):
            with open("C:\Users\Aryak\Arya Code\Python Arya\Games\snakes\\files\score.txt","w") as f:
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

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:# abs gives the absolute value
                score +=10
                food_x = rn.randint(70,screen_width/2)
                food_y = rn.randint(70,screen_height/2)
                snk_len +=7.5

            gameWindow.fill(white)
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

                # if head in snk_list[:-1]:  # harry's code
                #     game_over = True


            if snake_x<0 or snake_y<0 or snake_x>screen_width or snake_y>screen_height:
                game_over = True
            
            plot_snake(gameWindow,black,snk_list, snake_size,)

        pygame.display.update()# to apply the changes 
        clock.tick(fps)
    pygame.quit()
    quit()


gameloop()
import pygame
import random as rn
pygame.init()

# Colours
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)


screen_width = 900
screen_height = 600

# creating Window
gameWindow = pygame.display.set_mode((screen_width,screen_height))

# Game title
pygame.display.set_caption("SnakesWithArya")
pygame.display.update()

# Game Specific variables
exit_game = False
game_over = False
snake_x = 55
snake_y = 584/2
snake_size = 15
fps=60

food_size = 10
food_x = rn.randint(20,screen_width/1.5)
food_y = rn.randint(20,screen_height/1.5)

score = 0

velocity_x = 0
velocity_y = 0
init_velocity = 4

clock = pygame.time.Clock()

font = pygame.font.SysFont(None,30)
def text_screen(text,colour,x,y):
    screen_text = font.render(text,True,colour)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,colour,snk_list,size,):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,colour,[x,y, size, size])

snk_list = []
snk_len = 1

# game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
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
        score +=1
        food_x = rn.randint(20,screen_width/1.5)
        food_y = rn.randint(20,screen_height/1.5)
        snk_len +=7.5

    gameWindow.fill(white)
    text_screen(f"Score : {score*10}",black,5,5)
    pygame.draw.rect(gameWindow,red,[food_x, food_y, food_size, food_size])

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list)>(snk_len):
        del snk_list[0]

    plot_snake(gameWindow,black,snk_list, snake_size,)
    pygame.display.update()# to apply the changes 
    clock.tick(fps)


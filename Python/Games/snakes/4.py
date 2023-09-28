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
fps=30

food_size = 10
food_x = rn.randint(1,890)
food_y = rn.randint(1,690)

velocity_x = 0
velocity_y = 0

clock = pygame.time.Clock()


# game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_y = 0
                velocity_x = 7
            if event.key == pygame.K_LEFT:
                velocity_y = 0
                velocity_x = -7
                
            if event.key == pygame.K_DOWN:
                velocity_x = 0
                velocity_y = 7
            if event.key == pygame.K_UP:
                velocity_x = 0
                velocity_y = -7


    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow,red,[food_x, food_y, food_size, food_size])
    pygame.draw.rect(gameWindow,black,[snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()# to apply the changes 
    clock.tick(fps)


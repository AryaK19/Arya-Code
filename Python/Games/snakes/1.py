import pygame
pygame.init()

# Colours
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)


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
snake_x = 45
snake_y = 55
snake_size = 10
fps=30

clock = pygame.time.Clock()

# game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x + 10
            if event.key == pygame.K_LEFT:
                snake_x = snake_x - 10
                
            if event.key == pygame.K_DOWN:
                snake_y = snake_y + 10
            if event.key == pygame.K_UP:
                snake_y = snake_y - 10


    gameWindow.fill(white)
    pygame.draw.rect(gameWindow,black,[snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()# to apply the changes 
    clock.tick(fps)


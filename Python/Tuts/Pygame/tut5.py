
import pygame 
pygame.init()

# creating Window
gameWindow = pygame.display.set_mode((300,500))
pygame.display.set_caption("Name")

# Game Specific variables
run = True
game_over = False

# Creating a gameloop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            break
        if event.type == pygame.KEYDOWN:
            print(event)
            if event.key == pygame.K_RIGHT:
                print("You have pressed right arrow key")

pygame.quit()
quit()

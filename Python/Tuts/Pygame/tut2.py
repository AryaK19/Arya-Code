import pygame 
pygame.init()

# creating Window
gameWindow = pygame.display.set_mode((1200,500))
pygame.display.set_caption("My First Game")

# Game Specific variables
exit_game = False
game_over = False
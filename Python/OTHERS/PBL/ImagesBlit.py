import pygame
import os
pygame.init()

x = 0
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x},{y}"

pygame.display.set_mode([500,470])

image = pygame.image.load("Images\Synth.jpg").convert_alpha()
volume0 = pygame.image.load("Images\Buttons\\volume.png").convert_alpha()
pitchButtonDown = pygame.image.load("Images\pitchButtonDown.png").convert_alpha()
pitchButtonMid = pygame.image.load("Images\pitchButtonMid.png").convert_alpha()
pitchButtonUp = pygame.image.load("Images\pitchButtonUp.png").convert_alpha()
lightON = pygame.image.load("Images\lightON.png").convert_alpha()
lightOFF = pygame.image.load("Images\lightOFF.png").convert_alpha()
ONOFF = pygame.image.load("Images\ONOFF.png").convert_alpha()
Letters = pygame.image.load("Images\Letters.png").convert_alpha()
LettersB = pygame.image.load("Images\LettersB.png").convert_alpha()
Letters7 = pygame.image.load("Images\Letters7.png").convert_alpha()
Notes1 = pygame.image.load("Images\\Notes1.png").convert_alpha()
Notes4 = pygame.image.load("Images\\Notes4.png").convert_alpha()
Notes7 = pygame.image.load("Images\\Notes7.png").convert_alpha()
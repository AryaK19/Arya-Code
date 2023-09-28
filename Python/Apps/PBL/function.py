import pygame
pygame.init()

def keysImage(key):
    key = pygame.image.load(f"Images\keysPress\key{key}.png").convert_alpha()
    return key

def keysImageB(key):
    key = pygame.image.load(f"Images\keysPress\{key}.png").convert_alpha()
    return key
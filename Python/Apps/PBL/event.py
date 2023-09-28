import pygame
pygame.init()

def events(event,keyPresses):
    if event.type == pygame.KEYDOWN :
        if event.key == pygame.K_TAB:
            keyPresses['cpress'] = True   

    if event.type == pygame.KEYUP :
        if event.key == pygame.K_TAB:
            keyPresses['cpress'] = False   
           
            
            
import pygame
pygame.init()
import os

height,width = 400,900
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Does this work")

def makewindow():
    window.fill((100,200,240))
    
def rect(x, y):
    for a in range(x, x+40, 5):
        for b in range(y, y+70, 5):
            pygame.draw.rect(window, "black", (a,b,5,5))
    
    


def main():
    run = True
    while run:
        makewindow()
        pygame.draw.rect(window, "white", (100,100,40,70))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                POS = pygame.mouse.get_pos()
                rect(100,100)
                pygame.display.update()
                
        
        pygame.display.update()


    pygame.quit()

main()

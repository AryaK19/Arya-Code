import pygame
pygame.init()
import os
import time

height,width = 400,900
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Does this work")

def makewindow(a,b):
    window.fill((100,200,240))
    initialrect(a,b)
    pygame.display.update()

def initialrect(a,b):
    pygame.draw.rect(window, "white", (a,b,700,200))

def drawblack(a,b,x,y):
    if x+5 < a+700 and y+5 < b+200:
        pygame.draw.rect(window, "black", (x,y,5,5))


    
    

def main():
    run = True
    click = False
    a = 20
    b = 20
    makewindow(a,b)
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    POS = pygame.mouse.get_pos()
                    drawblack(a,b,POS[0],POS[1])
                    pygame.display.update()

                    

    pygame.quit()

main()
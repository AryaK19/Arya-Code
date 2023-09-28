import pygame
pygame.init()
import os
import time

height,width = 720,1280
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Does this work?")

def initialrect():
    for y in range(20,200,5):
        pygame.draw.rect(window, "white", (200,y,20,10))
        pygame.draw.rect(window, "white", (220,100,180,20))
        pygame.draw.rect(window,"white", (400,y,20,10))
        pygame.display.update()


def winscreen():
    font1 = pygame.font.SysFont("monospace", 60)
    text1 = font1.render("YOU WON!", 1, "yellow")
    window.blit(text1, (width/2 - 100,height/2 - 100))
    pygame.display.update()

def losescreen():
    font1 = pygame.font.SysFont("monospace", 60)
    text1 = font1.render("YOU LOST", 1, "yellow")
    window.blit(text1, (width/2 - 100,height/2 - 100))
    pygame.display.update()

def makebutton(text,x,y):
    pygame.draw.rect(window, "yellow", (x,y,330,40))
    font1 = pygame.font.SysFont("monospace", 20)
    text1 = font1.render(text, 1, "blue")
    window.blit(text1,(x+30,y+10))
    pygame.display.update()


def main():
    run = True
    loser = False
    window.fill((100,200,240))
    initialrect()
    makebutton("Right Click to continue", 100, 240)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                            POS = pygame.mouse.get_pos()
                            if POS[0] > 200 and POS[0] < 220 and POS[1] >= 20 and POS[1] <= 205:
                                POSx = (POS[1]//5) * 5
                                pygame.draw.rect(window, "black", (200,POSx,20,30))
                            elif POS[0] > 400 and POS[0] < 420 and POS[1] >= 20 and POS[1] <= 205:
                                POSx = (POS[1]//5) * 5
                                pygame.draw.rect(window, "black", (400,POSx,20,5))
                            elif POS[0] > 200 and POS[0] < 400 and POS[1] >= 100 and POS[1] <= 125:
                                POSy = (POS[0]//5) * 5
                                pygame.draw.rect(window, "black", (POSy, 100, 5, 20))
                            else:
                                pygame.draw.rect(window, (100,100,100), (POS[0],POS[1],5,5))
                            
                    if event.button == 3:
                        for A in range(1,width):
                            for B in range(1,height):
                                identity = window.get_at((A,B))
                                if identity == (255,255,255) or identity == (100,100,100):
                                    loser = True
                        if loser:
                            losescreen()
                        elif not loser:
                            winscreen()

                        
        pygame.display.update()
    pygame.quit()

main()
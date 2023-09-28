import pygame
pygame.init()
import os
import time

height,width = 400,900
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Does this work?")

# def initialrect(a,b,c,d,pics):
#     donot = 0
#     for x in range(a,b,10):
#         for y in range(c,d,10):
#             pics.append("T")
#             if pics[x*y - a*c] == "T":
#                 pygame.draw.rect(window, "white", (x,y,10,10))
#             else:
#                 pygame.draw.rect(window, "black", (x,y,10,10))

# def blackmouse(event, pics, x,y,a,c):
#     if event.type == pygame.MOUSEBUTTONDOWN:
#         if event.button == 1:
#                 POS = pygame.mouse.get_pos()
#                 if POS[0] in range(200,210) and POS[1] in range(200,210):
#                     pics[x*y - a*c] == "F"
#                     pygame.display.update()

def initialrect():
    for y in range(100,200,10):
        pygame.draw.rect(window, "white", (200,y,100,10))
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
    winner = None
    loser = False
    window.fill((100,200,240))
    initialrect()
    makebutton("Right Click to continue", 100, 240)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 0 or event.button == 1:
                            POS = pygame.mouse.get_pos()
                            if POS[0] > 200 and POS[0] < 300 and POS[1] >= 100 and POS[1] <= 200:
                                POSx = (POS[1]//10) * 10
                                pygame.draw.rect(window, "black", (200,POSx,100,10))
                                
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    for A in range(1,width):
                        for B in range(1,height):
                            identity = window.get_at((A,B))
                            if identity == (255,255,255):
                                loser = True
                    if loser:
                        losescreen()
                    elif not loser:
                        winscreen()
                                

            
                            
                            
            
            
                        
                                
                                    

        pygame.display.update()
    pygame.quit()

main()
import pygame
pygame.init()
import os

WIDTH,HEIGHT = 1200,750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PYTRACER")
COLOUR = (100,200,80)
FPS = 120
song = pygame.mixer.Sound("PYTRACER\\NIER.mp3")
song.play()
BACKGROUND_APP = pygame.image.load(os.path.join('PYTRACER','background.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND_APP,(WIDTH,HEIGHT))
BG2 = pygame.image.load(os.path.join('PYTRACER', 'background.png'))
BG2_R = pygame.transform.scale(BG2, (1200,750))

def Text(text,x,y):
    myfont = pygame.font.SysFont("monospace", 45)
    label = myfont.render(text, 1, "black")
    WIN.blit(label, (x, y))
    

def maingame():
    WIN.fill((100,200,240))
    make_Buttons(100,300,250,70,"Alphabet")
    make_Buttons(100,400,200,70,"Number")
    make_Buttons(100,500,200,70,"Back")
    

def make_Buttons(x,y,size_x,size_y,text):
    pygame.draw.rect(WIN,"white",[x,y,size_x,size_y])
    Text(text,x+30,y+10)
    
    

def menu():
    draw_window(WIN)
    make_Buttons(100,300,200,70,"Start")
    make_Buttons(100,400,200,70,"Sound")
    make_Buttons(100,500,200,70,"Quit")
    
def draw_window(WIN):
    
    WIN.blit(BACKGROUND,(0,0))
    

def loading():
    run = True
    
    soundplay = True
    CLOCK = pygame.time.Clock()
    menuBool = True
    maingameBool = True

    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if menuBool:
            menu()
            for event in pygame.event.get():
                if  event.type == pygame.MOUSEBUTTONDOWN:
                    POS = pygame.mouse.get_pos()
                    if POS[0] > 100 and POS[1] >500 and POS[0] <300 and POS[1] < 570:
                        if event.button == 1:
                            run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    POS = pygame.mouse.get_pos()
                    if POS[0] > 100 and POS[1] > 400 and POS[0] < 300 and POS[1] < 470:
                        if event.button == 1:
                            soundplay = not soundplay
                if event.type == pygame.MOUSEBUTTONDOWN:
                    POS = pygame.mouse.get_pos()
                    if POS[0] > 100 and POS[1] > 300 and POS[0] < 300 and POS[1] < 370:
                        if event.button == 1:
                            menuBool = False
                            

        else:
            maingame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                POS = pygame.mouse.get_pos()
                if POS[0] > 100 and POS[0] < 300 and POS[1] > 500 and POS[1] < 570:
                    menuBool  = True
            
            
                        
                                       
        if soundplay == False:
            pygame.mixer.pause()
        else:
            pygame.mixer.unpause()            
        pygame.display.update()
    pygame.quit()


loading()
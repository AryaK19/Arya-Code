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

def Text(text,x,y):
    myfont = pygame.font.SysFont("monospace", 45)
    label = myfont.render(text, 0, "black")
    WIN.blit(label, (x, y))
    pygame.display.update()


def make_Buttons(x,y,size_x,size_y,text):
    pygame.draw.rect(WIN,"white",[x,y,size_x,size_y])
    Text(text,x+30,y+10)
    pygame.display.update()
    

def menu():
    make_Buttons(100,300,200,70,"Start")
    make_Buttons(100,400,200,70,"Sound")
    make_Buttons(100,500,200,70,"Quit")
    
def draw_window(WIN):
    
    WIN.blit(BACKGROUND,(0,0))
    pygame.display.update()

def loading():
    run = True
    draw_window(WIN)
    soundplay = True
    CLOCK = pygame.time.Clock()
    while run:
        menu()
        
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif  event.type == pygame.MOUSEBUTTONDOWN:
                POS = pygame.mouse.get_pos()
                if POS[0] > 100 and POS[1] >500 and POS[0] <300 and POS[1] < 570:
                    if event.button == 1:
                        run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                POS = pygame.mouse.get_pos()
                if POS[0] > 100 and POS[0] < 300 and POS[1] > 400 and POS[1] < 470:
                    if event.button == 1:
                        soundplay = not soundplay

        if soundplay == False:
            pygame.mixer.pause()
        else:
            pygame.mixer.unpause()            

    pygame.quit()


loading()
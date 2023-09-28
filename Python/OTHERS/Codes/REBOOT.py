import pygame
pygame.init()
import os
import time
pygame.mixer.init()
pygame.mixer.set_num_channels(2)
os.chdir(r'\Users\Sai\Codes\Codes')

height,width = 900,1600
window = pygame.display.set_mode((width,height), pygame.FULLSCREEN)
pygame.display.set_caption('KINDERGARDEN 2.0')

NIER = pygame.mixer.Sound("NIER.mp3")
NIER.play()

BG1 = pygame.image.load(os.path.join("pygame assets", "balloonhouse.jpg"))
BG1_R = pygame.transform.scale(BG1, (width,height))
BG2 = pygame.image.load(os.path.join('pygame assets','woodenABC.jpg'))
BG2_R = pygame.transform.scale(BG2, (width,height))
BG3_R = pygame.transform.scale(pygame.image.load(os.path.join('pygame assets', 'numberbackground.jpg')), (width,height))
BG0 = pygame.image.load(os.path.join('pygame assets','colorfulbg.jpg'))
BG0_R = pygame.transform.scale(pygame.image.load(os.path.join('pygame assets', 'colorfulbg.jpg')), (width,height))

A = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "a.png")), (100,100))
B = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "b.png")), (100,100))
C = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "c.png")), (100,100))
D = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "d.png")), (100,100))
E = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "e.png")), (100,100))
F = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "f.png")), (100,100))
G = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "g.png")), (100,100))
H = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "h.png")), (100,100))
I = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "i.png")), (100,100))
J = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "j.png")), (100,100))
K = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "k.png")), (100,100))
L = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "l.png")), (100,100))
M = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "m.png")), (100,100))
N = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "n.png")), (100,100))
O = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "o.png")), (100,100))
P = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "p.png")), (100,100))
Q = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "q.png")), (100,100))
R = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "r.png")), (100,100))
S = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "s.png")), (100,100))
T = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "t.png")), (100,100))
U = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "u.png")), (100,100))
V = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "v.png")), (100,100))
W = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "w.png")), (100,100))
X = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "x.png")), (100,100))
Y = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "y.png")), (100,100))
Z = pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "z.png")), (100,100))
num1 =  pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "1.png")), (100,100))
num2 =  pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "2.png")), (100,100))
num3 =  pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "3.png")), (100,100))
num4 =  pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "4.png")), (100,100))
num5 =  pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "5.png")), (100,100))
num6 =  pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "6.png")), (100,100))
num7 =  pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "7.png")), (100,100))
num8 =  pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "8.png")), (100,100))
num9 =  pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "9.png")), (100,100))
#num0 =  pygame.transform.scale(pygame.image.load(os.path.join("pygame assets", "0.png")), (100,100))

Aa = pygame.mixer.Sound("a.mp3")
Ab = pygame.mixer.Sound("b.mp3")
Ac = pygame.mixer.Sound("c.mp3")
Ad = pygame.mixer.Sound("d.mp3")
Ae = pygame.mixer.Sound("e.mp3")
Af = pygame.mixer.Sound("f.mp3")
Ag = pygame.mixer.Sound("g.mp3")
Ah = pygame.mixer.Sound("h.mp3")
Ai = pygame.mixer.Sound("i.mp3")
Aj = pygame.mixer.Sound("j.mp3")
Ak = pygame.mixer.Sound("k.mp3")
Al = pygame.mixer.Sound("l.mp3")
Am = pygame.mixer.Sound("m.mp3")
An = pygame.mixer.Sound("n.mp3")
Ao = pygame.mixer.Sound("o.mp3")
Ap = pygame.mixer.Sound("p.mp3")
Aq = pygame.mixer.Sound("q.mp3")
Ar = pygame.mixer.Sound("r.mp3")
As = pygame.mixer.Sound("s.mp3")
At = pygame.mixer.Sound("t.mp3")
Au = pygame.mixer.Sound("u.mp3")
Av = pygame.mixer.Sound("v.mp3")
Aw = pygame.mixer.Sound("w.mp3")
Ax = pygame.mixer.Sound("x.mp3")
Ay = pygame.mixer.Sound("y.mp3")
Az = pygame.mixer.Sound("z.mp3")
A1 = pygame.mixer.Sound("1.mp3")
A2 = pygame.mixer.Sound("2.mp3")
A3 = pygame.mixer.Sound("3.mp3")
A4 = pygame.mixer.Sound("4.mp3")
A5 = pygame.mixer.Sound("5.mp3")
A6 = pygame.mixer.Sound("6.mp3")
A7 = pygame.mixer.Sound("7.mp3")
A8 = pygame.mixer.Sound("8.mp3")
A9 = pygame.mixer.Sound("9.mp3")

def screen():
    window.blit(BG1_R, (0,0))

def makebuttons(text,x,y,a,b):
    pygame.draw.rect(window, "red", (x,y,a,b))
    fontx = pygame.font.SysFont("italic", 50)
    textx = fontx.render(text, 1, "yellow")
    window.blit(textx, (x+30, y+10))

def alphamenu(text,x,y,a,b,z):
    makebuttons(text,x,y,a,b)
    window.blit(z, (x+15,y+10))

def nummenu(text,x,y,a,b,z):
    makebuttons(text,x,y,a,b)
    window.blit(z, (x+15,y+10))

def mainmenu():
    window.blit(BG0_R,(0,0))
    makebuttons("Start",100,300,200,70)
    makebuttons("Sound",100,400,200,70)
    makebuttons("Quit",100,500,200,70)
    
def maincode():
    mainvalue = True
    menuvalue = False
    alphavalue = False
    numvalue = False
    soundplay = True
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if mainvalue:
            mainmenu()
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
                         menuvalue = True
                         mainvalue = False
            if soundplay == False:
                pygame.mixer.pause()
            else:
                pygame.mixer.unpause()

        elif menuvalue:
            screen()
            makebuttons("NUMBERS",300,200,250,60)
            makebuttons("ALPHABETS",300,300,280,60)
            makebuttons("BACK", 300,400,150,60)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        POS = pygame.mouse.get_pos()
                        if POS[0] > 300 and POS[0] < 450 and POS[1] > 400 and POS[1] < 460:
                            mainvalue = True
                            menuvalue = False
                        elif POS[0] in range(300,580) and POS[1] in range(300,360):
                            menuvalue = False
                            alphavalue = True
                        elif POS[0] in range(300,550) and POS[1] in range(200,260):
                            menuvalue = False
                            numvalue = True

        elif alphavalue and not menuvalue and not numvalue:
            window.blit(BG2_R, (0,0))
            alphamenu("",100,100,130,130,A)
            alphamenu("",300,100,130,130,B)
            alphamenu("",500,100,130,130,C)
            alphamenu("",700,100,130,130,D)
            alphamenu("",900,100,130,130,E)
            alphamenu("",1100,100,130,130,F)
            alphamenu("",1300,100,130,130,G)
            alphamenu("",100,300,130,130,H)
            alphamenu("",300,300,130,130,I)
            alphamenu("",500,300,130,130,J)
            alphamenu("",700,300,130,130,K)
            alphamenu("",900,300,130,130,L)
            alphamenu("",1100,300,130,130,M)
            alphamenu("",1300,300,130,130,N)
            alphamenu("",100,500,130,130,O)
            alphamenu("",300,500,130,130,P)
            alphamenu("",500,500,130,130,Q)
            alphamenu("",700,500,130,130,R)
            alphamenu("",900,500,130,130,S)
            alphamenu("",1100,500,130,130,T)
            alphamenu("",1300,500,130,130,U)
            alphamenu("",100,700,130,130,V)
            alphamenu("",300,700,130,130,W)
            alphamenu("",500,700,130,130,X)
            alphamenu("",700,700,130,130,Y)
            alphamenu("",900,700,130,130,Z)

            pygame.draw.rect(window, "black", (1300,700,130,60))
            fontx = pygame.font.SysFont("italic",50)
            label = fontx.render("BACK", 1, "white")
            window.blit(label, (1305,705))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if pos[0] in range(1300,1430) and pos[1] in range(700,760):
                        alphavalue = False
                        menuvalue = True
                    if pos[0] in range(100,230) and pos[1] in range(100,230):
                        Aa.play()
                    elif pos[0] in range(300,430) and pos[1] in range(100,230):
                        Ab.play()
                    elif pos[0] in range(500,630) and pos[1] in range(100,230):
                        Ac.play()
                    elif pos[0] in range(700,830) and pos[1] in range(100,230):
                        Ad.play()
                    elif pos[0] in range(900,1030) and pos[1] in range(100,230):
                        Ae.play()
                    elif pos[0] in range(1100,1230) and pos[1] in range(100,230):
                        Af.play()
                    elif pos[0] in range(1300,1430) and pos[1] in range(100,230):
                        Ag.play()
                    elif pos[0] in range(100,230) and pos[1] in range(300,430):
                        Ah.play()
                    elif pos[0] in range(300,430) and pos[1] in range(300,430):
                        Ai.play()
                    elif pos[0] in range(500,630) and pos[1] in range(300,430):
                        Aj.play()
                    elif pos[0] in range(700,830) and pos[1] in range(300,430):
                        Ak.play()
                    elif pos[0] in range(900,1030) and pos[1] in range(300,430):
                        Al.play()
                    elif pos[0] in range(1100,1230) and pos[1] in range(300,430):
                        Am.play()
                    elif pos[0] in range(1300,1430) and pos[1] in range(300,430):
                        An.play()
                    elif pos[0] in range(100,230) and pos[1] in range(500,630):
                        Ao.play()
                    elif pos[0] in range(300,430) and pos[1] in range(500,630):
                        Ap.play()
                    elif pos[0] in range(500,630) and pos[1] in range(500,630):
                        Aq.play()
                    elif pos[0] in range(700,830) and pos[1] in range(500,630):
                        Ar.play()
                    elif pos[0] in range(900,1030) and pos[1] in range(500,630):
                        As.play()
                    elif pos[0] in range(1100,1230) and pos[1] in range(500,630):
                        At.play()
                    elif pos[0] in range(1300,1430) and pos[1] in range(500,630):
                        Au.play()
                    elif pos[0] in range(100,230) and pos[1] in range(700,830):
                        Av.play()
                    elif pos[0] in range(300,430) and pos[1] in range(700,830):
                        Aw.play()
                    elif pos[0] in range(500,630) and pos[1] in range(700,830):
                        Ax.play()
                    elif pos[0] in range(700,830) and pos[1] in range(700,830):
                        Ay.play()
                    elif pos[0] in range(900,1030) and pos[1] in range(700,830):
                        Az.play()

                    


            
        elif numvalue and not menuvalue and not alphavalue:
                window.blit(BG3_R,(0,0))
                nummenu("",100,100,130,130,num1)
                nummenu("",300,100,130,130,num2)
                nummenu("",500,100,130,130,num3)
                nummenu("",700,100,130,130,num4)
                nummenu("",900,100,130,130,num5)
                nummenu("",1100,100,130,130,num6)
                nummenu("",1300,100,130,130,num7)
                nummenu("",600,300,130,130,num8)
                nummenu("",800,300,130,130,num9)
                
                pygame.draw.rect(window, "black", (1300,700,130,60))
                fontx = pygame.font.SysFont("italic",50)
                label = fontx.render("BACK", 1, "white")
                window.blit(label, (1305,705))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        if pos[0] in range(1300,1430) and pos[1] in range(700,760):
                            numvalue = False
                            menuvalue = True
                        if pos[0] in range(100,230) and pos[1] in range(100,230):
                            A1.play()
                        elif pos[0] in range(300,430) and pos[1] in range(100,230):
                            A2.play()
                        elif pos[0] in range(500,630) and pos[1] in range(100,230):
                            A3.play()
                        elif pos[0] in range(700,830) and pos[1] in range(100,230):
                            A4.play()
                        elif pos[0] in range(900,1030) and pos[1] in range(100,230):
                            A5.play()
                        elif pos[0] in range(1100,1230) and pos[1] in range(100,230):
                            A6.play()
                        elif pos[0] in range(1300,1430) and pos[1] in range(100,230):
                            A7.play()
                        elif pos[0] in range(600,730) and pos[1] in range(300,430):
                            A8.play()
                        elif pos[0] in range(800,930) and pos[1] in range(300,430):
                            A9.play()
                        pygame.display.update()
                        
        
        pygame.display.update()
    pygame.quit()

maincode()
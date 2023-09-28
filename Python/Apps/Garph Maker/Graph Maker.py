
import pygame
from math import *

pygame.init()


#colours 
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
greyesh = (210,210,210)
black_1 = (170,170,170)

screen_width = 700
screen_height = 700

clock = pygame.time.Clock()

def Rect(colour,x,y,xx,yy):
    return pygame.draw.rect(appWindow,colour,[x,y,xx, yy])


def TextScreen(text,colour,x,y,size):
    screen_text = pygame.font.SysFont(None,size).render(text,True,colour)
    appWindow.blit(screen_text,[x,y])

# creating Window
appWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Graph Maker")
appWindow.fill(greyesh)


def AppLoop():
    exit_app = False
    edit = False
    make_graph = False
    enter =False 
    forgot =False 
    sli = 0
    zoom = 0
    events = []
    plotPoints = []
    appWindow.fill(greyesh)
    fps=35
    


    while not exit_app:

        Rect(greyesh,30 + sli*18,0,screen_width-(30 + sli*18),screen_height)
        Rect(greyesh,0,35,30 + sli*18,screen_height-35)

        Rect(black,(screen_width)/2,0,2,screen_height)
        Rect(black,0,(screen_height)/2,screen_width,2)
        Rect(black_1,sli*18,0,30,35)


        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                exit_app = True
                
        
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (event.pos[0] <=(30 + i*28) and event.pos[1] <= 35):
                edit = True
                
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (event.pos[0] > (30 + i*28) and event.pos[1] > 35):
                edit = False
                if edit:
                    Rect(black,2,0,2,35)

            if event.type == pygame.KEYDOWN :
                if event.key != pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    if edit: 
                        if event.type  == pygame.KEYDOWN and event.key  != pygame.K_LSHIFT and event.key != pygame.K_RETURN:
                            enter = False
                            forgot = False
                            events.append(event.unicode) 
                            TextScreen(sli*"   "+event.unicode,black,5,5,30)
                            sli += 1
                            

                    
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    AppLoop()


                if event.key == pygame.K_RETURN:
                    make_graph = True
                    try:
                        inpq = events[0]
                        inpa = ''
                        for i in range(1,len(events)):
                            if events[i]=='=':
                                break
                            inpq = inpq+ events[i]
                        for i in range (events.index("=")+1,len(events)):
                            inpa = inpa+ events[i]

                    except  IndexError:
                        enter = True
                        

                    except ValueError:
                        forgot=True
                        

                    


            if event.type == pygame.MOUSEWHEEL and event.y == 1:
                zoom+=0
                
                
            if event.type == pygame.MOUSEWHEEL and event.y == -1:
                zoom-=0

        if forgot:
            TextScreen("Forgot '=' ?",black,5,37,30)
        elif enter:
            TextScreen("Enter pls",black,5,37,30)



        if make_graph:
            try:
                if inpq == 'y': 
                    for x in range(-350, 350):
                        y = eval(inpa)
                        x = (x*20) + 350
                        y = 350 - (y*20 )
                        plotPoints.append([int(x), int(y)])
                    
                elif inpq == 'x': 
                    for y in range(-350, 350):
                        x = eval(inpa)

                        x = (x*20) + 350
                        y = 350 - (y*20)
                        plotPoints.append([int(x), int(y)])

                # for i in range (0,len(plotPoints)):   
                #     Rect(red,plotPoints[i][0],plotPoints[i][1],2,2)
                pygame.draw.lines(appWindow,red,False,plotPoints,2)

            except Exception:
                pass

    

        

        if 20+zoom<=2 :
            for i in range (int(screen_width/2),int(screen_width),2):
                Rect(black,((screen_width)/2)-4,i,10,2)
                Rect(black,i,((screen_height)/2)-4,2,10)
            for i in range (0,int((screen_width/2)),2):
                var = int((screen_width/2) - i) 
                Rect(black,((screen_width/2))-4,var,10,2)
                Rect(black,var,((screen_height/2))-4,2,10)
        elif 20+zoom > 2:
            add1 = 1
            add2 = 1
            
            for i in range (int(screen_width/2),int((screen_width)),20+zoom):
                Rect(black,((screen_width)/2)-4,i,10,2)
                Rect(black,i,((screen_height)/2)-4,2,10)           
                TextScreen(f"{add1}",black,i+zoom+13,int((screen_width/2)+7),int(20+zoom/2))
                TextScreen(f"{-add1}",black,int((screen_width/2)+7),i+zoom+12,int(20+zoom/2))
                add1+=1
            
            for i in range (0,int((screen_width/2)),20+zoom):
                var = int((screen_width/2) - i) 
                Rect(black,var,((screen_height/2))-4,2,10)
                Rect(black,((screen_width/2))-4,var,10,2)
                TextScreen(f"{-add2}",black,var-zoom-28 ,int((screen_width/2)+7),int(20+zoom/2))
                TextScreen(f"{add2}",black,int((screen_height/2)+7),var-zoom-28 ,int(20+zoom/2))
                add2+=1
        

        TextScreen("0",black,(screen_width+4)/2,(screen_height+2)/2,25)
        clock.tick(fps)
        pygame.display.update()
    pygame.quit()
    quit()

AppLoop()
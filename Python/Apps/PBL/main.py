import pygame
from Functions import*
from Events import events
from ImagesBlit import*
from LoadingScreen import loadingScreen

pygame.init()
pygame.mixer.set_num_channels(80)


def main():
 

    width, height = 1370,710

    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption("PyPiano") 

    keynamesW = ["c","d","e","f","g","a","b"]
    keynamesB = ["cd","de","fg","ga","ab"]
    
    keyImages = {}
    for i in keynamesW:
        for j in range(1,4):
            if j == 1:
                keyImages.update({"key"+i : keysImage(i)})
            else :
                keyImages.update({"key"+i+str(j) : keysImage(i + str(j))})

    for i in keynamesB:
        for j in range(1,4):
            if j == 1:
                keyImages.update({"key"+i : keysImageB(i)})
            else :
                keyImages.update({"key"+i+str(j) : keysImageB(i + str(j))})
    keyImages.update({"keyl" : keysImage("l")})

    keyPresses = {}
    for i in keynamesW:
        for j in range(1,4):
            if j == 1:
                keyPresses.update({i+"press" : False})
            else :
                keyPresses.update({i+str(j)+"press" : False})

    for i in keynamesB:
        for j in range(1,4):
            if j == 1:
                keyPresses.update({i+"press" : False})
            else :
                keyPresses.update({i+str(j)+"press" : False})
    keyPresses.update({"lpress" : False}) 

    volume30 = pygame.transform.rotate(volume0,30)
    volume60 = pygame.transform.rotate(volume0,60)
    volume90 = pygame.transform.rotate(volume0,90)
    volume120 = pygame.transform.rotate(volume0,120)
    volume150 = pygame.transform.rotate(volume0,150)
    volume30n = pygame.transform.rotate(volume0,-30)
    volume60n = pygame.transform.rotate(volume0,-60)
    volume90n = pygame.transform.rotate(volume0,-90)
    volume120n = pygame.transform.rotate(volume0,-120)
    volume150n = pygame.transform.rotate(volume0,-150)
    
    run = True 
    fps = 120
    clock = pygame.time.Clock()
    
    ON = False
    angle = 0
    spin = 1
    pitch = 0 
    showLetters = False
    showNotes = False


    while run:

        screen.blit(image,(0,0,width,height))
         
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                print(pygame.mouse.get_pos())
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEWHEEL:
                pos = pygame.mouse.get_pos()
                if pos[0] > 120 and pos[1] > 103 and pos[0] < 170 and pos[1] < 140:
                    if event.y == 1 and angle != 150:
                        angle+=30
                    if event.y == -1 and angle != -150:
                        angle-=30
                spin = pitchButton(event,spin)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] > 223 and pos[1] > 326 and pos[0] < 245 and pos[1] < 349:
                    if event.button == 1:
                        showLetters = not showLetters
                if pos[0] > 273 and pos[1] > 326 and pos[0] < 295 and pos[1] < 349:
                    if event.button == 1:
                        showNotes = not showNotes
                if pos[0] > 275 and pos[1] > 275 and pos[0] < 294 and pos[1] < 294:
                    if event.button == 1:
                        ON = not ON

            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and spin!=2:
                spin+=1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and spin!=0:
                spin-=1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and spin!=2:
                spin+=1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKQUOTE and spin!=0:
                spin-=1

            if ON:  
                events(event,keyPresses,pitch,angle)      

        if ON:
            
            keypress(screen,width,height,keyImages,keyPresses) 

        if angle == 30:
            screen.blit(volume30,(112,96))
        elif angle == 60:
            screen.blit(volume60,(112,96))
        elif angle == 90:
            screen.blit(volume90,(120,103))
        elif angle == 120:
            screen.blit(volume120,(112,96))
        elif angle == 150:
            screen.blit(volume150,(112,96))          
        elif angle == -30:
            screen.blit(volume30n,(112,96))
        elif angle == -60:
            screen.blit(volume60n,(112,96))
        elif angle == -90:
            screen.blit(volume90n,(120,103))
        elif angle == -120:
            screen.blit(volume120n,(112,96))
        elif angle == -150:
            screen.blit(volume150n,(112,96))

        if angle != 150:
            screen.blit(ONOFF,(223,277))
        if ON:
            screen.blit(ONOFF,(277,277))

        if spin == 0:
            if showNotes:
                screen.blit(Notes1,(0,0))
            if showLetters:
                screen.blit(LettersB,(0,0))
                screen.blit(Letters,(0,-5))
            
            pitch = -3
            screen.blit(pitchButtonDown,(0,0))
            screen.blit(lightOFF,(131,328))
                    
        elif spin == 1:
            if showNotes:
                screen.blit(Notes4,(-2,-8))
            if showLetters:
                screen.blit(LettersB,(0,0))                
                screen.blit(Letters,(0,-5))  
            pitch = 0
            screen.blit(pitchButtonMid,(0,0))
            screen.blit(lightOFF,(89,328))
                    
        elif spin == 2:
            if showNotes:
                screen.blit(Notes7,(0,0))
            if showLetters: 
                screen.blit(LettersB,(0,0))
                screen.blit(Letters7,(0,-5))
            pitch = 3
            screen.blit(pitchButtonUp,(0,0))
            screen.blit(lightOFF,(131,328))
            screen.blit(lightOFF,(89,328))
            screen.blit(lightON,(173,328))

        if not showLetters:
            screen.blit(lightOFF,(224,328))
        if not showNotes:
            screen.blit(lightOFF,(273,328))
        

        clock.tick(fps)
        pygame.display.update()

    pygame.quit()
    quit()


loadingScreen()
main()
import pygame

pygame.init()
from Functions import keysLoad,keysBlitLoad

def loadingScreen():


    width,height = 500,470
    screen = pygame.display.set_mode([width,height])
    pygame.display.set_caption("Loading......")
    icon = pygame.image.load("Images\Loading keys.png")
    pygame.display.set_icon(icon)

    title = pygame.image.load("Images\Loading animation\Title.png")
    screen.blit(title,(150,20))

    loadingd = pygame.image.load("Images\Loading animation\Loading..png")   
    screen.blit(loadingd,(135,400)) 

    loadingdd = pygame.image.load("Images\Loading animation\Loading...png")
    loadingddd = pygame.image.load("Images\Loading animation\Loading....png")
    loadingdddd = pygame.image.load("Images\Loading animation\Loading.....png")
    

    key1 = keysLoad("1")
    key2 = keysLoad("2")
    key3 = keysLoad("3")
    key4 = keysLoad("4")
    key5 = keysLoad("5")
    key6 = keysLoad("6")
    key7 = keysLoad("7")
    key8 = keysLoad("8")

    time = 5
    seconds = 0
    secondsp = 0
    run = True 
    
    fps = 30
    clock = pygame.time.Clock()

    while run:
        image = pygame.image.load("Images\Loading keys.png").convert_alpha()
        screen.blit(image,(0,70,width,height))

        for i in range (1,9):
            if seconds>=fps*i/2:
               
                keysBlitLoad(screen,width,height,eval(f"key{i}"))

        if secondsp%(fps) == 0 and secondsp !=0 and secondsp < fps*9:
            music = pygame.mixer.Sound(f"Images\Loading animation\\{int((secondsp/fps))}.wav").play()  
            music.set_volume(0.4)

        if seconds == fps*time:
            run = False
            break    
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RETURN:
                    print(pygame.mouse.get_pos())
                    
        if secondsp%fps == 0 :
            if int(secondsp/fps) == 1:
                screen.blit(loadingdd,(135,400))
            elif int(secondsp/fps) == 2:
                pygame.draw.rect(screen,"black",(135,400,250,40))
                screen.blit(loadingddd,(135,400))
            elif int(secondsp/fps) == 3:
                pygame.draw.rect(screen,"black",(135,400,250,40))
                screen.blit(loadingdddd,(135,400))
            elif int(secondsp/fps) == 4:
                pygame.draw.rect(screen,"black",(135,400,250,40))
                screen.blit(loadingd,(135,400))
            
            elif int(secondsp/fps) == 5:
                pygame.draw.rect(screen,"black",(135,400,250,40))
                screen.blit(loadingdd,(135,400))
            elif int(secondsp/fps) == 6:
                pygame.draw.rect(screen,"black",(135,400,250,40))
                screen.blit(loadingddd,(135,400))
            elif int(secondsp/fps) == 7:
                pygame.draw.rect(screen,"black",(135,400,250,40))
                screen.blit(loadingdddd,(135,400))
            elif int(secondsp/fps) == 8:
                pygame.draw.rect(screen,"black",(135,400,250,40))
                screen.blit(loadingd,(135,400))
            
        clock.tick(fps)        
        pygame.display.update()

        seconds += 1
        secondsp += 2
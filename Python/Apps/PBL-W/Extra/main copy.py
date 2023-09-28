import os
import pygame

pygame.init()

pygame.mixer.set_num_channels(50)

def pitchButton(event,spin):
    
    pos = pygame.mouse.get_pos()
    if pos[0] > 58 and pos[1] > 511 and pos[0] < 85 and pos[1] < 606:
        if event.y == 1 and spin != 2:
            spin+=event.y
        if event.y == -1 and spin != 0:
            spin+=event.y
       
    return spin
        

def keyPlay(key,angle):
    press = True 
    music = pygame.mixer.Sound(f"Audio\keys\{key}.wav").play()
    
    music.set_volume(-(angle - 150)/300)
    return press,music
def keyPlayB(key,angle):
    key = str(key)
    press = True
    if len(key) == 2:
        music = pygame.mixer.Sound(f"Audio\keys\{key[1].upper()}b1.wav").play()
      
    else:
        music = pygame.mixer.Sound(f"Audio\keys\{key[1].upper()}b{key[2]}.wav").play()
        
    music.set_volume(-(angle - 150)/300)
    
    
    return press,music
    
    

def keyPress(screen,width,height,key,booli):
    if booli:
       screen.blit(key,(0,0,width,height)) 
def keyPressB(screen,width,height,key,booli):
    if booli:
       screen.blit(key,(0,0,width,height)) 

def keysImage(key):
    key = pygame.image.load(f"Images\keysPress\key{key}.png").convert_alpha()
    return key
def keysImageB(key):
    key = pygame.image.load(f"Images\keysPress\{key}.png").convert_alpha()
    return key

def keysLoad(key):
    key = pygame.image.load(f"Images\Loading animation\\{key}.png").convert_alpha()
    return key

def keysBlitLoad(screen,width,height,key):
    screen.blit(key,(0,70,width,height))
   


def loadingScreen():
    
    x = 0
    y = 30
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x},{y}"

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

    time = 1
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
            main()    
        
            

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
   


def main():

    
    image = pygame.image.load("Images\Synth.jpg").convert_alpha()
    volume0 = pygame.image.load("Images\Buttons\\volume.png").convert_alpha()
    pitchButtonDown = pygame.image.load("Images\pitchButtonDown.png").convert_alpha()
    pitchButtonMid = pygame.image.load("Images\pitchButtonMid.png").convert_alpha()
    pitchButtonUp = pygame.image.load("Images\pitchButtonUp.png").convert_alpha()
    lightON = pygame.image.load("Images\lightON.png").convert_alpha()
    lightOFF = pygame.image.load("Images\lightOFF.png").convert_alpha()
    ONOFF = pygame.image.load("Images\ONOFF.png").convert_alpha()

    Letters = pygame.image.load("Images\Letters.png").convert_alpha()
    LettersB = pygame.image.load("Images\LettersB.png").convert_alpha()
    Letters7 = pygame.image.load("Images\Letters7.png").convert_alpha()
    Notes1 = pygame.image.load("Images\\Notes1.png").convert_alpha()
    Notes4 = pygame.image.load("Images\\Notes4.png").convert_alpha()
    Notes7 = pygame.image.load("Images\\Notes7.png").convert_alpha()


    keyc = keysImage("c")
    keyd = keysImage("d")
    keye = keysImage("e")
    keyf = keysImage("f")
    keyg = keysImage("g")
    keya = keysImage("a")
    keyb = keysImage("b")
    keyc2 = keysImage("c2")
    keyd2 = keysImage("d2")
    keye2 = keysImage("e2")
    keyf2 = keysImage("f2")
    keyg2 = keysImage("g2")
    keya2 = keysImage("a2")
    keyb2 = keysImage("b2")
    keyc3 = keysImage("c3")
    keyd3 = keysImage("d3")
    keye3 = keysImage("e3")
    keyf3 = keysImage("f3")
    keyg3 = keysImage("g3")
    keya3 = keysImage("a3")
    keyb3 = keysImage("b3")
    keyl  = keysImage("l")
    keycd  = keysImageB("cd")
    keyde  = keysImageB("de")
    keyfg  = keysImageB("fg")
    keyga  = keysImageB("ga")
    keyab  = keysImageB("ab")
    keycd2  = keysImageB("cd2")
    keyde2  = keysImageB("de2")
    keyfg2  = keysImageB("fg2")
    keyga2  = keysImageB("ga2")
    keyab2  = keysImageB("ab2")
    keycd3  = keysImageB("cd3")
    keyde3  = keysImageB("de3")
    keyfg3  = keysImageB("fg3")
    keyga3  = keysImageB("ga3")
    keyab3  = keysImageB("ab3")
   
    
    
    width, height = 1370,710

    screen = pygame.display.set_mode([width, height])

    pygame.display.set_caption("PyPiano") 

    
    cpress,cmusic = False,True
    dpress,dmusic = False,True
    epress,emusic = False,True
    fpress,fmusic = False,True
    gpress,gmusic = False,True
    apress,amusic = False,True
    bpress,bmusic = False,True
    c2press,c2music = False,True
    d2press,d2music = False,True
    e2press,e2music = False,True
    f2press,f2music = False,True
    g2press,g2music = False,True
    a2press,a2music = False,True
    b2press,b2music = False,True
    c3press,c3music = False,True
    d3press,d3music = False,True
    e3press,e3music = False,True
    f3press,f3music = False,True
    g3press,g3music = False,True
    a3press,a3music = False,True
    b3press,b3music = False,True
    lpress = False
    cdpress,cdmusic = False,True
    depress,demusic = False,True
    fgpress,fgmusic = False,True
    gapress,gamusic = False,True
    abpress,abmusic = False,True
    cd2press,cd2music = False,True
    de2press,de2music = False,True
    fg2press,fg2music = False,True
    ga2press,ga2music = False,True
    ab2press,ab2music = False,True
    cd3press,cd3music = False,True
    de3press,de3music = False,True
    fg3press,fg3music = False,True
    ga3press,ga3music = False,True
    ab3press,ab3music = False,True
    

    run = True 
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
    
    fps = 120
    clock = pygame.time.Clock()
 
    angle = 0
    spin = 1
    pitch = 0 
    showLetters = False
    showNotes = False

    while run:

        screen.blit(image,(0,0,width,height))
         
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RETURN:
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
                
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RETURN:
                    print(pygame.mouse.get_pos())

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP and spin!=2:
                    spin+=1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and spin!=0:
                    spin-=1
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    cpress,cmusic = keyPlay("c".upper()+f"{pitch + 4}",angle)
                if event.key == pygame.K_q:
                    dpress,dmusic = keyPlay("d".upper()+f"{pitch + 4}",angle)
                if event.key == pygame.K_w:
                    epress,emusic = keyPlay("e".upper()+f"{pitch + 4}",angle)
                if event.key == pygame.K_e:
                    fpress,fmusic = keyPlay("f".upper()+f"{pitch + 4}",angle)
                if event.key == pygame.K_r:
                    gpress,gmusic = keyPlay("g".upper()+f"{pitch + 4}",angle)
                if event.key == pygame.K_t:
                    apress,amusic = keyPlay("a".upper()+f"{pitch + 4}",angle)
                if event.key == pygame.K_y:
                    bpress,bmusic = keyPlay("b".upper()+f"{pitch + 4}",angle)

                if event.key == pygame.K_1:
                    cdpress,cdmusic = keyPlayB("cd"+str(pitch + 4),angle)
                if event.key == pygame.K_2:
                    depress,demusic = keyPlayB("de"+str(pitch + 4),angle)
                if event.key == pygame.K_4:
                    fgpress,fgmusic = keyPlayB("fg"+str(pitch + 4),angle)
                if event.key == pygame.K_5:
                    gapress,gamusic = keyPlayB("ga"+str(pitch + 4),angle)
                if event.key == pygame.K_6:
                    abpress,abmusic = keyPlayB("ab"+str(pitch + 4),angle)
               
                if pitch !=3:
                    if event.key == pygame.K_u:
                        c2press,c2music = keyPlay("c".upper()+f"{pitch + 5}",angle)
                    if event.key == pygame.K_i:
                        d2press,d2music = keyPlay("d".upper()+f"{pitch + 5}",angle)
                    if event.key == pygame.K_o:
                        e2press,e2music = keyPlay("e".upper()+f"{pitch + 5}",angle)
                    if event.key == pygame.K_p:
                        f2press,f2music = keyPlay("f".upper()+f"{pitch + 5}",angle)
                    if event.key == pygame.K_LEFTBRACKET:
                        g2press,g2music = keyPlay("g".upper()+f"{pitch + 5}",angle)
                    if event.key == pygame.K_RIGHTBRACKET:
                        a2press,a2music = keyPlay("a".upper()+f"{pitch + 5}",angle)
                    if event.key == pygame.K_BACKSLASH:
                        b2press,b2music = keyPlay("b".upper()+f"{pitch + 5}",angle)
                    if event.key == pygame.K_z:
                        c3press,c3music = keyPlay("c".upper()+f"{pitch + 6}",angle)
                    if event.key == pygame.K_x:
                        d3press,d3music = keyPlay("d".upper()+f"{pitch + 6}",angle)
                    if event.key == pygame.K_c:
                        e3press,e3music = keyPlay("e".upper()+f"{pitch + 6}",angle)
                    if event.key == pygame.K_v:
                        f3press,f3music = keyPlay("f".upper()+f"{pitch + 6}",angle)
                    if event.key == pygame.K_b:
                        g3press,g3music = keyPlay("g".upper()+f"{pitch + 6}",angle)
                    if event.key == pygame.K_n:
                        a3press,a3music = keyPlay("a".upper()+f"{pitch + 6}",angle)
                    if event.key == pygame.K_m:
                        b3press,b3music = keyPlay("b".upper()+f"{pitch + 6}",angle) 
                    if event.key == pygame.K_COMMA:
                        lpress = keyPlay("B0",angle)
                
                    if event.key == pygame.K_8:
                        cd2press,cd2music = keyPlayB("cd"+str(pitch + 5),angle)
                    if event.key == pygame.K_9:
                        de2press,de2music = keyPlayB("de"+str(pitch + 5),angle)
                    if event.key == pygame.K_MINUS:
                        fg2press,fg2music = keyPlayB("fg"+str(pitch + 5),angle)
                    if event.key == pygame.K_EQUALS:
                        ga2press,ga2music = keyPlayB("ga"+str(pitch + 5),angle)
                    if event.key == pygame.K_BACKSPACE:
                        ab2press,ab2music = keyPlayB("ab"+str(pitch + 5),angle)
                    if event.key == pygame.K_s:
                        cd3press,cd3music = keyPlayB("cd"+str(pitch + 6),angle)
                    if event.key == pygame.K_d:
                        de3press,de3music = keyPlayB("de"+str(pitch + 6),angle)
                    if event.key == pygame.K_g:
                        fg3press,fg3music = keyPlayB("fg"+str(pitch + 6),angle)
                    if event.key == pygame.K_h:
                        ga3press,ga3music = keyPlayB("ga"+str(pitch + 6),angle)
                    if event.key == pygame.K_j:
                        ab3press,ab3music = keyPlayB("ab"+str(pitch + 6),angle)

            if event.type == pygame.KEYUP :
                if event.key == pygame.K_TAB :
                    print(cmusic)
                    cpress = False

                        
                    cmusic.pause()
                        
                if event.key == pygame.K_q:
                    dpress = False
                    if dmusic != None:
                        dmusic.pause()
                        
                if event.key == pygame.K_w:
                    epress = False
                    if emusic != None:
                        emusic.pause()
                        
                if event.key == pygame.K_e:
                    fpress = False
                    if fmusic != None:
                        fmusic.pause()
                        
                if event.key == pygame.K_r:
                    gpress = False
                    if gmusic != None:
                        gmusic.pause()
                        
                if event.key == pygame.K_t:
                    apress = False
                    if amusic != None:
                        amusic.pause()
                        
                if event.key == pygame.K_y:
                    bpress = False
                    if bmusic != None:
                        bmusic.pause()
                        
                if event.key == pygame.K_1:
                    cdpress = False
                    if cmusic != None:
                        cmusic.pause()
                          

                
                if event.key == pygame.K_2:
                    depress =  False
                    if demusic != None:
                        demusic.pause()
                        
                if event.key == pygame.K_4:
                    fgpress =  False
                    if fgmusic != None:
                        fgmusic.pause()
                        
                if event.key == pygame.K_5:
                    gapress =  False
                    if gamusic != None:
                        gamusic.pause()
                        
                if event.key == pygame.K_6:
                    abpress =  False
                    if abmusic != None:
                        abmusic.pause()
                        
                if event.key == pygame.K_8:
                    cd2press = False
                    if cd2music != None:
                        cd2music.pause()
                        
                if event.key == pygame.K_9:
                    de2press = False
                    if de2music != None:
                        de2music.pause()
                        
                if event.key == pygame.K_MINUS:
                    fg2press = False
                    if fg2music != None:
                        fg2music.pause()
                        
                if event.key == pygame.K_EQUALS:
                    ga2press = False
                    if ga2music != None:
                        ga2music.pause()
                        
                if event.key == pygame.K_BACKSPACE:
                    ab2press = False
                    if ab2music != None:
                        ab2music.pause()
                         


                if pitch !=3:
                    if event.key == pygame.K_u:
                        c2press = False
                        if c2music != None:
                            c2music.pause()
                            
                    if event.key == pygame.K_i:
                        d2press = False
                        if d2music != None:
                            d2music.pause()
                            
                    if event.key == pygame.K_o:
                        e2press = False
                        if e2music != None:
                            e2music.pause()
                            
                    if event.key == pygame.K_p:
                        f2press = False
                        if f2music != None:
                            f2music.pause()
                            
                    if event.key == pygame.K_LEFTBRACKET:
                        g2press = False
                        if g2music != None:
                            g2music.pause()
                            
                    if event.key == pygame.K_RIGHTBRACKET:
                        a2press = False
                        if a2music != None:
                            a2music.pause()
                            
                    if event.key == pygame.K_BACKSLASH:
                        b2press = False
                        if b2music != None:
                            b2music.pause()
                              
                    if event.key == pygame.K_z:
                        c3press = False
                        if c3music != None:
                            c3music.pause()
                            
                    if event.key == pygame.K_x:
                        d3press = False
                        if d3music != None:
                            d3music.pause()
                            
                    if event.key == pygame.K_c:
                        e3press = False
                        if e3music != None:
                            e3music.pause()
                            
                    if event.key == pygame.K_v:
                        f3press = False
                        if f3music != None:
                            f3music.pause()
                            
                    if event.key == pygame.K_b:
                        g3press = False
                        if g3music != None:
                            g3music.pause()
                                   
                    if event.key == pygame.K_n:
                        a3press = False
                        if a3music!=None:
                            a3music.pause()
                            
                    if event.key == pygame.K_m:
                        b3press = False
                        if b3music!=None:
                            b3music.pause()
                            
                    if event.key == pygame.K_COMMA:
                        lpress = False  

                    if event.key == pygame.K_s:
                        cd3press = False
                        if cd3music!=None:
                            cd3music.pause()
                            
                    if event.key == pygame.K_d:
                        de3press = False
                        if de3music!=None:
                            de3music.pause()
                            
                    if event.key == pygame.K_g:
                        fg3press = False
                        if fg3music!=None:
                            fg3music.pause()
                            
                    if event.key == pygame.K_h:
                        ga3press = False
                        if ga3music!=None:
                            ga3music.pause()
                            
                    if event.key == pygame.K_j:
                        ab3press = False
                        if ab3music!=None:
                            ab3music.pause()
                            


        keyPress(screen,width,height,keyc,cpress)
        keyPress(screen,width,height,keyd,dpress)
        keyPress(screen,width,height,keye,epress)
        keyPress(screen,width,height,keyf,fpress)
        keyPress(screen,width,height,keyg,gpress)
        keyPress(screen,width,height,keya,apress)
        keyPress(screen,width,height,keyb,bpress)
        keyPress(screen,width,height,keyc2,c2press)
        keyPress(screen,width,height,keye2,e2press)
        keyPress(screen,width,height,keyd2,d2press)
        keyPress(screen,width,height,keyf2,f2press)
        keyPress(screen,width,height,keyg2,g2press)
        keyPress(screen,width,height,keya2,a2press)
        keyPress(screen,width,height,keyb2,b2press)
        keyPress(screen,width,height,keyc3,c3press)
        keyPress(screen,width,height,keyd3,d3press)
        keyPress(screen,width,height,keye3,e3press)
        keyPress(screen,width,height,keyf3,f3press)
        keyPress(screen,width,height,keyg3,g3press)
        keyPress(screen,width,height,keya3,a3press)
        keyPress(screen,width,height,keyb3,b3press)
        keyPress(screen,width,height,keyl,lpress)
        keyPressB(screen,width,height,keycd,cdpress)
        keyPressB(screen,width,height,keyde,depress)
        keyPressB(screen,width,height,keyfg,fgpress)
        keyPressB(screen,width,height,keyga,gapress)
        keyPressB(screen,width,height,keyab,abpress)
        keyPressB(screen,width,height,keycd2,cd2press)
        keyPressB(screen,width,height,keyde2,de2press)
        keyPressB(screen,width,height,keyfg2,fg2press)
        keyPressB(screen,width,height,keyga2,ga2press)
        keyPressB(screen,width,height,keyab2,ab2press)
        keyPressB(screen,width,height,keycd3,cd3press)
        keyPressB(screen,width,height,keyde3,de3press)
        keyPressB(screen,width,height,keyfg3,fg3press)
        keyPressB(screen,width,height,keyga3,ga3press)
        keyPressB(screen,width,height,keyab3,ab3press)
        
        

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
            screen.blit(ONOFF,(277,277))
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
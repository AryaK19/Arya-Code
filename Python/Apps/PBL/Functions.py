import pygame
pygame.init()
# from main_copy import*

def pitchButton(event,spin):
    
    pos = pygame.mouse.get_pos()
    if pos[0] > 58 and pos[1] > 511 and pos[0] < 85 and pos[1] < 606:
        if event.y == 1 and spin != 2:
            spin+=event.y
        if event.y == -1 and spin != 0:
            spin+=event.y
       
    return spin
        
def keyPlay(key,angle):
    music = pygame.mixer.Sound(f"Audio\keys\{key}.wav").play()
    music.set_volume(-(angle - 150)/300)
    
    press = True
    return press
    
def keyPlayB(key,angle):
    key = str(key)
    
    if len(key) == 2:
        music = pygame.mixer.Sound(f"Audio\keys\{key[1].upper()}b1.wav").play()
    else:
        music = pygame.mixer.Sound(f"Audio\keys\{key[1].upper()}b{key[2]}.wav").play()

    music.set_volume(-(angle - 150)/300)
    
    press = True
    return press


def keyPress(screen,width,height,key,booli):
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


def keypress(screen,width,height,keyImages,keyPresses): 
    keyPress(screen,width,height,keyImages["keyc"],keyPresses["cpress"])
    keyPress(screen,width,height,keyImages["keyd"],keyPresses["dpress"])
    keyPress(screen,width,height,keyImages["keye"],keyPresses["epress"])
    keyPress(screen,width,height,keyImages["keyf"],keyPresses["fpress"])
    keyPress(screen,width,height,keyImages["keyg"],keyPresses["gpress"])
    keyPress(screen,width,height,keyImages["keya"],keyPresses["apress"])
    keyPress(screen,width,height,keyImages["keyb"],keyPresses["bpress"])
    keyPress(screen,width,height,keyImages["keyc2"],keyPresses["c2press"])
    keyPress(screen,width,height,keyImages["keye2"],keyPresses["e2press"])
    keyPress(screen,width,height,keyImages["keyd2"],keyPresses["d2press"])
    keyPress(screen,width,height,keyImages["keyf2"],keyPresses["f2press"])
    keyPress(screen,width,height,keyImages["keyg2"],keyPresses["g2press"])
    keyPress(screen,width,height,keyImages["keya2"],keyPresses["a2press"])
    keyPress(screen,width,height,keyImages["keyb2"],keyPresses["b2press"])
    keyPress(screen,width,height,keyImages["keyc3"],keyPresses["c3press"])
    keyPress(screen,width,height,keyImages["keyd3"],keyPresses["d3press"])
    keyPress(screen,width,height,keyImages["keye3"],keyPresses["e3press"])
    keyPress(screen,width,height,keyImages["keyf3"],keyPresses["f3press"])
    keyPress(screen,width,height,keyImages["keyg3"],keyPresses["g3press"])
    keyPress(screen,width,height,keyImages["keya3"],keyPresses["a3press"])
    keyPress(screen,width,height,keyImages["keyb3"],keyPresses["b3press"])
    keyPress(screen,width,height,keyImages["keycd"],keyPresses["cdpress"])
    keyPress(screen,width,height,keyImages["keyde"],keyPresses["depress"])
    keyPress(screen,width,height,keyImages["keyfg"],keyPresses["fgpress"])
    keyPress(screen,width,height,keyImages["keyga"],keyPresses["gapress"])
    keyPress(screen,width,height,keyImages["keyab"],keyPresses["abpress"])
    keyPress(screen,width,height,keyImages["keycd2"],keyPresses["cd2press"])
    keyPress(screen,width,height,keyImages["keyde2"],keyPresses["de2press"])
    keyPress(screen,width,height,keyImages["keyfg2"],keyPresses["fg2press"])
    keyPress(screen,width,height,keyImages["keyga2"],keyPresses["ga2press"])
    keyPress(screen,width,height,keyImages["keyab2"],keyPresses["ab2press"])
    keyPress(screen,width,height,keyImages["keycd3"],keyPresses["cd3press"])
    keyPress(screen,width,height,keyImages["keyde3"],keyPresses["de3press"])
    keyPress(screen,width,height,keyImages["keyfg3"],keyPresses["fg3press"])
    keyPress(screen,width,height,keyImages["keyga3"],keyPresses["ga3press"])
    keyPress(screen,width,height,keyImages["keyab3"],keyPresses["ab3press"])
    keyPress(screen,width,height,keyImages["keyl"],keyPresses["lpress"])




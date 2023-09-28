import pygame
pygame.init()


def vRotate(volumeButton0,angle):
    for i in range(-150,151,30):
        if i == angle:
            volumeButton = pygame.transform.rotate(volumeButton0,i)
    return volumeButton

def loadSounds():
    sounds = {}

    for i in ["A","B",'C','D','E','F','G']:
        for j in range(1,8):
            sounds.update({f"{i}{j}" : pygame.mixer.Sound(f"Audio\keys\{i}{j}.wav")})

    for i in ["Ab","Bb",'Db','Eb','Gb']:
        for j in range(1,8):
            sounds.update({f"{i}{j}" : pygame.mixer.Sound(f"Audio\keys\{i}{j}.wav")})
    return sounds
    
def keysImage(key):
    key = pygame.image.load(f"Images\keysPress\key{key}.png").convert_alpha()
    return key

def keysImageB(key):
    key = pygame.image.load(f"Images\keysPress\{key}.png").convert_alpha()
    return key


# def keyPlay(key,angle):
#     from LoadingScreen import sounds
#     music = sounds[f"{key}"].play()
#     music.set_volume(-(angle - 150)/300)
#     return True
# def keyPlayB(key,angle):
#     from LoadingScreen import sounds
    
#     music = sounds[f"{key[0]}b{key[1]}"].play()
#     music.set_volume(-(angle - 150)/300)
#     return True

def keyPlay(key,angle):
    from LoadingScreen import sounds
    music = sounds[f"{key}"].play()
    music.set_volume(-(angle - 150)/300)
    return True,music
def keyPlayB(key,angle):
    from LoadingScreen import sounds
    
    music = sounds[f"{key[0]}b{key[1]}"].play()
    music.set_volume(-(angle - 150)/300)
    return True,music

def pitchButton(event,pitch):
    
    if event.type == pygame.MOUSEWHEEL:
        pos = pygame.mouse.get_pos()
        
        if pos[0] > 58 and pos[1] > 511 and pos[0] < 85 and pos[1] < 606:
            if event.y == 1 and pitch != 4:
                pitch+=1
            elif event.y == -1 and pitch != 0:
                pitch-=1
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and pitch !=4:
            pitch+=1
        elif event.key == pygame.K_DOWN and pitch !=0:
            pitch-=1

        
    return pitch


def keysLoad(key):
    key = pygame.image.load(f"Images\Loading animation\\{key}.png").convert_alpha()
    return key

def keysBlitLoad(screen,width,height,key):
    screen.blit(key,(0,70,width,height))

def beatPress(event,beat_bool,beat_sound):
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        if pos[0] > 611 and pos[1] > 326 and pos[0] < 631 and pos[1] < 348 and event.button ==1:
            beat_bool["beat1"] = not beat_bool["beat1"]
        if pos[0] > 655 and pos[1] > 329 and pos[0] < 676 and pos[1] < 348 and event.button ==1:
            beat_bool["beat2"] = not beat_bool["beat2"]
        if pos[0] > 695 and pos[1] > 326 and pos[0] < 716 and pos[1] < 348 and event.button ==1:
            beat_bool["beat3"] = not beat_bool["beat3"]
        if pos[0] > 740 and pos[1] > 326 and pos[0] < 759 and pos[1] < 348 and event.button ==1:
            beat_bool["beat4"] = not beat_bool["beat4"]
        if pos[0] > 788 and pos[1] > 326 and pos[0] < 808 and pos[1] < 348 and event.button ==1:
            beat_bool["beat5"] = not beat_bool["beat5"]
        if pos[0] > 829 and pos[1] > 326 and pos[0] < 849 and pos[1] < 348 and event.button ==1:
            beat_bool["beat6"] = not beat_bool["beat6"]
        
        for i in range(1,7):
            
            if beat_bool[f"beat{i}"]:
               
                
                beat_sound[f"beat{i}"].play()
        for i in range(1,7):
            
            if not beat_bool[f"beat{i}"]:
           
                beat_sound[f"beat{i}"].stop()

        return beat_bool
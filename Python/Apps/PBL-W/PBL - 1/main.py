import pygame
from event import events
from LoadingScreen import loadingScreen
from function import keysImage,keysImageB,keyPlay,keyPlayB, pitchButton,beatPress,vRotate

start = False
pygame.init()
pygame.mixer.set_num_channels(80)

def main():
    width, height = 1370,710
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption("PyPiano") 
    pygame.display.set_icon(pygame.image.load("Images\Synth.jpg").convert_alpha()) 

    run = True 
    angle = 0 
    fps = 120
    pitch = 3
    clock = pygame.time.Clock()
    ON = True
    showLetters = False

    image = pygame.image.load("Images\Synth.png").convert_alpha()
    ONOFF = pygame.image.load("Images\ONOFF.png").convert_alpha()
    lightOFF = pygame.image.load("Images\lightOFF.png").convert_alpha()
    pitchButton0 = pygame.image.load("Images\pitchButton0.png").convert_alpha()
    pitchButton1 = pygame.image.load("Images\pitchButton1.png").convert_alpha()
    pitchButton2 = pygame.image.load("Images\pitchButton2.png").convert_alpha()
    pitchButton3 = pygame.image.load("Images\pitchButton3.png").convert_alpha()
    pitchButton4 = pygame.image.load("Images\pitchButton4.png").convert_alpha()
    volumeButton0 = pygame.image.load("Images\\volume.png").convert_alpha()
    Letters = pygame.image.load("Images\Letters.png").convert_alpha()
    LettersB = pygame.image.load("Images\LettersB.png").convert_alpha()

    keynamesW = ["c","d","e","f","g","a","b"]
    keynamesB = ["cd","de","fg","ga","ab"]
    
    beats_img = {}
    for i in range(1,7):
        beats_img.update({f"beat{i}": pygame.image.load(f"Images\BeatON{i}.png")})

    beats_sound = {}
    for i in range(1,7):
        beats_sound.update({f"beat{i}": pygame.mixer.Sound(f"Audio\Beats\\beat{i}.mpeg")})

    beats_bool = {}
    for i in range(1,7):
        beats_bool.update({f"beat{i}":False})

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



    while run:
        screen.blit(image,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            # if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            #     print(pygame.mouse.get_pos()) 

            if event.type == pygame.MOUSEBUTTONDOWN :
                pos = pygame.mouse.get_pos()
                if event.button == 1:
                    if pos[0] > 275 and pos[1] > 275 and pos[0] < 294 and pos[1] < 294:
                        ON = not ON
                if pos[0] > 223 and pos[1] > 326 and pos[0] < 245 and pos[1] < 349:
                    if event.button == 1:
                        showLetters = not showLetters

            if event.type == pygame.MOUSEWHEEL:
                pos = pygame.mouse.get_pos()
                if pos[0] > 120 and pos[1] > 103 and pos[0] < 170 and pos[1] < 140:
                    if event.y == 1 and angle != 150:
                        angle+=30
                    if event.y == -1 and angle != -150:
                        angle-=30
            if ON:
                events(event,keyPresses,keyPlay,keyPlayB,pitch,angle)
                beatPress(event,beats_bool,beats_sound)
            
            pitch = pitchButton(event,pitch)

            
        for i in keynamesW:
            for j in range(1,4):
                if j == 1:
                    if keyPresses[i+"press"]:
                        screen.blit(keyImages['key'+i], (0,0))
                else:
                    if keyPresses[i+str(j)+"press"]:
                        screen.blit(keyImages['key'+i+str(j)], (0,0))
        for i in keynamesB:
            for j in range(1,4):
                if j == 1:
                    if keyPresses[i+"press"]:
                        screen.blit(keyImages['key'+i], (0,0))
                else:
                    if keyPresses[i+str(j)+"press"]:
                        screen.blit(keyImages['key'+i+str(j)], (0,0))


        for i in range(0,5):
            if i == pitch:
                screen.blit(eval(f"pitchButton{i}"),(0,0))
        for i in range(1,7):
            
            if beats_bool[f"beat{i}"]:
                screen.blit(beats_img[f"beat{i}"],(0,0))
               
        if ON:
            screen.blit(ONOFF,(277,277))       
        
        volumeButton = vRotate(volumeButton0, angle)
        
        if angle == 90 or angle == -90 or angle == 0:
            screen.blit(volumeButton,(120,103))
        else:
            screen.blit(volumeButton,(112,96))

        screen.blit(ONOFF,(223,277))

        if showLetters:
            screen.blit(LettersB,(0,0))
            screen.blit(Letters,(0,-5)) 
        else:
            screen.blit(lightOFF,(224,328))  

        clock.tick((fps))
        pygame.display.update()
    pygame.quit()
    quit()
    
start = loadingScreen()
if start:
    main()
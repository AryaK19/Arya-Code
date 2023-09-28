import pygame

pygame.init()
keynamesW = ["c","d","e","f","g","a","b"]
keynamesB = ["cd","de","fg","ga","ab"]

whiteKeys = {"TAB":"c" , "q":"d" , "w":"e" , "e":"f" ,"r":"g" , "t":"a" , "y":"b" , "u":"c2" , "i":"d2" , "o":"e2" , "p":"f2" ,"LEFTBRACKET":"g2" , "RIGHTBRACKET":"a2" , "BACKSLASH":"b2" , "z":"c3" , "x":"d3" , "c":"e3" ,"v":"f3" , "b":"g3" , "n":"a3" ,"m":"b3" }

blackKeys = {"1":"cd" , "2":"de" , "4":"fg" ,"5":"ga" , "6":"ab" , "8":"cd2" ,"9":"de2" , "MINUS":"fg2" , "EQUALS":"ga2" ,"BACKSPACE":"ab2" , "s":"cd3" , "d":"de3" ,"g":"fg3" , "h":"ga3" , "j":"ab3"}

def events(event,keyPresses,keyPlay,keyPlayB,pitch,angle):

    if event.type == pygame.KEYDOWN: 
        for i in whiteKeys :
            if event.key == eval(f"pygame.K_{i}"):
                if whiteKeys[i] in keynamesW:
                    keyPresses[f"{whiteKeys[i]}press"],music = keyPlay(whiteKeys[i].upper()+str(pitch+1),angle)
                else:
                    
                    keyPresses[f"{whiteKeys[i]}press"],music = keyPlay(whiteKeys[i][0].upper()+str(int(whiteKeys[i][1])+pitch),angle)

        for i in blackKeys :
            if event.key == eval(f"pygame.K_{i}"):
                if blackKeys[i] in keynamesB:
                    keyPresses[f"{blackKeys[i]}press"],music = keyPlayB(blackKeys[i][1].upper()+str(pitch+1),angle)
                else:
                    keyPresses[f"{blackKeys[i]}press"],music = keyPlayB(blackKeys[i][1].upper()+str(int(blackKeys[i][2])+pitch),angle)

    # try:

        
    if event.type == pygame.KEYUP: 
        for i in whiteKeys :
            if event.key == eval(f"pygame.K_{i}"):
                keyPresses[f"{whiteKeys[i]}press"] = False
                try:
                    music.pause()
                    print("Hi")
                except:
                    pass
        for i in blackKeys :
            if event.key == eval(f"pygame.K_{i}"):
                keyPresses[f"{blackKeys[i]}press"] = False
                try:
                    music.pause()
                    print("Hi")
                except:
                    pass
                

    



        

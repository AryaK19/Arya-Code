import pygame
from Functions import keyPlay,keyPlayB
pygame.init()

def events(event,keyPresses,pitch,angle):
    if event.type == pygame.KEYDOWN:   
                       
        if event.key == pygame.K_TAB :  
            keyPresses["cpress"] = keyPlay("c".upper()+f"{pitch + 4}",angle)
        if event.key == pygame.K_q:
            keyPresses["dpress"] = keyPlay("d".upper()+f"{pitch + 4}",angle)
        if event.key == pygame.K_w:
            keyPresses["epress"] = keyPlay("e".upper()+f"{pitch + 4}",angle)
        if event.key == pygame.K_e:
            keyPresses["fpress"] = keyPlay("f".upper()+f"{pitch + 4}",angle)
        if event.key == pygame.K_r:
            keyPresses["gpress"] = keyPlay("g".upper()+f"{pitch + 4}",angle)
        if event.key == pygame.K_t:
            keyPresses["apress"] = keyPlay("a".upper()+f"{pitch + 4}",angle)
        if event.key == pygame.K_y:
            keyPresses["bpress"] = keyPlay("b".upper()+f"{pitch + 4}",angle)

        if event.key == pygame.K_1:
            keyPresses["cdpress"] = keyPlayB("cd"+str(pitch + 4),angle)
        if event.key == pygame.K_2:
            keyPresses["depress"] = keyPlayB("de"+str(pitch + 4),angle)
        if event.key == pygame.K_4:
            keyPresses["fgpress"] = keyPlayB("fg"+str(pitch + 4),angle)
        if event.key == pygame.K_5:
            keyPresses["gapress"] = keyPlayB("ga"+str(pitch + 4),angle)
        if event.key == pygame.K_6:
            keyPresses["abpress"] = keyPlayB("ab"+str(pitch + 4),angle)
                
        if pitch !=3:
                        

            if event.key == pygame.K_u:
                keyPresses["c2press"] = keyPlay("c".upper()+f"{pitch + 5}",angle)
            if event.key == pygame.K_i:
                keyPresses["d2press"] = keyPlay("d".upper()+f"{pitch + 5}",angle)
            if event.key == pygame.K_o:
                keyPresses["e2press"] = keyPlay("e".upper()+f"{pitch + 5}",angle)
            if event.key == pygame.K_p:
                keyPresses["f2press"] = keyPlay("f".upper()+f"{pitch + 5}",angle)
            if event.key == pygame.K_LEFTBRACKET:
                keyPresses["g2press"] = keyPlay("g".upper()+f"{pitch + 5}",angle)
            if event.key == pygame.K_RIGHTBRACKET:
                keyPresses["a2press"] = keyPlay("a".upper()+f"{pitch + 5}",angle)
            if event.key == pygame.K_BACKSLASH:
                keyPresses["b2press"] = keyPlay("b".upper()+f"{pitch + 5}",angle)
            if event.key == pygame.K_z:
                keyPresses["c3press"] = keyPlay("c".upper()+f"{pitch + 6}",angle)
            if event.key == pygame.K_x:
                keyPresses["d3press"] = keyPlay("d".upper()+f"{pitch + 6}",angle)
            if event.key == pygame.K_c:
                keyPresses["e3press"] = keyPlay("e".upper()+f"{pitch + 6}",angle)
            if event.key == pygame.K_v:
                keyPresses["f3press"] = keyPlay("f".upper()+f"{pitch + 6}",angle)
            if event.key == pygame.K_b:
                keyPresses["g3press"] = keyPlay("g".upper()+f"{pitch + 6}",angle)
            if event.key == pygame.K_n:
                keyPresses["a3press"] = keyPlay("a".upper()+f"{pitch + 6}",angle)
            if event.key == pygame.K_m:
                keyPresses["b3press"] = keyPlay("b".upper()+f"{pitch + 6}",angle)
            if event.key == pygame.K_COMMA:
                keyPresses["lpress"] = keyPlay("B0",angle)


                    
            if event.key == pygame.K_8:
                keyPresses["cd2press"] = keyPlayB("cd"+str(pitch + 5),angle)
            if event.key == pygame.K_9:
                keyPresses["de2press"] = keyPlayB("de"+str(pitch + 5),angle)
            if event.key == pygame.K_MINUS:
                keyPresses["fg2press"] = keyPlayB("fg"+str(pitch + 5),angle)
            if event.key == pygame.K_EQUALS:
                keyPresses["ga2press"] = keyPlayB("ga"+str(pitch + 5),angle)
            if event.key == pygame.K_BACKSPACE:
                keyPresses["ab2press"] = keyPlayB("ab"+str(pitch + 5),angle)
            if event.key == pygame.K_s:
                keyPresses["cd3press"] = keyPlayB("cd"+str(pitch + 6),angle)
            if event.key == pygame.K_d:
                keyPresses["de3press"] = keyPlayB("de"+str(pitch + 6),angle)
            if event.key == pygame.K_g:
                keyPresses["fg3press"] = keyPlayB("fg"+str(pitch + 6),angle)
            if event.key == pygame.K_h:
                keyPresses["ga3press"] = keyPlayB("ga"+str(pitch + 6),angle)
            if event.key == pygame.K_j:
                keyPresses["ab3press"] = keyPlayB("ab"+str(pitch + 6),angle)

    if event.type == pygame.KEYUP :

        if event.key == pygame.K_TAB:
            keyPresses["cpress"] = False
        if event.key == pygame.K_q:
            keyPresses["dpress"] = False
        if event.key == pygame.K_w:
            keyPresses["epress"] = False
        if event.key == pygame.K_e:
            keyPresses["fpress"] = False
        if event.key == pygame.K_r:
            keyPresses["gpress"] = False
        if event.key == pygame.K_t:
            keyPresses["apress"] = False
        if event.key == pygame.K_y:
            keyPresses["bpress"] = False

                    
        if event.key == pygame.K_1:
            keyPresses["cdpress"] = False  
        if event.key == pygame.K_2:
            keyPresses["depress"] =  False
        if event.key == pygame.K_4:
            keyPresses["fgpress"] =  False
        if event.key == pygame.K_5:
            keyPresses["gapress"] =  False
        if event.key == pygame.K_6:
            keyPresses["abpress"] =  False


        if pitch !=3:
                        

            if event.key == pygame.K_u:
                keyPresses["c2press"] = False
            if event.key == pygame.K_i:
                keyPresses["d2press"] = False
            if event.key == pygame.K_o:
                keyPresses["e2press"] = False
            if event.key == pygame.K_p:
                keyPresses["f2press"] = False
            if event.key == pygame.K_LEFTBRACKET:
                keyPresses["g2press"] = False
            if event.key == pygame.K_RIGHTBRACKET:
                keyPresses["a2press"] = False
            if event.key == pygame.K_BACKSLASH:
                keyPresses["b2press"] = False      


            if event.key == pygame.K_z:
                keyPresses["c3press"] = False       
            if event.key == pygame.K_x:
                keyPresses["d3press"] = False       
            if event.key == pygame.K_c:
                keyPresses["e3press"] = False       
            if event.key == pygame.K_v:
                keyPresses["f3press"] = False       
            if event.key == pygame.K_b:
                keyPresses["g3press"] = False       
            if event.key == pygame.K_n:
                keyPresses["a3press"] = False       
            if event.key == pygame.K_m:
                keyPresses["b3press"] = False       
            if event.key == pygame.K_COMMA:
                keyPresses["lpress"] = False  



            if event.key == pygame.K_8:
                keyPresses["cd2press"] = False
            if event.key == pygame.K_9:
                keyPresses["de2press"] = False
            if event.key == pygame.K_MINUS:
                keyPresses["fg2press"] = False
            if event.key == pygame.K_EQUALS:
                keyPresses["ga2press"] = False
            if event.key == pygame.K_BACKSPACE:
                keyPresses["ab2press"] = False 

            if event.key == pygame.K_s:
                keyPresses["cd3press"] = False
            if event.key == pygame.K_d:
                keyPresses["de3press"] = False
            if event.key == pygame.K_g:
                keyPresses["fg3press"] = False
            if event.key == pygame.K_h:
                keyPresses["ga3press"] = False
            if event.key == pygame.K_j:
                keyPresses["ab3press"] = False
import pygame
import random
import math


pygame.init()

width, height = 900,600

screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("TriBounce")


def triangle(trix, triy, triw):
    pygame.draw.polygon(screen, 'green', points=[(trix - triw/2, triy - triw*math.sin(60*3.14/180)), (trix + triw/2, triy - triw*math.sin(3.14/3)), (trix, triy)])

def enemy(trix, triy , triw):
    pygame.draw.polygon(screen, 'red', points=[(trix - triw/2, triy - triw*math.sin(60*3.14/180)), (trix + triw/2, triy - triw*math.sin(60*3.14/180)), (trix, triy)])
   

def rect(x,y,width,height,color):
    pygame.draw.rect(screen,color,[x,y,width,height])

def text_screen(text,colour,x,y,font):
    screen_text = font.render(text,True,colour)
    screen.blit(screen_text,[x,y])


def main():
    run = True 
    gameOver = False

    time = 0
    score = 0
    jump = False
    clock = pygame.time.Clock()
    rectw = 100
    triw = 60
    trix ,triy = width/2,height - rectw
    triMoveL = False
    triMoveR = False
    trivel = -10.6
    trivele = -9.6
    acc = 0.2
    vel = trivel
    kills = 0
    
    triwe = 78
    trive = 2
    jumpe = False
    enemystats = []
    
    xtv = 4
    fps = 120
    limit = 10
    time_of_spawn = 1
    speed_up = 0.002

    while run:

        if not gameOver:
            if not jump:    
                if triy > height - rectw:
                    triy =  height - rectw

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_w or event.key == pygame.K_UP ) and triy - 100 <= height - rectw <= triy + 3:
                        jump = True
                        pygame.mixer.Sound('wing.wav').play()
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        triMoveL = True
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        triMoveR = True
  
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT: 
                        triMoveL = False
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        triMoveR = False   


            if triwe/2 + 3 > trix:
                triMoveL = False          
            elif width - (triwe/2 + 3) < trix:
                triMoveR = False   

            if triMoveL :
                trix = trix - xtv
            if triMoveR :
                trix = trix + xtv


            if score >  0 and len(enemystats) < limit and ((time%(fps*time_of_spawn))) == 0:
                    ran = random.randint(0,1)
                   
                    if ran == 0:
                        enemystats.append([width+ triw/2,1,ran])
                    else:
                        enemystats.append([-triw/2,1,ran])

            screen.fill("black")
            triangle(trix,triy,triw)
            rect(0,height - rectw ,width ,rectw,'grey')
            text_screen(f"Score : {score}",'white',10,10,pygame.font.SysFont(None,35))
            text_screen(f"Kills : {kills}",'white',width-150,10,pygame.font.SysFont(None,35))
                  
        
            for e in enemystats:

                if (e[0]- triwe/2 - 10 <= trix <= e[0]+triwe/2 + 10) and height - (rectw + triwe*math.sin(60*3.14/180)) - 3 <= triy <= height - (rectw + triwe*math.sin(60*3.14/180)) + 3 :
                    e[1] = 0
                    jumpe = True 
                    trivele = vel 
                    kills +=1
               

                if (e[0]- triwe/2 <= trix <= e[0]+triwe/2) and (height - rectw - triwe/2 <= triy <= height - rectw + triwe/2):
                    pygame.mixer.Sound('die.wav').play()
                    gameOver = True
                
                if e[0] <= 0 + triwe/2:
                    e[2] = 1 
                elif e[0] >= width - triwe/2:
                    e[2] = 0 
                if e[2] == 1:
                    e[0] += trive
                elif e[2] == 0:
                    e[0] -= trive
            
                if e[1] == 1:
                    enemy(e[0], height - rectw , triwe)

                if e[1] == 0:
                   
                    enemystats.remove(e)
                    pygame.mixer.Sound('hit.wav').play()
                    

            if jump:
                trivel += acc      
                if trivel >= -vel:
                    trivel = vel  
                    jump = False       
                triy = triy + trivel

            if jumpe: 
                trivele += acc
                triy = triy + trivele
                if triy >= height - rectw:
                    jumpe = False
                    trivele = vel
                
            
            clock.tick(fps)
            pygame.display.update()

            time += 1
            if time%fps == 0:
                score += 1
            
            trive+=speed_up

        else:
            s = pygame.Surface((width,height))  
            s.set_alpha(2.5)                
            s.fill((180,180,180))           
            screen.blit(s, (150,0))

            s = pygame.Surface((width,height))  
            s.set_alpha(2.5)                
            s.fill((180,180,180))           
            screen.blit(s, (0,50))
            rect(200,200,500,200,"black")
            text_screen("Press Space To Play Again",'white',width/2 - 170,height/2 + 10,pygame.font.SysFont(None,35))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    main()
                if event.type == pygame.QUIT:
                    run = False
                    break
            pygame.display.update()




    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
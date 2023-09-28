import pygame
import numpy as np 
import random as rn
pygame.init()


class Tribounce():

    def __init__(self,render=False) -> None:
        pygame.init()
        self.width,self.height = 1000,700
        self.render = render
        if self.render:
            self.screen = pygame.display.set_mode([self.width,self.height])
            pygame.display.set_caption("TriBounce")


        self.width,self.height = 1000,700
        self.moveRight= False 
        self.moveLeft = False 

        self.jump = False
        self.jumpe = False
        self.goingUp = True
        self.goingUpSpeed = 11.0
        self.gravitationalAccelartion = 0.2
        
        self.playerSpeed = 6

        self.clock = pygame.time.Clock()

        self.playerPos = [self.width/2,self.height-200]
        self.playerHeight = 60
        
        self.enemyStats = []
        
        self.enemySpeed = 8
        self.ran = 0
        self.kills = 0

        self.fps = 240
        self.fpsCount = 0
        self.time = 0  
    
        self.reward = 0

        self.done = False
        self.state=np.array([self.playerPos,[0,0],[0,0]])

    def run(self,action):

        self.done = False
        if self.render:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True


  
        if action == 2 and self.height-205<self.playerPos[1]<self.height-195:
            self.jump = True
            self.reward -=2
        if action == 0:
            self.moveRight = True 
        if action == 1:
            self.moveLeft = True
    
        if action != 2 and self.height-202<self.playerPos[1]<self.height-198:
            self.jump = False
        if action != 0:
            self.moveRight = False 
        if action != 1:
            self.moveLeft = False

        if self.jump and round(self.goingUpSpeed,1) > -11.0 + self.gravitationalAccelartion:
            self.goingUpSpeed -=self.gravitationalAccelartion
        elif self.jump :
            self.jump = False
            self.jumpe = False
            self.goingUpSpeed = 11.0
            self.playerPos[1] = self.height-200
        

        if self.jump:
            self.playerPos[1]-=self.goingUpSpeed

        if self.jumpe and round(self.goingUpSpeed,1) > -11.6 + self.gravitationalAccelartion:
            self.goingUpSpeed -=self.gravitationalAccelartion
            self.jump = False
        elif self.jumpe :
            self.jumpe = False
            
            self.goingUpSpeed = 11.0
            self.playerPos[1] = self.height-200

        if self.jumpe:
            self.playerPos[1]-=self.goingUpSpeed

        if self.moveRight:
            self.playerPos[0] +=self.playerSpeed
        if self.moveLeft:
            self.playerPos[0] -=self.playerSpeed

        if self.playerPos[0]> self.width - self.playerHeight/2:
            self.playerPos[0] = self.width-self.playerHeight/2
        elif self.playerPos[0]< self.playerHeight/2:
            self.playerPos[0] = self.playerHeight/2

        
        if self.time > 2 and self.fpsCount%(1.7*self.fps)== 0 and len(self.enemyStats)<4:
            if self.ran == 0:
                self.ran = 1

            elif self.ran == 1:
                self.ran = 0

            if self.ran == 0:
                self.enemyStats.append([[self.width-40,self.height-200],1,self.ran])
            else:
                self.enemyStats.append([[40,self.height-200],1,self.ran])
            

        for e in self.enemyStats:
                    # print(playerPos,[e[0][0],e[0][1]-40], goingUpSpeed<0)

            if (e[0][0]-5 - 40<=self.playerPos[0]<=e[0][0]+5+40) and (e[0][1]  - 1 - 80<= self.playerPos[1] <= e[0][1] + 1 - 80) and self.goingUpSpeed<0 :
                e[1] = 0
              
                self.jumpe = True 
                self.goingUpSpeed = 10.0
                self.kills +=1
                self.reward += 20
        

            # if (e[0]- triwe/2 <= trix <= e[0]+triwe/2) and (height - rectw - triwe/2 <= triy <= height - rectw + triwe/2):
            if (e[0][0]-2-40-self.playerHeight/2 <= self.playerPos[0] <= e[0][0]+2+40+self.playerHeight/2) and (self.height-200 - 80 - 2 <= self.playerPos[1]<=self.height-200 + 2)and e[1] == 1 :
                self.done = True
                self.reward -= 30
                
                
                
            else:
                self.done = False   
            
            if e[0][0] <= 40:
                e[2] = 1 
            elif e[0][0] >= self.width - 40:
                e[2] = 0 

            if e[2] == 1:
                e[0][0] += self.enemySpeed
            elif e[2] == 0:
                e[0][0] -= self.enemySpeed

            if e[1] == 0:
                self.enemyStats.remove(e)


   
        if len(self.enemyStats)>3:
            self.state = [self.playerPos,[self.enemyStats[0][0][0],self.enemyStats[1][0][0]],[self.enemyStats[2][0][0],self.enemyStats[3][0][0]]]
        elif len(self.enemyStats)>2:

            self.state = [self.playerPos,[self.enemyStats[0][0][0],self.enemyStats[1][0][0]],[self.enemyStats[2][0][0],0]]
        elif len(self.enemyStats)>1:

            self.state = [self.playerPos,[self.enemyStats[0][0][0],self.enemyStats[1][0][0]],[0,0]]
        elif len(self.enemyStats)>0:

            self.state = [self.playerPos,[self.enemyStats[0][0][0],0],[0,0]]
        elif len(self.enemyStats)==0:

            self.state = [self.playerPos,[0,0],[0,0]]
          




        self.fpsCount +=1
        if self.fpsCount%self.fps == 0:
            if self.time<8:
                self.enemySpeed-=self.time/10
            elif self.time < 12:
                self.enemySpeed+=0.20
            elif self.time>15 :
                self.enemySpeed+=0.30
            self.time+=1
            self.reward+=5

            

        self.clock.tick(self.fps) 


        info = {'playerPos':self.playerPos,'score':self.time,'kills':self.kills}
        
        if self.render:

            def makePlayer(pos,height):
                pygame.draw.polygon(self.screen, 'green', points=[pos, (pos[0]-height/2,pos[1]-height), (pos[0]+height/2,pos[1]-height)])

            def makeEnemy(enemyStats):
                for i in enemyStats:
                    pygame.draw.polygon(self.screen, 'red', points=[i[0], (i[0][0]-80/2,i[0][1]-80), (i[0][0]+80/2,i[0][1]-80)])

            def text_screen(text,colour,x,y,font):
                screen_text = font.render(text,True,colour)
                self.screen.blit(screen_text,[x,y])


            self.screen.fill('black')

            makeEnemy(self.enemyStats)
            makePlayer(self.playerPos,self.playerHeight)
            pygame.draw.rect(self.screen,'grey',[0,self.height-200,self.width,200])       

            text_screen(f"Score : {self.time}",'white',10,10,pygame.font.SysFont(None,35))
            text_screen(f"Kills : {self.kills}",'white',self.width-110,10,pygame.font.SysFont(None,35))        
            
            
            pygame.display.update()
        self.state = np.array(self.state)
            
        return self.state,self.reward,self.done,info

    def close(self):
        pygame.quit()

    def reset(self):
        
        self.done = False
        self.reward = 0
        self.moveRight= False 
        self.moveLeft = False 

        self.jump = False
        self.jumpe = False
        self.goingUp = True
        self.goingUpSpeed = 11.0
        self.gravitationalAccelartion = 0.2
        
        self.playerSpeed = 6

        self.clock = pygame.time.Clock()

        self.playerPos = [self.width/2,self.height-200]
        self.playerHeight = 60
        
        self.enemyStats = []
        
        self.enemySpeed = 8
        self.ran = 0
        self.kills = 0

        self.fps = 120
        self.fpsCount = 0
        self.time = 0  
        self.state=np.array([self.playerPos,[0,0],[0,0]])
        return self.state


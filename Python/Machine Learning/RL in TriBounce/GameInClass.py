import pygame
import numpy as np 
import random as rn



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
        
        self.enemySpeed = 5

        self.kills = 0

        self.fps = 120
        self.fpsCount = 0
        self.time = 0  
    
        self.reward = 0

        self.done = False
    def run(self):
        done = False
        nearEnemy = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and self.height-205<self.playerPos[1]<self.height-195:
                    self.jump = True
                if event.key == pygame.K_d:
                    self.moveRight = True 
                if event.key == pygame.K_a:
                    self.moveLeft = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w and self.height-202<self.playerPos[1]<self.height-198:
                    self.jump = False
                if event.key == pygame.K_d:
                    self.moveRight = False 
                if event.key == pygame.K_a:
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

        
        if self.time > 2 and self.fpsCount%(1.7*self.fps)== 0:
            ran = rn.randint(0,1)
            if ran == 0:
                self.enemyStats.append([[self.width-40,self.height-200],1,ran])
            else:
                self.enemyStats.append([[40,self.height-200],1,ran])

        for e in self.enemyStats:
                    # print(playerPos,[e[0][0],e[0][1]-40], goingUpSpeed<0)

            if (e[0][0]-5 - 40<=self.playerPos[0]<=e[0][0]+5+40) and (e[0][1]  - 1 - 80<= self.playerPos[1] <= e[0][1] + 1 - 80) and self.goingUpSpeed<0 :
                e[1] = 0
                self.jumpe = True 
                self.goingUpSpeed = 10.0
                self.kills +=1
                self.reward += 7
        

            # if (e[0]- triwe/2 <= trix <= e[0]+triwe/2) and (height - rectw - triwe/2 <= triy <= height - rectw + triwe/2):
            elif (e[0][0]-2-40-self.playerHeight/2 <= self.playerPos[0] <= e[0][0]+2+40+self.playerHeight/2) and (self.height-200 - 80 - 2 <= self.playerPos[1]<=self.height-200 + 2) :
                self.done = True
                
                
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


            nearEnemy.append(e[0][0]-self.playerPos[0])
        if len(self.enemyStats)>0:
            nearEnemy.sort()
            nearEnemy = nearEnemy[0]
            state = [self.playerPos,[len(self.enemyStats),nearEnemy]]

        else:

            state=[self.playerPos,[0,0]]


        self.fpsCount +=1
        if self.fpsCount%self.fps == 0:
            self.enemySpeed+=0.1
            self.time+=1
            self.reward +=2

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

        return np.array(state),self.reward,self.done,info

    def close(self):
        pygame.quit()
        quit()

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
        
        self.enemySpeed = 5

        self.kills = 0

        self.fps = 120
        self.fpsCount = 0
        self.time = 0  




# game = Tribounce(render=True)
# done = False

# while not done:
#     state,reward,done,info = game.run()

#     print(state,'\n',reward)

# print(info['kills'],info['score'])

# game.close()

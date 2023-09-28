import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()

font = pygame.font.SysFont("arial", 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple("Point","x, y")

BLOCK_SIZE = 20
fps = 20

class  SnakeGameAI:
    def __init__(self,w=640,h=480):
        self.w = w
        self.h = h
        #init the display
        self.display = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.reset()


    def reset(self):
        #init game states
        self.direction = Direction.RIGHT

        self.head = Point(self.w/2 ,self.h/2)
        self.snake = [self.head,
                    Point(self.head.x-BLOCK_SIZE,self.head.y),
                    Point(self.head.x-(BLOCK_SIZE*2),self.head.y),
                    ]
        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0
            

    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (self.h-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
      
        self.food = Point(x,y)
              

    def play_step(self,action):
        game_over = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # if event.type == pygame.KEYDOWN: 
            #     if event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
            #         self.direction = Direction.LEFT
            #     elif event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
            #         self.direction = Direction.RIGHT
            #     elif event.key == pygame.K_UP and self.direction != Direction.DOWN:
            #         self.direction = Direction.UP
            #     elif event.key == pygame.K_DOWN and self.direction != Direction.UP:
            #         self.direction = Direction.DOWN
            
        self._move(action)
        self.snake.insert(0,self.head)
        reward = 0

        game_over = False

        if self.is_collision() or self.frame_iteration > 100*len(self.snake):
            game_over = True
            reward = -10
            return  game_over,self.score,reward
        if self.food in self.snake:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()

        self._update_UI()
        self.clock.tick(fps)
        return game_over,self.score,reward

    def is_collision(self,pt=None):
        
        if pt is None:
            pt = self.head

        if pt in self.snake[1:]:
            return True

        elif (pt.x) > self.w-BLOCK_SIZE or pt.x < 0 or (pt.y) > self.h-BLOCK_SIZE or pt.y < 0:
            return True 
        else:
            return False

    def _update_UI(self):
        self.display.fill("black")
        for pt in self.snake:
            pygame.draw.rect(self.display,'darkgreen',pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display,'green',pygame.Rect(pt.x+4, pt.y+4, BLOCK_SIZE-8, BLOCK_SIZE-8))
            
        pygame.draw.rect(self.display,"red",pygame.Rect(self.food.x,self.food.y,BLOCK_SIZE,BLOCK_SIZE))
        
        text = font.render(f"SCORE : {self.score}",True,'white')
        self.display.blit(text,(2,5))
        pygame.display.flip()

    def _move(self,action):
        # [straight, right, left]


        clock_wise = [Direction.RIGHT,Direction.DOWN,Direction.LEFT,Direction.UP]

        idx = clock_wise.index(self.direction)


        if np.array_equal(action,[1,0,0]):
            new_dir = clock_wise[idx] 
        elif np.array_equal(action,[0,1,0]):
            next_idx = (idx+1)%4        # does the next trunn in clock wise (that is the right turn)
            new_dir = clock_wise[next_idx] 
        elif np.array_equal(action,[0,0,1]):
            next_idx = (idx-1)%4
            new_dir = clock_wise[next_idx] 

        self.direction = new_dir

        x = self.head.x
        y = self.head.y

        if self.direction == Direction.RIGHT:
            x+=BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x-=BLOCK_SIZE
        elif self.direction == Direction.UP:
            y-=BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y+=BLOCK_SIZE

        self.head = Point(x,y)


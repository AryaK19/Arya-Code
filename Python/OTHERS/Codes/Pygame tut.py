import pygame
import os

WIDTH,HEIGHT= 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("The game")

WHITE = (255, 255, 255)
BLACK = (0,0,0)

YELLOW = (255,255,0)
FPS = 60
VEL = 5
BULLET_VEL = 8
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT +2
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(55,40)),90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(55,40)),270)
AKASHGANGA= pygame.image.load(os.path.join('Assets','space.png'))

BORDER = pygame.Rect(WIDTH//2,0,10,HEIGHT)
red_bullet = []
yellow_bullet =[]

def movement(keys_pressed,yellow):
    
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #LEFT
            yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: #RIGHT
            yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #UP
            yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT: #DOWN
            yellow.y += VEL

def movement2(keys_pressed ,red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: #DOWN
        red.y += VEL

def handle_bullets(yellow_bullet,red_bullet,yellow,red):
    for bullet in yellow_bullet:
        bullet.x += BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullet.remove(bullet)
    for bullet in red_bullet:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullet.remove(bullet)

def draw_window(red,yellow):
    WIN.blit(AKASHGANGA,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))

    for bullet in red_bullet:
        pygame.draw.rect(WIN,YELLOW,bullet)
    for bullet in yellow_bullet:
        pygame.draw.rect(WIN,YELLOW,bullet)
    pygame.display.update()



def main():
    red = pygame.Rect(700,300,55,40)
    yellow = pygame.Rect(100,300,55,40)
    
    clock = pygame.time.Clock()
    MAX_BULLETS = 10

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break 
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullet) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2 - 2,10,5)
                    yellow_bullet.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullet) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x,red.y+red.height//2 - 2,10,5)
                    red_bullet.append(bullet)
        
        print(yellow_bullet,red_bullet)
        keys_pressed =pygame.key.get_pressed()
        movement(keys_pressed,yellow)
        movement2(keys_pressed,red)
        handle_bullets(yellow_bullet,red_bullet,yellow,red)
        
        draw_window(red,yellow)

    pygame.quit()

if __name__=="__main__":
    main()

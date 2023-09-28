import pygame
import os

# NOW, I WILL DEFINE THE PLAYER AND THE CONSTRICTIONS IT WILL HAVE

height, width = (600,900)
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("first game")
color = (100,200,240)
black = (0,0,0)
FPS = 60

S_D_h, S_D_w = 40,40
VEL = 3

border = pygame.Rect(width/2, 0, 10, height) # x,y,hor_width,ver_height

# Go to notepad

YSPACESHIP = pygame.image.load(os.path.join('spaceship_yellow.png'))
RSPACESHIP = pygame.image.load(os.path.join('spaceship_red.png'))
YSPACESHIP_resize = pygame.transform.rotate(pygame.transform.scale(YSPACESHIP, (S_D_h, S_D_w)), 90)
RSPACESHIP_resize = pygame.transform.rotate(pygame.transform.scale(RSPACESHIP, (S_D_h, S_D_w)), 270)


def draw_window(red, yellow):
    window.fill(color)
    pygame.draw.rect(window, black, border) # Black's coordinates are mentioned above, so I am entering a defined variable here
    window.blit(YSPACESHIP_resize, (yellow.x, yellow.y))
    window.blit(RSPACESHIP_resize, (red.x, red.y))
    pygame.display.update()

# MADE A FUNCTION TO DEFINE MOVEMENT OF THE SHIPS
def movement(presskey, yellow, red):
        if presskey[pygame.K_a] and yellow.x - VEL > 0: # LEFT MOVEMENT
            yellow.x -= VEL
        if presskey[pygame.K_d] and yellow.x + VEL + yellow.width < border.x: # RIGHT MOVEMENT
            yellow.x += VEL
        if presskey[pygame.K_w] and yellow.y - VEL > 0 : # UP MOVEMENT
            yellow.y -= VEL
        if presskey[pygame.K_s] and yellow.y + VEL + yellow.height < height: # DOWN MOVEMENT
            yellow.y += VEL

        if presskey[pygame.K_LEFT] and red.x - VEL > border.x:
            red.x -= VEL
        if presskey[pygame.K_RIGHT] and red.x + VEL + red.width < width:
            red.x += VEL
        if presskey[pygame.K_UP] and red.y - VEL > 0:
            red.y -= VEL
        if presskey[pygame.K_DOWN] and red.y + VEL + red.height < height:
            red.y += VEL

def main():
    red = pygame.Rect(850,200, S_D_h,S_D_w) # 200,300 are the XY coordinates and 40,40 is the scale of the ship
    yellow = pygame.Rect(0,100, S_D_h,S_D_w)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        presskey = pygame.key.get_pressed()
        movement(presskey, yellow, red)

        draw_window(red, yellow)

main()
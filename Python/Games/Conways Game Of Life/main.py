import time
import pygame
import numpy as np
pygame.init()

width,height = 900,600
time1 = 0.01

color_bg = (10,10,10)
color_grid = (40,40,40)
color_alive = (225,225,225)
color_die = (170,170,170)

def update(screen,cells,size,with_progress=False): 
    updated_cells = np.zeros((cells.shape[0],cells.shape[1]))

    for row,col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2,col-1:col+2 ]) - cells[row,col]
        color = color_bg if cells[row,col] == 0 else color_alive

        if cells[row,col] == 1:
            if alive < 2 or alive > 3 :
                if with_progress:
                    color = color_die
            elif 2 <= alive <= 3:
                updated_cells[row,col] = 1
                if with_progress:
                    color = color_alive

        else:
            if alive == 3:
                updated_cells[row ,col] = 1
                if with_progress:
                    color = color_alive

  

        pygame.draw.rect(screen,color,(col * size,row * size,(size - 1),(size - 1)))



    return updated_cells

def main():
    size = 15
    screen = pygame.display.set_mode((width,height))

    cells = np.zeros((int((height/size)*2),int((width/size)*2)))
    screen.fill(color_grid)
    update(screen,cells,size)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen,cells,size)
                    pygame.display.update()
            
                elif event.key == pygame.K_RETURN:
                    main()
            
            elif event.type == pygame.MOUSEWHEEL:
                if event.y == -1:
                    size  = size - 5
                if event.y == +1:
                    size  = size + 5
                    
            
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // size,pos[0] // size] = 1
                update(screen,cells,size)
                pygame.display.update()

        screen.fill(color_grid)

        if running :
            
            cells = update(screen,cells,size,with_progress=True)
            pygame.display.update()
     
        
     
        time.sleep(time1)


if __name__ == "__main__":
    main()

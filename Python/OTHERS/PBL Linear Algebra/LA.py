import pygame
import numpy as np
import math


# vertices = np.array([
#     [-1, 1, 1],
#     [1, 1, 1],
#     [1, -1, 1],
#     [-1, -1, 1],
#     [0, 0, 0],
#     [1, 1, -1],
#     [1, -1, -1],
#     [-1, -1, -1]
# ])
vertices = np.array([
    [-1, 1, 1],
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, -1],
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1]
])

def Rx(theta):
    return np.array([
        [1,              0,                 0],
        [0, math.cos(theta), -math.sin(theta)],
        [0, math.sin(theta),  math.cos(theta)]
    ])

def Ry(theta):
    return np.array([
        [math.cos(theta), 0, math.sin(theta)],
        [0,               1,               0],
        [-math.sin(theta), 0,math.cos(theta)]
    ])

def Rz(theta):
    return np.array([
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta), math.cos(theta),  0],
        [0,                             0,  1]
    ])

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("3D Rotation")


def draw_cube(vertices):
   
    for i, j in [(0,1), (1,2), (2,3), (0,3), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]:
    # for i in range(len(vertices)):
    #     for j in range(len(vertices)):

            x1, y1, z1 = vertices[i]
            x2, y2, z2 = vertices[j]
            

            x1, y1 = x1*100 + 320, y1*100 + 240
            x2, y2= x2*100 + 320, y2*100 + 240
            if i == 4 and j==5:
                pygame.draw.line(screen, "red", (x1, y1), (x2, y2))
            elif i == 0 and j==4:
                pygame.draw.line(screen, "green", (x1, y1), (x2, y2))
            elif i == 7 and j==4:
                pygame.draw.line(screen, "blue", (x1, y1), (x2, y2))
            else:
                pygame.draw.line(screen, "white", (x1, y1), (x2, y2))


def main():
    running = True
    theta_x = 0
    xu = False
    
    theta_y = 0
    yu = False
    
    theta_z = 0
    zu = False
    
    theta_delta = math.pi/1800
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    yu = True 
                elif event.key == pygame.K_RIGHT:
                    zu = True 
                elif event.key == pygame.K_UP:
                    xu = True 
                
            else:
                xu,yu,zu = False,False,False


        if xu:
            theta_x += theta_delta
        if yu:
            theta_y +=theta_delta
        if zu:
            theta_z +=theta_delta
        Rx_matrix = Rx(theta_x)
        Ry_matrix = Ry(theta_y)
        Rz_matrix = Rz(theta_z)
        rotation_matrix = (Rx_matrix @ Ry_matrix) @ Rz_matrix
        rotated_vertices = np.dot(vertices, rotation_matrix)

        screen.fill((0, 0, 0))

        draw_cube(rotated_vertices)

        pygame.display.flip()
    pygame.quit()

main()

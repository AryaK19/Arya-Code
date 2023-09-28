import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
SL = 30 # spring length
m = 1.0  # Mass of block
k = 9.0  # Spring constant
c = 1  # Damping constant
g = 9.8  # Acceleration due to gravity
y = 30 # Displacement (m)



w = np.sqrt(k/m)  # Natural frequency
T = 2*np.pi/w  # Period

# Initial conditions
x0 = y*3  # Initial displacement
v0 = 0.0  # Initial velocity

# Time range
t = np.linspace(0, 100*T, 10000)

# Function to return derivatives
def derivatives(x, t, v):
    return v, -w**2*x - c*v + g

# Solve for x and v using the ODE solver
x, v = np.zeros_like(t), np.zeros_like(t)
x[0], v[0] = x0, v0
for i in range(1, t.size):
    dt = t[i] - t[i-1]
    x[i], v[i] = x[i-1] + derivatives(x[i-1], t[i-1], v[i-1])[0]*dt, v[i-1] + derivatives(x[i-1], t[i-1], v[i-1])[1]*dt

# Plot the results
fig, ax = plt.subplots()
ax.set_xlim(0, 10*T)
ax.set_ylim(1.1*x.min(), 1.1*x.max())
block, = ax.plot([], [], 'o-', lw=1)

Fnet = -k * x0 - m * g - c * v0

fig.suptitle(r' Damped Oscillation with ' + f"the net Force = {Fnet}",fontsize=16)

# Animation function
def animate(i):
    block.set_data(t[:i], x[:i])
    return block,

# Run the animation
ani = FuncAnimation(fig, animate, frames=len(t), interval=1, blit=True)

# Show the plot
plt.show()


import pygame
import pymunk
import pymunk.pygame_util


pygame.init()

width , height = 1000 , 700
window = pygame.display.set_mode([width,height])

# Variables



def text_screen(text,colour,x,y,font):
    screen_text = font.render(text,True,colour)
    window.blit(screen_text,[x,y])

def to_pygame(p):
    """Small hack to convert pymunk to pygame coordinates"""
    return int(p.x), int(-p.y + height)

def from_pygame(p):
    return to_pygame(p)

def Draw(window,space,draw_options,t):
    window.fill("black")
    space.debug_draw(draw_options)
    text_screen(f"Time : {t}",'white',10,10,pygame.font.SysFont(None,35))
    pygame.display.update()
     



def Create_pendulum(space,posix,posiy,m,y):
    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = (posix,0)

    body = pymunk.Body()
    body.position = (posix,posiy + y*10)

    shape = pymunk.Circle(body,20,(0,0))
    shape.elasticity = 1
    shape.mass = m
     
    shape.color = (194,194,194,100)
    rotation_center_joint = pymunk.DampedSpring(body,rotation_center_body, (0, 0), (0, 0),SL*6.5,damping=c/2,stiffness=k)

    space.add(shape,body,rotation_center_joint)
    

def run (window,width,height):
    exit_ = False
    selected = None
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps
    t = 0
    fr = 0

    space = pymunk.Space()

    mouse_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    space.gravity = (0,g)

    
    pendulems = 1
    
    
    Create_pendulum(space, 500 , 50 ,m , y ) 

    

    draw_options = pymunk.pygame_util.DrawOptions(window) 


    while not exit_:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_ = True
                break

            
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:

                    run(window,width,height)
                if event.key == pygame.K_LALT:

                    space.gravity = (0,0)
                if event.key == pygame.K_RALT:

                    space.gravity = (0,9.8)

                elif event.key == pygame.K_SPACE and dt != 0:
                    dt = 0
                elif event.key == pygame.K_SPACE and dt == 0:
                    dt = 1 / fps

        

        Draw(window,space,draw_options,t)
        
        fr+=1
        if fr%fps==0:
            t+=1
        space.step(dt)
        clock.tick(fps)
        pygame.display.update()

    pygame.quit()

run(window,width,height)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
m = 1.0  # Mass of block
k = 9.0  # Spring constant
b = 0.3  # Damping constant
g = 9.8  # Acceleration due to gravity
w = np.sqrt(k/m)  # Natural frequency
T = 2*np.pi/w  # Period

# Initial conditions
x0 = 0.5  # Initial displacement
v0 = 0.0  # Initial velocity

# Time range
t = np.linspace(0, 100*T, 10000)

# Function to return derivatives
def derivatives(x, t, v):
    return v, -w**2*x - b*v + g

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

Fnet = -k * x0 - m * g - b * v0

fig.suptitle(r' Damped Oscillation with ' + f"the net Force = {Fnet}",fontsize=16)

# Animation function
def animate(i):
    block.set_data(t[:i], x[:i])
    return block,

# Run the animation
ani = FuncAnimation(fig, animate, frames=len(t), interval=1, blit=True)

# Show the plot
plt.show()

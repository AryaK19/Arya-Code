import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initial conditions
y0 = 0.1 # initial position (meters)
v0 = 0 # initial velocity (meters/second)
m = 1 # mass of the object (kg)
k = 10 # spring constant (N/m)
g = 9.8 # acceleration due to gravity (m/s^2)
b = 0.1 # damping coefficient (kg/s)

# Time step and number of steps
dt = 0.01 # time step (seconds)
steps = 200 # number of steps

# Time array
t = np.arange(0, steps*dt, dt)

# Calculation of position and velocity using the formula for SHM with damping
y = y0 * np.exp(-b/2/m * t) * np.cos(np.sqrt(k/m - b**2/4/m**2) * t + np.arctan(v0 * m / (y0 * b)))
v = -y0 * np.exp(-b/2/m * t) * np.sqrt(k/m - b**2/4/m**2) * np.sin(np.sqrt(k/m - b**2/4/m**2) * t + np.arctan(v0 * m / (y0 * b))) + b/2/m * y

# Calculation of the net force on the object
Fnet = -k * y - m * g - b * v

# Initialize figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], 'o-', lw=2)

# Function to update the animation at each time step
def update(frame):
    line.set_data(t[:frame], y[:frame])
    ax.relim()
    ax.autoscale_view()
    return line,

# Set up the animation
ani = animation.FuncAnimation(fig, update, frames=steps, interval=1, blit=True,repeat=True)

# Save the animation as a .gif file
ani.save('anim.gif',writer="imagemagick")
print("DONE")
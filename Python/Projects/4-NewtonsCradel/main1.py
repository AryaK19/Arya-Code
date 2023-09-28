import numpy as np
import matplotlib.pyplot as plt

# Initial conditions
y0 = 0.1 # initial position (meters)
v0 = 0 # initial velocity (meters/second)
m = 1 # mass of the object (kg)
k = 10 # spring constant (N/m)
g = 9.8 # acceleration due to gravity (m/s^2)

# Time step and number of steps
dt = 0.01 # time step (seconds)
steps = 2000 # number of steps

# Time array
t = np.arange(0, steps*dt, dt)

# Calculation of position and velocity using the formula for SHM
y = y0 * np.cos(np.sqrt(k/m) * t) - (v0 + y0 * np.sqrt(k/m)) / np.sqrt(k/m) * np.sin(np.sqrt(k/m) * t)
v = -y0 * np.sqrt(k/m) * np.sin(np.sqrt(k/m) * t) + (v0 + y0 * np.sqrt(k/m)) * np.cos(np.sqrt(k/m) * t)

# Calculation of the net force on the object
Fnet = -k * y - m * g

# Plot of position vs. time
plt.figure()
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Position vs. Time')

# Plot of velocity vs. time
plt.figure()
plt.plot(t, v)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs. Time')

# Plot of net force vs. time
plt.figure()
plt.plot(t, Fnet)
plt.xlabel('Time (s)')
plt.ylabel('Net Force (N)')
plt.title('Net Force vs. Time')

plt.show()
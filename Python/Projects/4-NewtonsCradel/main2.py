import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Initial conditions
y0 = 0.1 # initial position (meters)
v0 = 0 # initial velocity (meters/second)
m = 1 # mass of the object (kg)
k = 10 # spring constant (N/m)
b = 0.2 # damping coefficient (kg/s)
g = 9.8 # acceleration due to gravity (m/s^2)

# Time step and number of steps
dt = 0.01 # time step (seconds)
steps = 2000 # number of steps

# Time array
t = np.arange(0, steps*dt, dt)

# Calculation of position and velocity using the formula for damped SHM
y = y0 * np.exp(-b/(2*m) * t) * np.cos(np.sqrt(k/m - b**2/(4*m**2)) * t)
v = -y0 * np.exp(-b/(2*m) * t) * (b/(2*m) * np.cos(np.sqrt(k/m - b**2/(4*m**2)) * t) + np.sqrt(k/m - b**2/(4*m**2)) * np.sin(np.sqrt(k/m - b**2/(4*m**2)) * t))

# Calculation of the net force on the object
Fnet = -k * y - b * v - m * g

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

fig, (ax1) = plt.subplots(1,1, figsize=(8,12))
fig.suptitle(r' Damped Oscillation with $\beta$$\approx$' + str(round(b,2)), fontsize=16)
line1, = ax1.plot([], [], lw=10,c="blue",ls="-",ms=50,marker="s",mfc="gray",fillstyle="none",mec="black",markevery=2)
time_text = ax1.text(0.1, 0.9, '', transform=ax1.transAxes)
time_template = '\nTime = %.1fs'

def init():
    line1.set_data([], [])
    time_text.set_text('')
    return line1, time_text

def animate(i):
    line1.set_data([y[i],0], [t[i],0])
    time_text.set_text(time_template % (i*dt))
    return line1, time_text

ani = animation.FuncAnimation(fig,animate, np.arange(1, steps),interval=50, blit=True, init_func=init(),repeat=True)

ani.save("ANIM.gif")
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


#Constants
x0 = 10.0             #Initial Aplitude
vx0 = 1.0             #Initial Velocity
w = 5                 #angular frequency
c = 0.1              #Damping Coefficient

#Function that implements rk4 integration
b = np.pi * c       #damping parameter
def rk4(t, x, f, dt):
    dx1 = f(t, x)*dt
    dx2 = f(t+0.5*dt, x+0.5*dx1)*dt
    dx3 = f(t+0.5*dt, x+0.5*dx2)*dt
    dx4 = f(t+dt, x+dx3)*dt
    return x+dx1/6.0+dx2/3.0+dx3/3.0+dx4/6.0

#Function that returns dX/dt for the linearly damped oscillator
def dXdt(t, X):
    x = X[0]
    vx = X[1]
    ax = -2*b*vx - w**2*x
    return np.array([vx, ax])


#Setting time array for graph visualization
dt = 0.05
N = 200
t = np.linspace(0,dt*N,N,endpoint=False)
x = np.zeros(N)
vx = np.zeros(N)
y = np.zeros(N)
# integrate equations of motion using rk4;
# X is a vector that contains the positions and velocities being integrated
X = np.array([x0, vx0])

for i in range(N):
    x[i] = X[0]
    vx[i] = X[1]
    # update the vector X to the next time step
    X = rk4(i*dt, X, dXdt, dt)

fig, (ax1, ax2, ax3) = plt.subplots(3,1, figsize=(8,12))
fig.suptitle(r' Damped Oscillation with $\beta$$\approx$' + str(round(b,2)) + r' and $\omega$$\approx$' + str(round(w,2)), fontsize=16)
line1, = ax1.plot([], [], lw=10,c="blue",ls="-",ms=50,marker="s",mfc="gray",fillstyle="none",mec="black",markevery=2)
line2, = ax2.plot([], [], lw=1, color='r')
line3, = ax3.plot([], [], lw=1, color='g')
time_template = '\nTime = %.1fs'
time_text = ax1.text(0.1, 0.9, '', transform=ax1.transAxes)


ax1.set_xlim(1.2*min(x), 1.2*max(x))
ax1.set_xlabel('x')
ax1.set_ylabel('y')

ax2.set_ylim(1.2*min(x), 1.2*max(x))
ax2.set_xlim(0, N*dt)
ax2.set_xlabel('t')
ax2.set_ylabel('x')

ax3.set_xlim(1.2*min(x), 1.2*max(x))
ax3.set_ylim(1.2*min(vx), 1.2*max(vx))
ax3.set_xlabel('x')
ax3.set_ylabel('vx')

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    time_text.set_text('')
    return line1, line2, line3, time_text

def animate(i):
    line1.set_data([x[i],0], [y[i],0])
    line2.set_data(t[:i], x[:i])
    line3.set_data(x[:i], vx[:i])
    time_text.set_text(time_template % (i*dt))
    return line1, line2, line3, time_text  

ani = animation.FuncAnimation(fig, animate, np.arange(1, N),interval=50, blit=True, init_func=init,repeat=True)

ani.save("ANIM.gif")
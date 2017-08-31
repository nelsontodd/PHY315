# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Animation to illustrate simple harmonic motion. 
Animation stops at four cardinal points of oscillation on mouse clicks.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse

# Set physical parameters:
#   k   - spring constant (newton/meter)
#   m   - mass (kg)
#   phi - phase (radian)
#   A   - amplitude (meter)

k   = 100 
m   = 20
phi = np.pi/3.
A   = 2

# Set derived parameters:
#   w  - angular frequency (radian/second)

w = np.sqrt(k/m)
 
# Set simulation parameters:
#   counter - current time
#   tt      - time array
#   xx      - coordinate of center of mass array
#   vv      - velocity of center of mass array
#   aa      - acceleration of center of mass array

counter =  0
tt      = [0]
xx      = [0]
vv      = [0]
aa      = [0]

# Setup plotting space
fig = plt.figure(figsize=(7,7))
ax1 = fig.add_subplot(1,1,1)
ax2 = fig.add_subplot(2,1,1)
ax3 = fig.add_subplot(3,1,1)
fig.subplots_adjust(hspace=.45)

# Function to return coordinate of center of mass
def fun(t):
    global w, phi, A
    return A*np.cos(w*t-phi)

# Function to return center of mass velocity
def vel(t):
    global w, phi, A
    return -A*w*np.sin(w*t-phi)

# Function to return center of mass acceleration
def acceleration(t):
    global w, phi, A
    return -A*w**2*np.cos(w*t-phi)

# Function to return coordinates of mass corners
def position(x):
    x1 = x - 1.
    x2 = x + 1.
    y1 =  1.
    y2 = -1.

    p1 = [x1, y2]
    p2 = [x2, y2]
    p3 = [x2, y1]
    p4 = [x1, y1]
    
    return [p1, p2, p3, p4]

# Function to capture mouse clicks
#   pause = 0 - run simulation
#   pause = 1 - w*t-phi = 0
#   pause = 2 - w*t-phi = pi/2
#   pause = 3 - w*t-phi = pi
#   pause = 4 - w*t-phi = 3*pi/2

pause = 0
def onClick(event):
    global pause

    if pause < 4:
        pause += 1
    else:
        pause = 0

# Animation function
def animate(i):
    global counter, tt, xx, A, vv, aa, pause
    ax3.clear()

    #
    # Generate mass-spring animation plot
    #
    plt.subplot(311)
    plt.xlim(-3.5, 3.5)
    plt.ylim(-2, 2)
    plt.xlabel("Displacement (m)")
    plt.title("m = 20 kg  k = 100 N/m  a = 2 m  phi = pi/3")
    cur_axes = plt.gca()
    cur_axes.axes.get_yaxis().set_visible(False)

    # Get coordinates of mass corners
    p1 = [position(fun(counter))[0][0], position(fun(counter))[0][1]]
    p2 = [position(fun(counter))[1][0], position(fun(counter))[1][1]]
    p3 = [position(fun(counter))[2][0], position(fun(counter))[2][1]]
    p4 = [position(fun(counter))[3][0], position(fun(counter))[3][1]]

    x     = [p1[0], p2[0], p3[0], p4[0], p1[0]]
    y     = [p1[1], p2[1], p3[1], p4[1], p1[1]]
    linex = [-4, p1[0]]
    liney = [0, 0]

    # Plot mass
    plt.plot(x, y, lw=5, color="blue")

    # Plot spring
    plt.plot(linex, liney, color="red", ls=":", lw=5)

    # Plot center of mass
    data_x = [fun(counter)]
    data_y = [0.]
    plt.plot(data_x, data_y, 'o', color="black")

    #
    # Generate velocity plot
    #
    plt.subplot(312)
    tt.append(counter)
    vv.append(vel(counter))
    plt.ylabel("Velocity (m/s)")
    plt.xlabel("Time (s)")
    plt.xlim(0,15)
    plt.ylim(-A*w-0.5, A*w+0.5)
    plt.plot(tt, vv, lw=1, color="green")
    plt.plot([0,15], [0,0], lw=0.5, color="black")

    #
    # Generate acceleration plot
    #
    plt.subplot(313)
    aa.append(acceleration(counter))
    plt.ylabel("Acceleration (m/s^2)")
    plt.xlabel("Time (s)")
    plt.xlim(0, 15)
    plt.ylim(-A*w**2-0.5, A*w**2+0.5)
    plt.plot(tt, aa, lw=1, color="green")
    plt.plot([0,15], [0,0], lw=0.5, color="black")

    #
    # Stop at cardinal points of osciilation on mouse clicks
    #
    dt = 0.075
    if pause == 1:
        if fun(counter)/A < 0.99:
            counter += dt
    elif pause == 2:
        if fun(counter)*fun(counter-dt) > 0.:
            counter += dt
    elif pause == 3:
        if fun(counter)/A > -0.99:
            counter += dt
    elif pause == 4:
        if fun(counter)*fun(counter-dt) > 0.:
            counter += dt
    else: 
        counter += dt
        
fig.canvas.mpl_connect('button_press_event', onClick)
ani = animation.FuncAnimation(fig, animate, interval=2)
plt.show()



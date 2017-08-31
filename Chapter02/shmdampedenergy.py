# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Animation to illustrate energy flows in damped simple harmonic motion. 
Pauses on mouse click.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse

# Set physical parameters:
#   k   - spring constant (newton/meter)
#   m   - mass (kg)
#   xnu - damping rate
#   phi - phase (radian)
#   A   - amplitude (meter)

k   = 100 
m   = 20
ga  = 0.05
phi = np.pi/3.
A   = 2

# Set derived parameters:
#   w  - angular frequency (radian/second)

w = np.sqrt(k/m)
 
# Set simulation parameters:
#   counter - current time
#   tt      - time array
#   xx      - coordinate of center of mass array
#   uu      - potential energy
#   kk      - kinetic energy
#   ee      - total energy

counter =  0.
tt      = [0]
xx      = [0]
uu      = [0]
kk      = [0]
ee      = [0]

# Setup plotting space
fig = plt.figure(figsize=(7,7))
ax1 = fig.add_subplot(1,1,1)
ax2 = fig.add_subplot(2,1,1)
ax3 = fig.add_subplot(3,1,1)
fig.subplots_adjust(hspace=.45)

# Function to return coordinate of center of mass
def fun(t):
    global w, phi, A
    return A*np.exp(-ga*t)*np.cos(w*t-phi)

# Function to return center of mass velocity
def vel(t):
    global w, phi, A
    return -A*np.exp(-ga*t)*w*np.sin(w*t-phi) - A*ga*np.exp(-ga*t)*np.cos(w*t-phi)

# Function to return potential energy
def potential(t):
    global w, phi, A, k
    return 0.5*k*fun(t)*fun(t)

# Function to return kinetic energy
def kinetic(t):
    global w, phi, A, m
    return 0.5*m*vel(t)*vel(t)

# Function to return total energy
def total(t):
    return potential(t) + kinetic(t)

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
pause = 0
def onClick(event):
    global pause

    if pause == 0:
        pause = 1
    else:
        pause = 0

# Animation function
def animate(i):
    global counter, tt, xx, A, uu, kk, ee, pause
    ax3.clear()

    #
    # Generate mass-spring animation plot
    #
    plt.subplot(311)
    plt.xlim(-3.5, 3.5)
    plt.ylim(-2, 2)
    plt.xlabel("Displacement (m)")
    plt.title("m = 20 kg  k = 100 N/m  a = 2 m  nu  =  0.1 rad/s  phi = pi/3")
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
    # Generate kinetic and potential energy plots
    #
    plt.subplot(312)
    tt.append(counter)
    uu.append(potential(counter))
    kk.append(kinetic(counter))
    plt.ylabel("Energy (J)")
    plt.xlabel("Time (s)")
    plt.xlim(0,15)
    plt.ylim(0., 250.)
    plt.plot(tt, uu, lw=1, color="green", label="U")
    plt.plot(tt, kk, lw=1, color="blue",  label="K")
    plt.plot([0,15], [0,0], lw=0.5, color="black")
    if counter == 0.:
        plt.legend(loc="upper right")

    #
    # Generate total energy plot
    #
    plt.subplot(313)
    ee.append(total(counter))
    plt.ylabel("Total Energy (J)")
    plt.xlabel("Time (s)")
    plt.xlim(0, 15)
    plt.ylim(0., 250.)
    plt.plot(tt, ee, lw=1, color="red")
    plt.plot([0,15], [0,0], lw=0.5, color="black")

    #
    # Pause on mouse click
    #
    dt = 0.075
    if pause == 0:
        counter += dt
        
fig.canvas.mpl_connect('button_press_event', onClick)
ani = animation.FuncAnimation(fig, animate, interval=2)
plt.show()



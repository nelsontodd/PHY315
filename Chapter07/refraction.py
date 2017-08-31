# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Animation to illustrate reflection and refraction of plane wave at plane boundary
between rarefied and dense media. 
Pauses on mouse click.

Input parameters:

i - angle of incidence (degrees)
n - refractive index
t - time step
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-i', type=float,  default=45., help='angle of incidence (degrees)')
parser.add_argument('-n', type=float,  default=1.5, help='refractive index')
parser.add_argument('-t', type=float,  default=0.1, help='time step')

# Read command line options
args = parser.parse_args()
i  = args.i
nr = args.n
dt = args.t

# Test input
if i < 0. or i > 90.: 
    print 'Error: i must be between 0 and 90'
    sys.exit(1)
if nr < 1.: 
    print 'Error: n must be greater than or equal to unity'
    sys.exit(1)
if dt <= 0.:
    print 'Error: t must be positive'
    sys.exit(1)

# Calculate directions of incident, relected, and refracted waves
theta_i = i*np.pi/180.
theta_r = (180.-i)*np.pi/180.
theta_t = np.arcsin(np.sin(theta_i)/nr)
tt = theta_t*180./np.pi

# y as function of x
def Gety(x, t, n, theta, index):
    
    return (n - index*x*np.cos(theta) + t)/np.sin(theta)/index

# x as function of y
def Getx(y, t, n, theta, index):
    
    return (n - index*y*np.sin(theta) + t)/np.cos(theta)/index

# Function to capture mouse clicks
pause = 0
def onClick(event):
    global pause

    if pause == 0:
        pause = 1
    else:
        pause = 0
        
# Setup plotting space
fig = plt.figure(figsize=(7,7))
ax1 = fig.add_subplot(1,1,1)

# Produce animation
counter = 0.

def animate(iii):
    global counter, pause, theta_i, theta_r, theta_t, i, tt, nr
    ax1.clear()

    # Generate animation plot
    A = 8.
    plt.xlim(-A, A)
    plt.ylim(-A, A)
    plt.xlabel(r"$x/\lambda$", size='large')
    plt.ylabel(r"$y/\lambda$", size='large')
    plt.title(r"$\theta_i$ = %3.0f$^\circ$  $\theta_t$ = %3.0f$^\circ$" %(i, tt), size='large')

    for ii in range(40):
        n = ii - 20

        # Plot incident wave
        ni = 1.
        x1 = -A
        y1 = Gety(-A, counter, n, theta_i, ni)
        x2 = 0.
        y2 = Gety(0., counter, n, theta_i, ni)
        x3 = Getx(-A, counter, n, theta_i, ni)
        y3 = -A
        x4 = Getx(+A, counter, n, theta_i, ni)
        y4 = +A

        if   -A < y1 < +A and -A < y2 < +A:
             plt.plot((x1,x2), (y1,y2), color="blue", ls="solid", lw=2)
        elif -A < y1 < +A and -A < x3 < 0.:
             plt.plot((x1,x3), (y1,y3), color="blue", ls="solid", lw=2)
        elif -A < y1 < +A and -A < x4 < 0.:
             plt.plot((x1,x4), (y1,y4), color="blue", ls="solid", lw=2)
        elif -A < y2 < +A and -A < x3 < 0.:
             plt.plot((x2,x3), (y2,y3), color="blue", ls="solid", lw=2)
        elif -A < y2 < +A and -A < x4 < 0.:
             plt.plot((x2,x4), (y2,y4), color="blue", ls="solid", lw=2)
        elif -A < x3 < 0. and -A < x4 < 0.:
             plt.plot((x3,x4), (y3,y4), color="blue", ls="solid", lw=2)

        # Plot reflected wave
        x1 = -A
        y1 = Gety(-A, counter, n, theta_r, ni)
        x2 = 0.
        y2 = Gety(0., counter, n, theta_r, ni)
        x3 = Getx(-A, counter, n, theta_r, ni)
        y3 = -A
        x4 = Getx(+A, counter, n, theta_r, ni)
        y4 = +A

        if   -A < y1 < +A and -A < y2 < +A:
             plt.plot((x1,x2), (y1,y2), color="green", ls="solid", lw=2)
        elif -A < y1 < +A and -A < x3 < 0.:
             plt.plot((x1,x3), (y1,y3), color="green", ls="solid", lw=2)
        elif -A < y1 < +A and -A < x4 < 0.:
             plt.plot((x1,x4), (y1,y4), color="green", ls="solid", lw=2)
        elif -A < y2 < +A and -A < x3 < 0.:
             plt.plot((x2,x3), (y2,y3), color="green", ls="solid", lw=2)
        elif -A < y2 < +A and -A < x4 < 0.:
             plt.plot((x2,x4), (y2,y4), color="green", ls="solid", lw=2)
        elif -A < x3 < 0. and -A < x4 < 0.:
             plt.plot((x3,x4), (y3,y4), color="green", ls="solid", lw=2)

        # Plot refracted wave
        x1 = 0.
        y1 = Gety(0., counter, n, theta_t, nr)
        x2 = +A
        y2 = Gety(+A, counter, n, theta_t, nr)
        x3 = Getx(-A, counter, n, theta_t, nr)
        y3 = -A
        x4 = Getx(+A, counter, n, theta_t, nr)
        y4 = +A

        if   -A < y1 < +A and -A < y2 < +A:
             plt.plot((x1,x2), (y1,y2), color="red", ls="solid", lw=2)
        elif -A < y1 < +A and 0. < x3 < +A:
             plt.plot((x1,x3), (y1,y3), color="red", ls="solid", lw=2)
        elif -A < y1 < +A and 0. < x4 < +A:
             plt.plot((x1,x4), (y1,y4), color="red", ls="solid", lw=2)
        elif -A < y2 < +A and 0. < x3 < +A:
             plt.plot((x2,x3), (y2,y3), color="red", ls="solid", lw=2)
        elif -A < y2 < +A and 0. < x4 < +A:
             plt.plot((x2,x4), (y2,y4), color="red", ls="solid", lw=2)
        elif 0. < x3 < +A and 0. < x4 < +A:
             plt.plot((x3,x4), (y3,y4), color="red", ls="solid", lw=2)

        plt.axvline(x=0., lw=3, color='black', ls='solid')
 
    if not pause:
        counter += dt

fig.canvas.mpl_connect('button_press_event', onClick)        
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()

# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Animation to illustrate propagation of plane wave.
Pauses on mouse click.

Input parameters:

a - angular direction (degrees)
t - time step
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-a', type=float,  default=45., help='angular direction (degrees)')
parser.add_argument('-t', type=float,  default=0.1, help='time step')

# Read command line options
args = parser.parse_args()
a  = args.a
dt = args.t

# Test input
if a < 0. or a > 180.: 
    print 'Error: a must be between 0 and 180'
    sys.exit(1)
if dt <= 0.:
    print 'Error: t must be positive'
    sys.exit(1)

# Convert angle to radians
ang = a*np.pi/180.

# y as function of x
def Gety(x, t, n):
    global ang
    
    return (n - x*np.cos(ang) + t)/np.sin(ang)

# x as function of y
def Getx(y, t, n):
    global ang
    
    return (n - y*np.sin(ang) + t)/np.cos(ang)

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

def animate(i):
    global counter, pause
    ax1.clear()

    # Generate animation plot
    A = 8.
    plt.xlim(-A, A)
    plt.ylim(-A, A)
    plt.xlabel(r"$x/\lambda$", size='large')
    plt.ylabel(r"$y/\lambda$", size='large')
    plt.title(r"$\theta$ = %3.0f$^\circ$" %a, size='large')

    for i in range(40):
        n = i - 20

        x1 = -A
        y1 = Gety(-A, counter, n)
        x2 = +A
        y2 = Gety(+A, counter, n)
        x3 = Getx(-A, counter, n)
        y3 = -A
        x4 = Getx(+A, counter, n)
        y4 = +A

        if   -A < y1 < +A and -A < y2 < +A:
             plt.plot((x1,x2), (y1,y2), color="blue", ls="solid", lw=2)
        elif -A < y1 < +A and -A < x3 < +A:
             plt.plot((x1,x3), (y1,y3), color="blue", ls="solid", lw=2)
        elif -A < y1 < +A and -A < x4 < +A:
             plt.plot((x1,x4), (y1,y4), color="blue", ls="solid", lw=2)
        elif -A < y2 < +A and -A < x3 < +A:
             plt.plot((x2,x3), (y2,y3), color="blue", ls="solid", lw=2)
        elif -A < y2 < +A and -A < x4 < +A:
             plt.plot((x2,x4), (y2,y4), color="blue", ls="solid", lw=2)
        elif -A < x3 < +A and -A < x4 < +A:
             plt.plot((x3,x4), (y3,y4), color="blue", ls="solid", lw=2)
 
    if not pause:
        counter += dt

fig.canvas.mpl_connect('button_press_event', onClick)        
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()

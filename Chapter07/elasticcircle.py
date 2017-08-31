# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy, matplotlib, and scipy

"""
Animation to illustrate normal modes of circular elastic sheet.
Pauses on mouse click.

Input parameters:

m - mode number
t - time step
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.special as sp
from matplotlib import colors, cm
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-m', type=int,    default=1,    help='mode number')
parser.add_argument('-t', type=float,  default=0.2,  help='time step')

# Read command line options
args = parser.parse_args()
m  = args.m
dt = args.t

# Test input
if m < 1:
    print 'Error: m must be positive'
    sys.exit(1)
if dt <= 0.:
    print 'Error: t must be positive'
    sys.exit(1)

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
    plt.xlim(-1., 1.)
    plt.ylim(-1., 1.)
    plt.xlabel(r"$x/a$", size='large')
    plt.ylabel(r"$y/a$", size='large')
    plt.title(r"$m$ = %3d" %m, size='large')

    zero = sp.jn_zeros(0,10)
    zr   = zero[m-1]
    
    N = 200
    x = np.linspace(-1., 1., N)
    y = np.linspace(-1., 1., N)
 
    X, Y = np.meshgrid(x, y)

    Z = np.zeros_like(X)

    for i in range(N):
        for j in range(N):
            r = np.sqrt(X[i,j]*X[i,j]+Y[i,j]*Y[i,j])
            if r < 1.:
                Z[i,j] = sp.j0(zr*r)*np.cos(counter)
 
    levels = np.arange(-1.02,1.02,0.01)
    
    cs = plt.contourf(X, Y, Z, levels, cmap=cm.bwr)

    theta = np.arange(0.,2.*np.pi,0.01)
    x = np.cos(theta)
    y = np.sin(theta)
    plt.plot (x, y, lw=4, color="black")
 
    if not pause:
        counter += dt

fig.canvas.mpl_connect('button_press_event', onClick)        
ani = animation.FuncAnimation(fig,animate,interval=1)

plt.show()

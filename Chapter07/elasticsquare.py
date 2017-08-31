# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Animation to illustrate normal modes of square elastic sheet.
Pauses on mouse click.

Input parameters:

m - x mode number
n - y mode number
t - time step
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors, cm
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-m', type=int,    default=1,    help='x mode number')
parser.add_argument('-n', type=int,    default=2,    help='y mode number')
parser.add_argument('-t', type=float,  default=0.01, help='time step')

# Read command line options
args = parser.parse_args()
m  = args.m
n  = args.n
dt = args.t

# Test input
if m < 1:
    print 'Error: m must be positive'
    sys.exit(1)
if n < 1:
    print 'Error: n must be positive'
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
    plt.xlim(0., 1.)
    plt.ylim(0., 1.)
    plt.xlabel(r"$x/a$", size='large')
    plt.ylabel(r"$y/a$", size='large')
    plt.title(r"$m$ = %3d  $n$ = %3d" %(m,n), size='large')

    N = 500
    x = np.linspace(0., 1., N)
    y = np.linspace(0., 1., N)
    w = np.pi*np.sqrt(1.*(m*m+n*n))

    X, Y = np.meshgrid(x, y)

    z = np.sin(m*np.pi*X)*np.sin(n*np.pi*Y)*np.cos(w*counter)

    levels = np.arange(-1.1,1.1,0.1)
    
    cs = plt.contourf(X, Y, z, levels, cmap=cm.bwr)
 
    if not pause:
        counter += dt

fig.canvas.mpl_connect('button_press_event', onClick)        
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()

# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Animation to illustate TE mode in rectangular waveguide.
Animation freezes on mouse clicks.

Input parameters:

j - mode number
w - ratio of mode frequency to cutoff frequency for j=1 mode
t - time step
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors, cm
import argparse

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-j', type=int,    default=1,    help='mode number')
parser.add_argument('-w', type=float,  default=2.,   help='mode frequency')
parser.add_argument('-t', type=float,  default=0.1,  help='time step')

# Read command line options
args = parser.parse_args()
j  = args.j
w  = args.w
dt = args.t

# Test input
if j < 1:
    print 'Error: j must be positive integer'
    sys.exit(1)
if w <= 0.:
    print 'Error: w must be positive'
    sys.exit(1)
if dt <= 0.:
    print 'Error: t must be positive'
    sys.exit(1)

# Setup plotting space
fig = plt.figure(figsize=(14.,6.))
ax1 = plt.subplot2grid((2,3),(0,0))
ax2 = plt.subplot2grid((2,3),(1,0),colspan=3)

# Function to capture mouse clicks
pause = 0
def onClick(event):
    global pause

    if pause == 0:
        pause = 1
    else:
        pause = 0

# Animation function
counter = 0.
def animate(i):
    global counter, pause
    ax2.clear()

    #
    # Generate x-y plot
    #
    plt.subplot2grid((2,3),(0,0))
    plt.xlabel(r"$y/b$", size='large')
    plt.ylabel(r"$x/a$", size='large')
    plt.title(r"TE mode, $E_y$: $j$ = %3d  $\omega/\omega_0$ = %4.2f" %(j, w), size='large')
    
    N = 500
    x = np.linspace(0., 1., N)
    y = np.linspace(0., 1., N)
    if (w > j):
        k = np.pi*np.sqrt(w*w-j*j)
    else:
        k = np.pi*np.sqrt(j*j-w*w)
    
    X, Y = np.meshgrid(x, y)

    F = np.sin(j*np.pi*X)*np.cos(w*counter)

    levels = np.arange(-1.1,1.1,0.1)

    cs = plt.contourf(Y, X, F, levels, cmap=cm.bwr)

    plt.plot((0,1,1,0,0),(0,0,1,1,0), color="black", lw=6)

    #
    # Generate x-z plot
    #
    plt.subplot2grid((2,3),(1,0),colspan=3)
    plt.xlabel(r"$z/a$", size='large')
    plt.ylabel(r"$x/a$", size='large')
   
    z = np.linspace(0., 5., N)
    
    X, Z = np.meshgrid(x, z)

    if (w > j):
        F1 = np.sin(j*np.pi*X)*np.cos(w*counter - k*Z)
    else:
        F1 = np.sin(j*np.pi*X)*np.cos(w*counter)*np.exp(-k*Z)
        
    cs1 = plt.contourf(Z, X, F1, levels, cmap=cm.bwr)
    plt.plot((0,5),(0,0), color="black", lw=6)
    plt.plot((0,5),(1,1), color="black", lw=6)
    plt.tight_layout()
    
    #
    # Freeze animation on mouse clicks
    #
    if not pause:
        counter += dt
        
fig.canvas.mpl_connect('button_press_event', onClick)
ani = animation.FuncAnimation(fig, animate, interval=2)
plt.show()



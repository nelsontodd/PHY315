# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Animation to illustrate propagation of spherical wave.
Wavefront thickness indicates amplitude.
Pauses on mouse click.

Input parameters:

t - time step
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-t', type=float,  default=0.1, help='time step')

# Read command line options
args = parser.parse_args()
dt = args.t

# Test input
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
    A = 8.
    plt.xlim(-A, A)
    plt.ylim(-A, A)
    plt.xlabel(r"$x/\lambda$", size='large')
    plt.ylabel(r"$y/\lambda$", size='large')

    for i in range(40):
        n = i - 20
        r = n + counter

        if (r > 0.4):
            theta = np.arange(0.,2.*np.pi,0.01)
            x     = r*np.cos(theta)
            y     = r*np.sin(theta)
            plt.plot(x, y, color="blue", lw=5./r)

    plt.plot(0., 0., 'o', color="black", markersize='10')
            
    if not pause:
        counter += dt

fig.canvas.mpl_connect('button_press_event', onClick)        
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()

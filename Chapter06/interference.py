# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy, matplotlib, and animation

"""
Animation to illustrate interference of two counter-propagating traveling waves.
Pauses on mouse click.

Input parameters:

a - ratio of wave amplitudes
t - time step
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-a', type=float,  default=1.,   help='amplitude ratio')
parser.add_argument('-t', type=float,  default=0.02,  help='time step')

# Read command line options
args = parser.parse_args()
A1 = 1.
A2 = args.a
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
counter = 0

def animate(i):
    global counter, pause, N
    ax1.clear()

    # Generate animation plot
    plt.xlim(0., 8.)
    plt.ylim(-1.25, 1.25)
    plt.xlabel("$x/\lambda$", size='large')
    plt.ylabel("$\psi$",      size='large')
    plt.title(r"$A_r$ = %3.1f  $A_l$ = %3.1f" %(A1, A2), size='large')

    x  =  np.arange(0., 8., 0.01)
    p1 =  np.cos(2.*np.pi*(counter - x))/(1.+A2)
    p2 = A2*np.cos(2.*np.pi*(counter + x))/(1.+A2)
    p  = p1 + p2
 
    plt.plot(x, p1, color="red",   ls="solid", lw=2)
    plt.plot(x, p2, color="blue",  ls="solid", lw=2)
    plt.plot(x, p , color="black", ls="solid", lw=3)
    plt.axhline(y=0.,  lw=2, color='green', ls='dotted')

    if not pause:
        counter += dt

fig.canvas.mpl_connect('button_press_event', onClick)        
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()

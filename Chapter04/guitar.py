# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Animation of motion of guitar string plucked at midpoint.
Animation freezes on mouse click.

Input parameters:

k  - number of harmonics
t  - time step
n  - damping rate
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-k', type=int,    default=16,   help='number of harmonics')
parser.add_argument('-t', type=float,  default=0.01, help='time step')
parser.add_argument('-n', type=float,  default=0.0,  help='damping rate')

# Read command line options
args = parser.parse_args()
K  = args.k
dt = args.t
nu = args.n

# Test input
if K < 1:
    print 'Error: k must be positive integer'
    sys.exit(1)
if dt <= 0.:
    print 'Error: t must be positive'
    sys.exit(1)
if nu < 0.:
    print 'Error: n must be non-negative'
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
    global counter, N, A, n, w, pause
    ax1.clear()

    # Generate animation plot
    plt.xlim(0., 1.)
    plt.ylim(-1.25, 1.25)
    plt.xlabel("$x/l$", size='large')
    plt.ylabel("$y/A$",   size='large')

    # Plot string 
    x = np.linspace(0., 1., 1000)
    y = np.zeros_like(x)

    for k in range(K):
        kk = k+1
        y += -2.*np.cos(kk*np.pi)/(kk-0.5)/(kk-0.5)/np.pi/np.pi\
             *np.sin((2.*kk-1.)*np.pi*x)\
             *np.cos(2.*np.pi*(2.*kk-1.)*counter)\
             *np.exp(-(2.*kk-1.)*nu*counter)

    plt.plot(x, y, color="blue", lw=3)
    plt.axhline(y=0., lw=2, color='red', ls='dotted')

    if not pause:
        counter += dt
        
fig.canvas.mpl_connect('button_press_event', onClick)
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()


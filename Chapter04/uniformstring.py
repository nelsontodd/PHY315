# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Animation to illustrate normal modes of oscillation of uniform string.
Animation freezes on mouse click.

Input parameters:

k - mode number
a - amplitude
t - time step
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-k', type=int,    default=1,    help='mode number')
parser.add_argument('-a', type=float,  default=0.75, help='amplitude')
parser.add_argument('-t', type=float,  default=0.05, help='time step')

# Read command line options
args = parser.parse_args()
n  = args.k
A  = args.a
dt = args.t

# Test input
if n < 1:
    print 'Error: k must be positive integer'
    sys.exit(1)
if A <= 0.:
    print 'Error: a must be positive'
    sys.exit(1)
if dt <= 0.:
    print 'Error: t must be positive'
    sys.exit(1)

# Set derived parameters
#   w - normal frequency / fundamental frequency

w = 1.*n

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
    plt.ylim(-A-0.25, A+0.25)
    plt.xlabel("$x/l$", size='large')
    plt.ylabel("$y$",   size='large')

    # Plot string 
    x = np.linspace(0., 1., 1000)
    y = A*np.sin(np.pi*n*x)*np.cos(w*counter)
    plt.plot(x, y, color="blue", lw=3)
    plt.axhline(y=0., lw=2, color='red', ls='dotted')

    if not pause:
        counter += dt
        
fig.canvas.mpl_connect('button_press_event', onClick)
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()


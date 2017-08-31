# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy, matplotlib, and animation

"""
Animation to illustrate difference between standing wave and travelling wave.
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
parser.add_argument('-t', type=float,  default=0.075,  help='time step')

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
ax2 = fig.add_subplot(2,1,1)
ax3 = fig.add_subplot(3,1,1)
fig.subplots_adjust(hspace=.60)



# Produce animation
counter = 0

def animate(i):
    global counter, pause
    plt.clf()
 
    # Generate standing wave plot
    plt.subplot(311)
    plt.xlim(0., 8.)
    plt.ylim(-1.5, 1.5)
    plt.xlabel("$x/\lambda$", size='large')
    plt.ylabel("$\psi$",      size='large')
    plt.title("$\psi = cos(k\,x)\,\cos(\omega\,t)$", color="red", size='large')
    plt.axhline(y=0., color='black', ls='dotted', lw=1)

    x  = np.arange(0., 8., 0.01)
    p  = np.cos(2.*np.pi*x)*np.cos(2.*np.pi*counter)
    plt.plot(x, p, color="red",   ls="solid",  lw=3)

    # Generate forward travelling wave plot
    plt.subplot(312)
    plt.xlim(0., 8.)
    plt.ylim(-1.5, 1.5)
    plt.xlabel("$x/\lambda$", size='large')
    plt.ylabel("$\psi$",      size='large')
    plt.title("$\psi = cos[k\,(x - \omega\,t)]$", color="blue", size='large')
    plt.axhline(y=0., color='black', ls='dotted', lw=1)

    p1 = np.cos(2.*np.pi*(x-counter))
    plt.plot(x, p1, color="blue",  ls="solid",  lw=3)
    
    # Generate backward travelling wave plot
    plt.subplot(313)
    plt.xlim(0., 8.)
    plt.ylim(-1.5, 1.5)
    plt.xlabel("$x/\lambda$", size='large')
    plt.ylabel("$\psi$",      size='large')
    plt.title("$\psi = cos[k\,(x + \omega\,t)]$", color="green", size='large')
    plt.axhline(y=0., color='black', ls='dotted', lw=1)
  
    p2 = np.cos(2.*np.pi*(x+counter))
    plt.plot(x, p2, color="green", ls="solid",  lw=3)
    
    if not pause:
        counter += dt

fig.canvas.mpl_connect('button_press_event', onClick)        
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()

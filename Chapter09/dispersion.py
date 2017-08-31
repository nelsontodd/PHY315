# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Animation to illustrate propagation of dispersive waves
Pauses on mouse click.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-v', type=float,  default=1.,   help='group velocity')
parser.add_argument('-t', type=float,  default=0.2,  help='time step')

# Read command line options
args = parser.parse_args()
vg = args.v
dt = args.t

# Test input
if vg < 0.:
    print 'Error: v must be positive'
    sys.exit(1)
if dt <= 0.:
    print 'Error: t must be positive'
    sys.exit(1)

# Wave data    
xmax = 10.;
dx   = 0.05;
k0   = 10.;
kmax = 10.;
dk   = 0.1
   
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
counter = -int(xmax/vg)

def animate(i):
    global counter, pause
    ax1.clear()

    # Generate animation plot
    plt.xlim(-10, 10)
    plt.ylim(-1.5, 1.5)
    plt.xlabel(r"$x$", size='large')

    xx = np.arange(-xmax,xmax,dx)
    kk = np.arange(-kmax+k0,kmax+k0,dk)
    yy = []

    for x in xx:
        sum = 0.
        for k in kk:
            sum += np.cos(k0*(counter-x))*np.exp(-(k-k0)*(k-k0)/2.)*np.cos((k-k0)*(vg*counter-x))*dk

        yy.append(sum/np.sqrt(2.*np.pi))
  
            
    plt.plot(xx, yy, color="blue", lw=3)    

    if not pause:
        counter += dt

fig.canvas.mpl_connect('button_press_event', onClick)        
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()

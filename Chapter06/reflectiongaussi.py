# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy, matplotlib, and animation

"""
Animation to illustrate reflection and transmission of Gaussian traveling wave 
pulse at boundary. Plots wave amplitude.
Pauses on mouse click.

Input parameters:

z - ratio of impedances
s - width of incident pulse
t - time step
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-z', type=float,  default=2.,   help='impedence ratio')
parser.add_argument('-s', type=float,  default=0.2,  help='pulse width')
parser.add_argument('-t', type=float,  default=0.08, help='time step')

# Read command line options
args = parser.parse_args()
Z1 = 1.
Z2 = args.z
s  = args.s
dt = args.t

# Test input
if Z2 <= 0.:
    print 'Error: z must be positive'
    sys.exit(1)
if s <= 0.:
    print 'Error: s must be positive'
    sys.exit(1)
if dt <= 0.:
    print 'Error: t must be positive'
    sys.exit(1)

# Forward propagating Gaussian pulse
def Gaussianf(x, t):
    global s
    
    tt = t*np.ones_like(x)
    xx = tt - x

    return np.exp(-xx*xx/s/s)

# Backward propagating Gaussian pulse
def Gaussianb(x, t):
    global s
    
    tt = t*np.ones_like(x)
    xx = tt + x

    return np.exp(-xx*xx/s/s)
    
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
counter = -10.

def animate(i):
    global counter, pause, N
    ax1.clear()

    # Calculate reflection and transmission coefficients
    t = 2.*Z2/(Z2+1.)
    r = (Z2-1.)/(Z2+1.)
    R = r*r
    T = t*t/Z2
    
    # Generate animation plot
    plt.xlim(-8., 8.)
    plt.ylim(-2.25, 2.25)
    plt.xlabel("$x$", size='large')
    plt.ylabel(r"$I$", size='large')
    plt.title(r"$Z_1$ = %3.1f  $Z_2$ = %3.1f  $R$ = %4.2f  $T$ = %4.2f" %(Z1, Z2, R, T), size='large')
  
    xl = np.arange(-8., 0., 0.01)
    xr = np.arange(0.,  8., 0.01)

    vl = Gaussianf(xl, counter) + r*Gaussianb(xl, counter)
    il = Gaussianf(xl, counter) - r*Gaussianb(xl, counter)
    vr = t*Gaussianf(xr, counter)
    ir = t*Gaussianf(xr, counter)/Z2
    el = il*vl
    er = ir*vr

    plt.plot(xl, il, color="blue", ls="solid", lw=2)
    plt.plot(xr, ir, color="blue", ls="solid", lw=2)
    plt.axhline(y=0., lw=2, color='black', ls='dotted')
    plt.axvline(x=0., lw=4, color='black')

    if not pause:
        counter += dt

fig.canvas.mpl_connect('button_press_event', onClick)        
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()

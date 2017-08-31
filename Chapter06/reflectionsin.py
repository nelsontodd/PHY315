# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy, matplotlib, and animation

"""
Animation to illustrate reflection and transmission of sinusoidal traveling wave 
train at boundary. Plots energy flux. Also plots mean energy flux.
Pauses on mouse click.

Input parameters:

z - ratio of impedences
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
parser.add_argument('-t', type=float,  default=0.08, help='time step')

# Read command line options
args = parser.parse_args()
Z1 = 1.
Z2  = args.z
dt = args.t

# Test input
if Z2 <= 0.:
    print 'Error: z must be positive'
    sys.exit(1)
if dt <= 0.:
    print 'Error: t must be positive'
    sys.exit(1)

# Forward propagating sinusoidal pulse
def Sinf(x, t):
    
    tt = t*np.ones_like(x)
    xx = tt - x

    return np.sin(xx)

# Backward propagating Gaussian pulse
def Sinb(x, t):
    
    tt = t*np.ones_like(x)
    xx = tt + x

    return np.sin(xx)
    
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

    # Calculate reflection and transmission coefficients
    t = 2.*Z2/(Z2+1.)
    r = (Z2-1.)/(Z2+1.)
    R = r*r
    T = t*t/Z2

    # Generate animation plot
    plt.xlim(-16., 16.)
    plt.ylim(-2.25, 2.25)
    plt.xlabel("$x$",    size='large')
    plt.ylabel(r"${\cal I}/{\cal I}_i$", size='large')
    plt.title(r"$Z_1$ = %3.1f  $Z_2$ = %3.1f  $R$ = %4.2f  $T$ = %4.2f" %(Z1, Z2, R, T), size='large')
    
    xl = np.arange(-16., 0., 0.01)
    xr = np.arange(0.,  16., 0.01)

    vl = Sinf(xl, counter) + r*Sinb(xl, counter)
    il = Sinf(xl, counter) - r*Sinb(xl, counter)
    vr = t*Sinf(xr, counter)
    ir = t*Sinf(xr, counter)/Z2
    el = 2.*il*vl
    er = 2.*ir*vr
    el0 = (1.-r*r)*np.ones_like(xl)
    er0 = (t*t/Z2)*np.ones_like(xr)

    plt.plot(xl, el, color="blue", ls="solid", lw=2)
    plt.plot(xr, er, color="blue", ls="solid", lw=2)
    plt.plot(xl, el0, color="red", ls="dashed", lw=2)
    plt.plot(xr, er0, color="red", ls="dashed", lw=2)
    plt.axhline(y=0., lw=2, color='black', ls='dotted')
    plt.axvline(x=0., lw=4, color='black')

    if not pause:
        counter += dt

fig.canvas.mpl_connect('button_press_event', onClick)        
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()

# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy, matplotlib, and animation

"""
Animation to illustrate quarter-wave transformer. Plots wave amplitude. 
Pauses on mouse click.

Input parameters:

z - impedance of transformer
t - time step
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-z', type=float,  default=2.,   help='Z3')
parser.add_argument('-t', type=float,  default=0.1, help='time step')

# Read command line options
args = parser.parse_args()
Z1 = 1.
Z2 = 100.
Z3 = args.z
dt = args.t

# Test input
if Z3 <= 0.:
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
counter = -10.

def animate(i):
    global counter, pause, N
    ax1.clear()

    # Calculate reflection and transmission coefficients
    r = (Z3*Z3-Z2)/(Z3*Z3+Z2)
    t = 2.*Z3*Z2/(Z3*Z3+Z2)
    a = Z3*(Z3+Z2)/(Z3*Z3+Z2)
    b = Z3*(Z3-Z2)/(Z3*Z3+Z2)
    R = r*r
    T = t*t/Z2
    
    # Generate animation plot
    plt.xlim(-16., 16.)
    plt.ylim(-3, 3)
    plt.xlabel("$x$",    size='large')
    plt.ylabel(r"${\cal I}$", size='large')
    plt.title(r"$Z_1$ = %3.1f  $Z_3$ = %3.1f  $Z_2$ = %3.1f  $R$ = %4.2f  $T$ = %4.2f" %(Z1, Z3, Z2, R, T), size='large')

    xl = np.arange(-16., 0., 0.01)
    xm = np.arange(0., np.pi/2., 0.01)
    xr = np.arange(np.pi/2., 16., 0.01)

    vl = Sinf(xl, counter) + r*Sinb(xl, counter)
    il = Sinf(xl, counter) - r*Sinb(xl, counter)
    vm = a*Sinf(xm, counter)    + b*Sinb(xm, counter)
    im = a*Sinf(xm, counter)/Z3 - b*Sinb(xm, counter)/Z3
    vr = t*Sinf(xr, counter)
    ir = t*Sinf(xr, counter)/Z2
    el = il*vl
    em = im*vm
    er = ir*vr

    plt.plot(xl, il, color="blue", ls="solid", lw=2)
    plt.plot(xm, im, color="blue", ls="solid", lw=2)
    plt.plot(xr, ir, color="blue", ls="solid", lw=2)
    plt.axhline(y=0., lw=2, color='black', ls='dotted')
    plt.axvline(x=0., lw=2, color='black')
    plt.axvline(x=np.pi/2., lw=2, color='black')

    if not pause:
        counter += dt

fig.canvas.mpl_connect('button_press_event', onClick)        
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()

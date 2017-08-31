# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy, matplotlib, and animation

"""
Animation to illustrate reflection of sinusoidal traveling wave 
at vacuum plasma boundary. Animation plots electric field.
Pauses on mouse click.

Input parameters:

w - ratio of wave frequency to plasma frequency
z - plot from -z to +z
t - time step
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-w', type=float,  default=0.8,  help='frequency ratio')
parser.add_argument('-z', type=float,  default=10.,  help='plot from -z to +z')
parser.add_argument('-t', type=float,  default=0.02, help='time step')

# Read command line options
args = parser.parse_args()
w  = args.w
z  = args.z
dt = args.t

# Test input
if w >= 1.:
    print 'Error: w must be less than unity'
    sys.exit(1)
if z <= 0.:
    print 'Error: z must be positive'
    sys.exit(1)    
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

    # Generate wave data
    alpha = np.sqrt(1./w/w-1.)
    pr    = np.arctan(2.*alpha/(1.-alpha*alpha))
    pt    = np.arctan(alpha)
    Et    = 2./np.sqrt(1.+alpha*alpha)
    R     = 1.
    T     = 0.

    # Generate animation plot
    plt.xlim(-z, z)
    plt.ylim(-2.25, 2.25)
    plt.xlabel("$z/\lambda_0$",    size='large')
    plt.ylabel(r"$E_x$", size='large')
    plt.title(r"$\omega/\omega_p$ = %4.2f  $R$ = %4.2f  $T$ = %4.2f" %(w, R, T), size='large')
    
    zl = np.arange(-z, 0., z*0.01)
    zr = np.arange(0., z, z*0.01)

    el = np.cos(2.*np.pi*(counter-zl)) +  np.cos(2.*np.pi*(counter+zl)+pr)
    er = Et*np.exp(-2.*np.pi*alpha*zr)*np.cos(2.*np.pi*counter+pt)

    plt.plot(zl, el, color="blue", ls="solid", lw=2)
    plt.plot(zr, er, color="blue", ls="solid", lw=2)
    plt.axhline(y=0., lw=2, color='black', ls='dotted')
    plt.axvline(x=0., lw=4, color='black')

    if not pause:
        counter += dt

fig.canvas.mpl_connect('button_press_event', onClick)        
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()

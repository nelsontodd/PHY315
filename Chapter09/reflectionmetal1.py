# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy, matplotlib, and animation

"""
Animation to illustrate reflection of sinusoidal traveling wave 
at vacuum metal boundary. Animation plots energy flux.
Also plots mean energy flux.
Pauses on mouse click.

Input parameters:

a - ratio of impedance in metal to that in free space
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
parser.add_argument('-a', type=float,  default=0.2,  help='impedance ratio')
parser.add_argument('-z', type=float,  default=10.,  help='plot from -z to +z')
parser.add_argument('-t', type=float,  default=0.02, help='time step')

# Read command line options
args = parser.parse_args()
a  = args.a
z  = args.z
dt = args.t

# Test input
if a <= 0.:
    print 'Error: a must be positive'
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
    Er = - np.sqrt(1.+a**4)/(1.+np.sqrt(2.)*a+a*a)
    pr = np.arctan2(-np.sqrt(2.)*a,1.-a*a)
    Et = np.sqrt(2.)*a*np.sqrt((1.+np.sqrt(2.)*a)**2+1.)/(1.+np.sqrt(2.)*a+a*a)
    pt = np.arctan2(1.,1.+np.sqrt(2.)*a)
    R  = Er*Er
    T  = 1.-R
    T1 = Et*Et/np.sqrt(2.)/a

    # Generate animation plot
    plt.xlim(-z, z)
    plt.ylim(-2.25, 2.25)
    plt.xlabel("$z/\lambda_0$",    size='large')
    plt.ylabel(r"${\cal I}_z/{\cal I}_{i\,z}$", size='large')
    plt.title(r"$Z/Z_0$ = %4.2f  $R$ = %4.2f  $T$ = %4.2f" %(a,R,T), size='large')
    
    zl = np.arange(-z, 0., 0.01*z)
    zr = np.arange(0.,  z, 0.01*z)

    el  = np.cos(2.*np.pi*(counter-zl)) +  Er*np.cos(2.*np.pi*(counter+zl)+pr)
    hl  = np.cos(2.*np.pi*(counter-zl)) -  Er*np.cos(2.*np.pi*(counter+zl)+pr)
    er  = Et*np.exp(-2.*np.pi*zr/np.sqrt(2.)/a)*np.cos(2.*np.pi*(counter-zr/np.sqrt(2.)/a)+pt)
    hr  = (Et/a)*np.exp(-2.*np.pi*zr/np.sqrt(2.)/a)*np.cos(2.*np.pi*(counter-zr/np.sqrt(2.)/a)+pt-np.pi/4.)
    il  = 2.*el*hl
    ir  = 2.*er*hr
    il0 = 1.-Er*Er*np.ones_like(zl)
    ir0 = (Et*Et/np.sqrt(2.)/a)*np.exp(-4.*np.pi*zr/np.sqrt(2.)/a)

    plt.plot(zl, il, color="blue", ls="solid", lw=2)
    plt.plot(zr, ir, color="blue", ls="solid", lw=2)
    plt.plot(zl, il0, color="red", ls="dashed", lw=2)
    plt.plot(zr, ir0, color="red", ls="dashed", lw=2)
    plt.axhline(y=0., lw=2, color='black', ls='dotted')
    plt.axvline(x=0., lw=4, color='black')

    if not pause:
        counter += dt

fig.canvas.mpl_connect('button_press_event', onClick)        
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()

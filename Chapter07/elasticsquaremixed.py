# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Animation to illustrate mixed mode of square elastic sheet.
Pauses on mouse click.

Input parameters:

m1 - x mode number of 1st mode
n1 - y mode number of 1st mode
m2 - x mode number of 2nd mode
n2 - y mode number of 2nd mode
t - time step
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors, cm
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-m1', type=int,    default=1,    help='x mode number of 1st mode')
parser.add_argument('-n1', type=int,    default=1,    help='y mode number of 1st mode')
parser.add_argument('-m2', type=int,    default=2,    help='x mode number of 2nd mode')
parser.add_argument('-n2', type=int,    default=2,    help='y mode number of 2nd mode')
parser.add_argument('-t', type=float,  default=0.01, help='time step')

# Read command line options
args = parser.parse_args()
m1 = args.m1
n1 = args.n1
m2 = args.m2
n2 = args.n2
dt = args.t

# Test input
if m1 < 1:
    print 'Error: m1 must be positive'
    sys.exit(1)
if n1 < 1:
    print 'Error: n1 must be positive'
    sys.exit(1)
if m2 < 1:
    print 'Error: m2 must be positive'
    sys.exit(1)
if n2 < 1:
    print 'Error: n2 must be positive'
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

    # Generate animation plot
    plt.xlim(0., 1.)
    plt.ylim(0., 1.)
    plt.xlabel(r"$x/a$", size='large')
    plt.ylabel(r"$y/a$", size='large')
    plt.title(r"$m_1$ = %3d  $n_1$ = %3d  $m_2$ = %3d  $n_2$ = %3d" %(m1,n1,m2,n2), size='large')

    N = 500
    x = np.linspace(0., 1., N)
    y = np.linspace(0., 1., N)
    w1 = np.pi*np.sqrt(1.*(m1*m1+n1*n1))
    w2 = np.pi*np.sqrt(1.*(m2*m2+n2*n2))

    X, Y = np.meshgrid(x, y)

    z  = 0.5*np.sin(m1*np.pi*X)*np.sin(n1*np.pi*Y)*np.cos(w1*counter)
    z += 0.5*np.sin(m2*np.pi*X)*np.sin(n2*np.pi*Y)*np.cos(w2*counter)

    levels = np.arange(-1.1,1.1,0.1)
    
    cs = plt.contourf(X, Y, z, levels, cmap=cm.bwr)
 
    if not pause:
        counter += dt

fig.canvas.mpl_connect('button_press_event', onClick)        
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()

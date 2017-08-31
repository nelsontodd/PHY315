# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Animation to illustrate normal modes of spring-coupled
mass system with both ends fixed.

Input parameters:

n - number of masses
k - mode number
a - relative amplitude
t - time step
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int,    default=8,    help='number of masses')
parser.add_argument('-k', type=int,    default=1,    help='mode number')
parser.add_argument('-a', type=float,  default=0.5,  help='amplitude')
parser.add_argument('-t', type=float,  default=0.3,  help='time step')

# Read command line options
args = parser.parse_args()
N  = args.n
n  = args.k
A  = args.a
dt = args.t

# Test input
if N < 0:
    print 'Error: n must be positive integer'
    sys.exit(1)
if n < 1 or n > N:
    print 'Error: k must lie between 1 and n'
    sys.exit(1)
if A <= 0.:
    print 'Error: a must be positive'
    sys.exit(1)
if dt <= 0.:
    print 'Error: t must be positive'
    sys.exit(1)

# Function to return normal frequency
def omega():
    global n, N
    return 2.*np.sin(0.5*np.pi*n/(N+1.))

# Set derived parameters
#   w - normal frequency /omega_0

w = omega()
    
# Function to return coordinate of center of ith mass
def X(t, i):
    global w, A
    return i + A*np.sin(np.pi*i*n/(N+1.))*np.cos(w*t)

# Function to return coordinates of mass corners
def position(x):
    x1 = x - 0.15
    x2 = x + 0.15
    y1 = 0.25 
    y2 = -0.25

    p1 = [x1, y2]
    p2 = [x2, y2]
    p3 = [x2, y1]
    p4 = [x1, y1]
    
    return [p1, p2, p3, p4]

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
    global counter, pause, N
    ax1.clear()

    # Generate animation plot
    plt.xlim(0., 1.+N)
    plt.ylim(-N/2, N/2)
    plt.xlabel("$x/a$", size='large')
    plt.ylabel("$y$", size='large')

    # Get coordinates of mass corners
    xx = np.zeros((4,N))
    yy = np.zeros((4,N))
    for i in range(N):
        ii = i+1

        # Plot masses
        xx[0,i] = position(X(counter,ii))[0][0]
        xx[1,i] = position(X(counter,ii))[1][0]
        xx[2,i] = position(X(counter,ii))[2][0]
        xx[3,i] = position(X(counter,ii))[3][0]

        yy[0,i] = position(X(counter,ii))[0][1]
        yy[1,i] = position(X(counter,ii))[1][1]
        yy[2,i] = position(X(counter,ii))[2][1]
        yy[3,i] = position(X(counter,ii))[3][1]

    # Plot masses
    for i in range(N):

        x = [xx[0,i], xx[1,i], xx[2,i], xx[3,i], xx[0,i]]
        y = [yy[0,i], yy[1,i], yy[2,i], yy[3,i], yy[0,i]]

        plt.plot(x, y, lw=3, color="blue")

    # Plot springs     
    for i in range(N-1):
       
        linex = [xx[1,i], xx[0,i+1]]
        liney = [0, 0]
        plt.plot(linex, liney, color="red", ls=":", lw=5)

    linex = [0., xx[0][0]]
    liney = [0, 0]
    plt.plot(linex, liney, color="red", ls=":", lw=5)

    linex = [xx[1][N-1], 1.+N]
    liney = [0, 0]
    plt.plot(linex, liney, color="red", ls=":", lw=5)

    if not pause:
        counter += dt

fig.canvas.mpl_connect('button_press_event', onClick)        
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()

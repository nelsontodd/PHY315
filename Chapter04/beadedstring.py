# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires nump and matplotlib

"""
Animation to illustrate normal modes of oscillation of beaded string.
Animation freezes on mouse click.

Input parameters:

n - number of beads
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
parser.add_argument('-n', type=int,    default=8,    help='number of beads')
parser.add_argument('-k', type=int,    default=1,    help='mode number')
parser.add_argument('-a', type=float,  default=0.75, help='amplitude')
parser.add_argument('-t', type=float,  default=0.05, help='time step')

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

# Set physical parameters
#   k - spring constant (newton/meter)
#   m -  mass (kg)

k   = 100 
m   = 20

# Function to return normal frequency
def omega():
    global k, m, n, N
    return 2.*np.sqrt(k/m)*np.sin(0.5*np.pi*n/(1.+N))

# Set derived parameters
#   w - normal frequency (rad/s)

w = omega()

# Function to return x-coordinates of masses
def X(t):
    global N
    
    x = np.zeros(N)
    for i in range(N):
        x[i] = 1.*i+1.

    return x    

# Function to return y-coordinates of masses
def Y(t):
    global N, A, n, w
    
    y = np.zeros(N)
    for i in range(N):
        y[i] = A*np.sin(np.pi*n*(1.+i)/(1.+N))*np.cos(w*t)

    return y    

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
    plt.xlim(0., 1.+N)
    plt.ylim(-A-0.25, A+0.25)
    plt.xlabel("$x/a$", size='large')
    plt.ylabel("$y$", size='large')

    # Get x-coordinates of masses
    x_data = X(counter)

    # Get y-coordinates of masses
    y_data = Y(counter)

    xx_data = np.append ([0.],x_data)
    yy_data = np.append ([0.],y_data)
    xx_data = np.append (xx_data,[1.+N])
    yy_data = np.append (yy_data,[0.])

    # Plot envelope
    x = np.linspace(0., 1.+N, 1000)
    y = A*np.sin(np.pi*n*x/(1.+N))*np.cos(w*counter)
    plt.plot(x, y, color="green", ls="dotted", lw=1)

    # Plot strings
    plt.plot(xx_data, yy_data, lw='4', ls='dotted', color="blue")

    # Plot masses
    plt.plot(x_data, y_data, 'o', color="black", markersize='10')
    plt.axhline(y=0., lw=2, color='red', ls='dotted')

    if not pause:
        counter += dt
        
fig.canvas.mpl_connect('button_press_event', onClick)
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()


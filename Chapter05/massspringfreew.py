# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Script to plot normal frequecies of mass-spring system with left end free and
right end fixed.

Input parameters:

n - number of masses
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int,    default=8,    help='number of masses')

# Read command line options
args = parser.parse_args()
N  = args.n

# Test input
if N < 0:
    print 'Error: n must be positive integer'
    sys.exit(1)

# Function to return normal frequencies
def omega():
    global N

    w = np.zeros(N)
    
    for i in range(N):
        w[i] = 2.*np.sin(0.5*np.pi*(i+0.5)/(N+0.5))
        
    return w

# Function to return normal wavenumbers
def wave():
    global N

    k = np.zeros(N)
    
    for i in range(N):
        k[i] = np.pi*(i+0.5)/(N+0.5)
        
    return k    

# Produce plot
fig = plt.figure(figsize=(7,7))
ax1 = fig.add_subplot(1,1,1)

plt.xlim(0., np.pi)
plt.ylim(0., np.pi)
plt.xlabel(r"$k\,a$", size='large')
plt.ylabel(r"$\omega/\omega_0$", size='large')

x_data = wave()
y_data = omega()

xx_data = np.append ([0.],x_data)
yy_data = np.append ([0.],y_data)
xx_data = np.append (xx_data,[1.+N])
yy_data = np.append (yy_data,[2.])

plt.plot([0.,np.pi], [0.,np.pi], lw='2', ls='dotted', color="red")
plt.plot(xx_data, yy_data, lw='4', ls='dotted', color="blue")
plt.plot(x_data, y_data, 'o', color="black", markersize='10')

plt.show()


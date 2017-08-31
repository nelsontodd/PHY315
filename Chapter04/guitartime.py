# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Script to plot displacement of midpoint of guitar string plucked at midpoint
versus time.

Input parameters:

k  - number of harmonics
m  - maximum time
n  - damping rate
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-k', type=int,    default=16,   help='number of harmonics')
parser.add_argument('-m', type=float,  default=10.,  help='maximum time')
parser.add_argument('-n', type=float,  default=0.0,  help='damping rate')

# Read command line options
args = parser.parse_args()
K  = args.k
T  = args.m
nu = args.n

# Test input
if K < 1:
    print 'Error: k must be positive integer'
    sys.exit(1)
if T <= 0.:
    print 'Error: m must be positive'
    sys.exit(1)
if nu < 0.:
    print 'Error: n must be non-negative'
    sys.exit(1)

# Produce plot
fig = plt.figure(figsize=(7,7))
ax1 = fig.add_subplot(1,1,1)

plt.xlim(0., T)
plt.ylim(-1.25, 1.25)
plt.xlabel(r"$t/\tau$", size='large')
plt.ylabel(r"$y(x=l/2)/A$", size='large')

t = np.linspace(0., T, 1000)
y = np.zeros_like(t)

for k in range(K):
    kk = k+1
    y += 2./(kk-0.5)/(kk-0.5)/np.pi/np.pi\
         *np.cos(2.*np.pi*(2.*kk-1.)*t)\
         *np.exp(-(2.*kk-1.)*nu*t)
    
plt.plot(t, y, color="blue", lw=3)
plt.axhline(y=0., lw=2, color='red', ls='dotted')

plt.show()


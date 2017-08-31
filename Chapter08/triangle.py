# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Function to illustrate Fourier transform of triangle function

Inputs:

km - maximum value of k
dk - step length in k
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-km', type=float, default=40,   help='k_max')
parser.add_argument('-dk', type=float, default=0.01, help='dk')

# Read command line options
args = parser.parse_args()
kmax = args.km
dk   = args.dk

# Test input
if kmax <= 0.:
    print 'Error: km must be positive'
    sys.exit(1)
if dk <= 0.: 
    print 'Error: dk must be positive'
    sys.exit(1)

xmax = 2.
dx   = 0.01

# Setup plotting space
fig = plt.figure(figsize=(15.,5.))
ax1 = fig.add_subplot(1,1,1)
ax2 = fig.add_subplot(1,2,1)
ax3 = fig.add_subplot(1,3,1)
fig.subplots_adjust(hspace=2.)

# Plot function
plt.subplot(131)
plt.xlim(-xmax, xmax)
plt.ylim(-0.1, 1.2)
plt.xlabel("$x/l$", size="large")
plt.title(R"Function", size="large")

plt.plot((-2.,-0.5,-0.,0.5,2.),(0.,0.,1.,0.,0.), lw=3, color="black")
plt.axvline(x=0.,  lw=1, color='black', ls='dotted')
plt.axhline(y=0.,  lw=1, color='black', ls='dotted')

# Plot Fourier transform
plt.subplot(132)
plt.xlim(-kmax, kmax)
plt.ylim(-0.01, 0.17)
plt.xlabel("$k\,l$", size="large")
plt.title(R"Fourier Transform", size="large")

kk = np.arange (-kmax, kmax, dk)
CC = np.sin(kk/4.)*np.sin(kk/4.)/(kk/4.)/(kk/4.)/4./np.pi

plt.plot(kk, CC, lw=3, color="black")
plt.axvline(x=0.,  lw=1, color='black', ls='dotted')
plt.axhline(y=0.,  lw=1, color='black', ls='dotted')

# Plot inverse Fourier transform
plt.subplot(133)
plt.xlim(-xmax, xmax)
plt.ylim(-0.1, 1.2)
plt.xlabel("$x/l$", size="large")
plt.title(R"Inverse Fourier Transform", size="large")

xx = np.arange (-xmax, xmax, dx)
ff = []
for x in xx:
    sum = 0.;
    for k, C in zip(kk, CC):
        sum += C*np.cos(k*x)*dk

    ff.append(sum)

plt.plot(xx, ff, lw=3, color="black")
plt.axvline(x=0.,  lw=1, color='black', ls='dotted')
plt.axhline(y=0.,  lw=1, color='black', ls='dotted')

plt.show()

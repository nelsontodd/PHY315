# Author: Richard Fitzpatrick
# Modified from  http://matplotlib.org/examples/widgets/slider_demo.py
# Requires numpy,  matplotlib, and scipy

"""
Widget to illustrate Rayleigh criterion for resolving
power of telescope. Plots intensity versus angle in two
dimensions. Saves output as png image. 

Input parameter:

d - angular separation between stars
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib import colors, cm
import scipy.special as sp
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-d', type=float, default=1.22, help='angular spacing')

# Read command line options
args = parser.parse_args()
d  = args.d

# Test input
if d < 0.:
    print 'Error: d must be positive'
    sys.exit(1)

# Setup plotting space
fig = plt.figure(figsize=(7,7))
ax1 = fig.add_subplot(1,1,1)

# Generate plot
plt.xlim(-8., 8.)
plt.ylim(-8., 8.)
plt.xlabel(r"$\theta_x\,D/\lambda$", size='large')
plt.ylabel(r"$\theta_y\,D/\lambda$", size='large')
plt.title (r"$\Delta\theta\,D/\lambda$ = %4.2f" %(d))

N = 1000
x = np.linspace(-8., 8., N)
y = np.linspace(-8., 8., N)

X, Y = np.meshgrid(x, y)

Z = np.zeros_like(X)

for i in range(N):
        for j in range(N):
            r1 = np.sqrt(Y[i,j]*Y[i,j]+(X[i,j]-d/2.)*(X[i,j]-d/2.))
            r2 = np.sqrt(Y[i,j]*Y[i,j]+(X[i,j]+d/2.)*(X[i,j]+d/2.))
            Z[i,j]  = (sp.j0(np.pi*r1) + sp.jn(2,np.pi*r1))**2
            Z[i,j] += (sp.j0(np.pi*r2) + sp.jn(2,np.pi*r2))**2

max = np.amax(Z) + 0.01            
levels = np.arange(0.,max,0.01)
    
cs = plt.contourf(X, Y, Z, levels, cmap=cm.Reds)

plt.savefig("airy.png")
plt.show()

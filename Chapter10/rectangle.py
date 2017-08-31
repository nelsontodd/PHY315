# Author: Richard Fitzpatrick
# Modified from  http://matplotlib.org/examples/widgets/slider_demo.py
# Requires numpy and matplotlib

"""
Widget to illustrate two-dimensional, far-field, interference pattern
due to rectangular aperture normally illuminated by light from monochromatic 
source of negligible angular extent. Plots square root of intensity of 
light versus angle. 

Input parameters:

b - Aspect ratio of aperture.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib import colors, cm
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-b', type=float, default=2., help='aspect ratio')

# Read command line options
args = parser.parse_args()
b  = args.b

# Test input
if b < 0.:
    print 'Error: b must be positive'
    sys.exit(1)

# Setup plotting space
fig = plt.figure(figsize=(7,7))
ax1 = fig.add_subplot(1,1,1)

# Generate plot
plt.xlim(-3., 3.)
plt.ylim(-3., 3.)
plt.xlabel(r"$\theta_x\,a/\lambda$", size='large')
plt.ylabel(r"$\theta_y\,a/\lambda$", size='large')
plt.title(r"$b/a$ = %3.0f" %(b), size='large')

N = 1000
x = np.linspace(-3., 3., N)
y = np.linspace(-3., 3., N)

X, Y = np.meshgrid(x, y)

Z = np.abs(np.sinc(X)*np.sinc(b*Y))

levels = np.arange(0.,1.01,0.01)
    
cs = plt.contourf(X, Y, Z, levels, cmap=cm.Reds)

plt.show()

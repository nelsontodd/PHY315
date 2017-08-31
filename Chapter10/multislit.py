# Author: Richard Fitzpatrick
# Modified from  http://matplotlib.org/examples/widgets/slider_demo.py
# Requires numpy and matplotlib

"""
Widget to illustrate multi-slit, far-field interference
due to monochromatic light source of negligible angular extent.
Plots intensity of light versus angle as function
of d/lambda and delta/lambda, where d is slit-spacing,
lambda is wavelength, and delta is slit width.

Input Parameter:

n - number of slits
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import argparse
import sys

# Set up command line options
parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int, default=10, help='number of slits')

# Read command line options
args = parser.parse_args()
N  = args.n

# Test input
if N < 2:
    print 'Error: n must be greater than unity'
    sys.exit(1)

# Generate initial plot
t   = np.arange(-0.5,0.5,0.0001)
d0  = 10.
dd0 = 2.
F1  = np.sin(np.pi*N*d0*np.sin(t*np.pi))/ np.sin(np.pi*d0*np.sin(t*np.pi))/ (1.*N)
F2  = np.sinc(dd0*np.sin(t*np.pi))
I = F1*F1*F2*F2

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.20, bottom=0.30)
l,  = plt.plot(t, I, lw=2, color='red')
plt.axis([-0.5, 0.5, 0., 1.1])
plt.xlabel(r'$\theta/\pi$', size='large')
plt.ylabel('$I$', size='large')
plt.title('$N$ = %3d' %(N))

# Generate slider
axcolor = 'lightgoldenrodyellow'
axd     = plt.axes([0.20, 0.15, 0.65, 0.03], axisbg=axcolor)
axt     = plt.axes([0.20, 0.10, 0.65, 0.03], axisbg=axcolor)
sd      = Slider(axd, r'$d/\lambda$', 0., 20., valinit=d0)
sdd     = Slider(axt, r'$\delta/\lambda$', 0., 20., valinit=dd0)

# Update plot using slider data
def update(val):
    d  = sd.val
    dd = sdd.val
    F1  = np.sin(np.pi*N*d*np.sin(t*np.pi))/ np.sin(np.pi*d*np.sin(t*np.pi))/ (1.*N)
    F2  = np.sinc(dd*np.sin(t*np.pi))
    l.set_ydata(F1*F1*F2*F2)
    fig.canvas.draw_idle()
sd.on_changed(update)
sdd.on_changed(update)

# Generate reset button
resetax = plt.axes([0.8, 0.02, 0.1, 0.04])
button  = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sd.reset()
    sdd.reset()
button.on_clicked(reset)

plt.show()

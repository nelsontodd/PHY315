# Author: Richard Fitzpatrick
# Modified from  http://matplotlib.org/examples/widgets/slider_demo.py
# Requires numpy and matplotlib

"""
Script to illustrate relationship between gaussian function and its fourier transform.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Setup plotting space
fig = plt.figure(figsize=(15.,5.))
ax1 = fig.add_subplot(1,1,1)
ax2 = fig.add_subplot(1,2,1)
fig.subplots_adjust(hspace=2.)
plt.subplots_adjust(left=0.20, bottom=0.30)

xmax = 4.
dx   = 0.01
kmax = 4.
dk   = 0.01
sigmax = 1.
sigmak = 1.
ymax   = 1.

# Generate initial plot
xx   = np.arange(-xmax, xmax, dx)
ff   = np.exp(-xx*xx/2./sigmax)

kk   = np.arange(-kmax, kmax, dk)
gg   = np.exp(-kk*kk/2./sigmak)/np.sqrt(2.*np.pi)/sigmak


# Plot Fourier transform
plt.subplot(121)
plt.xlim(-kmax, kmax)
plt.ylim(-0.0, ymax)
plt.xlabel("$k$", size="large")
plt.title(R"Fourier Transform", size="large")

l2, = plt.plot(kk, gg, lw=3, color="black")
plt.axvline(x=0.,  lw=1, color='black', ls='dotted')

# Plot function
plt.subplot(122)
plt.xlim(-xmax, xmax)
plt.ylim(0., 1.2)
plt.xlabel("$x$", size="large")
plt.title(R"Function", size="large")

l1, = plt.plot(xx, ff, lw=3, color="black")
plt.axvline(x=0.,  lw=1, color='black', ls='dotted')


# Generate slider
axcolor = 'lightgoldenrodyellow'
axnu    = plt.axes([0.20, 0.15, 0.65, 0.03], axisbg=axcolor)
snu     = Slider(axnu, r'$\sigma_x$', 0.01, 100., valinit=1.)

# Update plot using slider data
def update(sigmax):
    sigmak=1./sigmax
    ff = np.exp(-xx*xx/2./sigmax)
    gg = np.exp(-kk*kk/2./sigmak)/np.sqrt(2.*np.pi)/sigmak

    ym = 1./np.sqrt(2.*np.pi)/sigmak
    if ym > 0.9*ymax or ym < ymax/2.:
        ax2.set_ylim(0, 1.5*ym)
        ax2.figure.canvas.draw()
        
    l1.set_ydata(ff)
    l2.set_ydata(gg)
    fig.canvas.draw_idle()
snu.on_changed(update)

# Generate reset button
resetax = plt.axes([0.8, 0.02, 0.1, 0.04])
button  = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    snu.reset()
button.on_clicked(reset)

plt.show()

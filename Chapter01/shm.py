# Author: Richard Fitzpatrick
# Modified from  http://matplotlib.org/examples/widgets/slider_demo.py
# Requires numpy and matplotlib

"""
Widget to illustrate solution of simple harmonic oscillator equation.
Shows how solution 

 x(t) = a*cos(2*pi*f - phi)

depends on choice of amplitude, a, frequency, f, and phase angle, phi.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import matplotlib

font = {'size' : 13}
matplotlib.rc('font', **font)

# Generate initial plot
t  = np.arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 3
p0 = 180
x  = a0*np.cos(2.*np.pi*f0*t-p0*np.pi/180.)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.20, bottom=0.30)
l,  = plt.plot(t, x, lw=2, color='red')
plt.axhline(y=0., lw=2, color='blue', ls='dotted')
plt.axis([0, 1, -10, 10])
plt.xlabel(r'$t({\rm s})$', size='large')
plt.ylabel(r'$x({\rm m})$', size='large')
plt.title(r'$x = a \,\cos (2 \pi\, f\, t - \phi)$', size='large')

# Generate sliders
axcolor = 'lightgoldenrodyellow'
axamp   = plt.axes([0.20, 0.17, 0.65, 0.03], axisbg=axcolor)
axfreq  = plt.axes([0.20, 0.12, 0.65, 0.03], axisbg=axcolor)
axphas  = plt.axes([0.20, 0.07, 0.65, 0.03], axisbg=axcolor)
samp    = Slider(axamp,  r'$a({\rm m})$',      0.1, 10.0,  valinit=a0)
sfreq   = Slider(axfreq, r'$f({\rm s^{-1}})$', 0.1, 30.0,  valinit=f0)
sphas   = Slider(axphas, r'$\phi(^\circ)$',    0.1, 360.0, valinit=p0)

# Update plot using slider data
def update(val):
    amp  = samp.val
    freq = sfreq.val
    phas = sphas.val
    l.set_ydata(amp*np.cos(2.*np.pi*freq*t-phas*np.pi/180.))
    fig.canvas.draw_idle()

sfreq.on_changed(update)
samp.on_changed(update)
sphas.on_changed(update)

# Generate reset button
resetax = plt.axes([0.8, 0.01, 0.1, 0.04])
button  = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sfreq.reset()
    samp.reset()
    sphas.reset()

button.on_clicked(reset)

# Show plot
plt.show()


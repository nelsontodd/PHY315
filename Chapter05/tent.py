# Author: Richard Fitzpatrick
# Modified from  http://matplotlib.org/examples/widgets/slider_demo.py
# Requires numpy and matplotlib

"""
Widget to illustrate how Fourier reconstruction of tent waveform
depends on number terms included in series.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

t = np.arange(0.0, 4.0, 0.001)

def gety(N):

   y = np.zeros_like(t)
   y += 0.5
   
   for n in range(N):
       nn = n+1
       y += -np.sin(0.5*np.pi*nn)*np.sin(0.5*np.pi*nn)/(0.5*np.pi*nn)/(0.5*np.pi*nn)\
            *np.cos(2.*np.pi*nn*t)

   return y    

# Generate initial plot
N0  = 4.
i   = int(round(N0))
y   = gety(i)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.20, bottom=0.30)
l,  = plt.plot(t, y,  lw=2, color='blue')
plt.axhline(y=1.,  lw=2, color='red', ls='dotted')
plt.axis([0, 4., 0., 1.25])
plt.xlabel(r'$t/\tau$', size='large')
plt.ylabel('$y/A$', size='large')

# Generate slider
axcolor = 'lightgoldenrodyellow'
axn     = plt.axes([0.20, 0.15, 0.65, 0.03], axisbg=axcolor)
sn      = Slider(axn, r'$N$', 1., 64., valinit=N0, valfmt='%1.0f')

# Update plot using slider data
def update(val):
    N  = sn.val
    i  = int(round(N))
    l.set_ydata(gety(i))
    fig.canvas.draw_idle()
sn.on_changed(update)

# Generate reset button
resetax = plt.axes([0.8, 0.02, 0.1, 0.04])
button  = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sn.reset()
button.on_clicked(reset)

plt.show()

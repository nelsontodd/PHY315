# Author: Richard Fitzpatrick
# Modified from  http://matplotlib.org/examples/widgets/slider_demo.py
# Requires numpy and matplotlib

"""
Widget to illustrate how amplitude of time-asymptotic solution
to damped driven harmonic oscillator equation depends on normalized
damping rate. Solution is

x(w) = 1/sqrt((1-w*w)*(1-w*w) + nu*nu*w*w)

where x = x_0/X_0, w = omega/omega_0, and nu = nu/omega_0. Here, omega_0 is
undamped angular oscillation frequency. Quality factor Q = 1/nu. 
nu is adjustable. 
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Generate initial plot
w   = np.arange(0.0, 2.0, 0.001)
nu0 = 0.1
x0  = 1./np.sqrt((1.-w*w)*(1.-w*w)+nu0*nu0*w*w)
ym = 15

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.20, bottom=0.30)
l,  = plt.plot(w, x0,  lw=2, color='red')
plt.axvline(x=1., lw=2, color='blue', ls='dotted')
plt.axis([0, 2, 0, ym])
plt.xlabel('$\omega/\omega_0$', size='large')
plt.ylabel('$x_0/X_0$', size='large')

# Generate slider
axcolor = 'lightgoldenrodyellow'
axnu    = plt.axes([0.20, 0.15, 0.65, 0.03], axisbg=axcolor)
snu     = Slider(axnu, r'$\nu/\omega_0$', 0., 0.5, valinit=nu0)

# Update plot using slider data
def update(val):
    nu  = snu.val
    x   = 1./np.sqrt((1.-w*w)*(1.-w*w)+nu*nu*w*w)

    ymax = 1./nu
    if ymax > ym or ymax < ym/2.:
        ax.set_ylim(0, 1.5*ymax)
        ax.figure.canvas.draw()
           
    l.set_ydata(x)
    fig.canvas.draw_idle()
snu.on_changed(update)

# Generate reset button
resetax = plt.axes([0.8, 0.02, 0.1, 0.04])
button  = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    snu.reset()
button.on_clicked(reset)

plt.show()

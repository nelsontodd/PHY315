# Author: Richard Fitzpatrick
# Modified from  http://matplotlib.org/examples/widgets/slider_demo.py
# Requires numpy and matplotlib

"""
Widget to illustrate how phase of time-asymptotic solution
to damped driven harmonic oscillator equation depends on normalized
damping rate. Solution is

phi(w) = atan (nu*w / (1-w*w))

where w = omega/omega_0, and nu = nu/omega_0. Here, omega_0 is
undamped angular oscillation frequency. Q = 1/nu. 
nu is adjustable. 
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Generate initial plot
w   = np.arange(0.0, 2.0, 0.001)
nu0 = 0.1
p0  = np.arctan2(nu0*w,1.-w*w)/np.pi

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.20, bottom=0.30)
l,  = plt.plot(w, p0,  lw=2, color='red')
plt.axvline(x=1., lw=2, color='blue', ls='dotted')
plt.axhline(y=0.5, lw=2, color='blue', ls='dotted')
plt.axis([0, 2, 0, 1])
plt.ylabel('$\phi/\pi$', size='large')
plt.xlabel('$\omega/\omega_0$', size='large')

# Generate slider
axcolor = 'lightgoldenrodyellow'
axnu    = plt.axes([0.20, 0.15, 0.65, 0.03], axisbg=axcolor)
snu     = Slider(axnu, r'$\nu/\omega_0$', 0., 0.5, valinit=nu0)

# Update plot using slider data
def update(val):
    nu  = snu.val
    l.set_ydata(np.arctan2(nu*w,1.-w*w)/np.pi)
    fig.canvas.draw_idle()
snu.on_changed(update)

# Generate reset button
resetax = plt.axes([0.8, 0.02, 0.1, 0.04])
button  = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    snu.reset()
button.on_clicked(reset)

plt.show()

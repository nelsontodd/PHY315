# Author: Richard Fitzpatrick
# Modified from  http://matplotlib.org/examples/widgets/slider_demo.py
# Requires numpy and matplotlib

"""
Widget to illustrate solution of damped simple harmonic oscillator equation.
Shows how solution 

 x(t) = exp(-pi*nu*t)*cos(2*pi*sqrt(1-nu*nu/4)*t)

depends on choice of normalized damping rate, nu = nu/omega_0. Here,
x = x/a, t = t/T_0, T_0 is undamped oscillation period, and omega_0
is corresponding angular frequency.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Generate initial plot
t   = np.arange(0.0, 10.0, 0.001)
nu0 = 0.05
s   = np.exp(-np.pi*nu0*t)*np.cos(2*np.pi*np.sqrt(1.-nu0*nu0/4.)*t)
gp  =    np.exp(-np.pi*nu0*t)
gm  = -  np.exp(-np.pi*nu0*t)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.20, bottom=0.30)
l,  = plt.plot(t, s,  lw=2, color='red')
lp, = plt.plot(t, gp, lw=1, color='blue', ls='dotted')
lm, = plt.plot(t, gm, lw=1, color='blue', ls='dotted')
plt.axhline(y=0., lw=2, color='blue', ls='dotted')
plt.axis([0, 10, -1., 1.])
plt.xlabel('$t/T_0$', size='large')
plt.ylabel('$x/a$', size='large')
plt.title(r'$x = a\exp(-\nu\,t/2)\,\cos (\sqrt{\omega_0^{\,2}-\nu^{\,2}/4}\, t)$', size='large')

# Generate slider
axcolor = 'lightgoldenrodyellow'
axnu    = plt.axes([0.20, 0.15, 0.65, 0.03], axisbg=axcolor)
snu     = Slider(axnu, r'$\nu/\omega_0$', 0., 0.5, valinit=nu0)

# Update plot using slider data
def update(val):
    nu  = snu.val
    l.set_ydata(np.exp(-np.pi*nu*t)*np.cos(2*np.pi*np.sqrt(1.-nu*nu/4.)*t))
    lp.set_ydata(np.exp(-np.pi*nu*t))
    lm.set_ydata(-np.exp(-np.pi*nu*t))
    fig.canvas.draw_idle()
snu.on_changed(update)

# Generate reset button
resetax = plt.axes([0.8, 0.02, 0.1, 0.04])
button  = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    snu.reset()
button.on_clicked(reset)

plt.show()

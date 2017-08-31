# Author: Richard Fitzpatrick
# Modified from  http://matplotlib.org/examples/widgets/slider_demo.py
# Requires numpy and matplotlib

"""
Widget to illustrate how transients affect solution
to damped driven harmonic oscillator equation. Solution
such that initial displacement and velocity both zero
and frequency is relatively close to resonant frequency. 
Solution is

x(t) = [2*(1-w)/4*(1-w)*(1-w)+nu*nu]*[cos(2*pi*w*t)-exp(-pi*nu*t)*cos(2*pi*t)]
     + [nu/4*(1-w)*(1-w)+nu*nu]*[sin(2*pi*w*t)-exp(-pi*nu*t)*sin(2*pi*t)]

where x = x_0/X_0, t=t/T_0, w = omega/omega_0, and nu = nu/omega_0. Here, T_0
is undamped oscillation period, and omega_0 is associated angular frequency.
Quality factor Q = 1/nu. w and nu are both adjustable. 
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Generate initial plot
t   = np.arange(0.0, 25., 0.001)
w0  = 1.0
nu0 = 0.1
ym  = 20.

amp = 4.*(1.-w0)*(1.-w0) + nu0*nu0
amp = 1./amp
x   = 2.*(1.-w0)*(np.cos(2.*np.pi*w0*t) - np.exp(-np.pi*nu0*t)*np.cos(2.*np.pi*t))
x  += nu0*(np.sin(2.*np.pi*w0*t) - np.exp(-np.pi*nu0*t)*np.sin(2.*np.pi*t))
x  *= amp
z   = np.zeros_like(t)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.20, bottom=0.30)
l,  = plt.plot(t, x, lw=2, color='red')
l1, = plt.plot(t, z, lw=1, color='blue', ls='dashed')
plt.axis([0, 25, -ym, ym])
plt.xlabel('$t/T_0$', size='large')
plt.ylabel('$x/X_0$', size='large')

# Generate sliders
axcolor = 'lightgoldenrodyellow'
axw     = plt.axes([0.20, 0.15, 0.65, 0.03], axisbg=axcolor)
axnu    = plt.axes([0.20, 0.10, 0.65, 0.03], axisbg=axcolor)
sw      = Slider(axw,  '$\omega/\omega_0$', 0.,    5.0, valinit=w0)
snu     = Slider(axnu, r'$\nu/\omega_0$',   1.e-6, 0.5, valinit=nu0)

# Update plot using slider data
def update(val):
    w   = sw.val
    nu  = snu.val
    
    amp = 4.*(1.-w)*(1.-w) + nu*nu
    amp = 1./amp
    x   = 2.*(1.-w)*(np.cos(2.*np.pi*w*t) - np.exp(-np.pi*nu*t)*np.cos(2.*np.pi*t))
    x  += nu*(np.sin(2.*np.pi*w*t) - np.exp(-np.pi*nu*t)*np.sin(2.*np.pi*t))
    x  *= amp

    ymax = np.max(x)
    if ymax > ym or ymax < ym/2.:
        ax.set_ylim(-1.5*ymax, 1.5*ymax)
        ax.figure.canvas.draw()
    
    l.set_ydata(x)
    fig.canvas.draw_idle()

sw.on_changed(update)
snu.on_changed(update)

# Generate reset button
resetax = plt.axes([0.8, 0.02, 0.1, 0.04])
button  = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sw.reset()
    snu.reset()

button.on_clicked(reset)

# Show graph
plt.show()

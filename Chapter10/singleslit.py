# Author: Richard Fitzpatrick
# Modified from  http://matplotlib.org/examples/widgets/slider_demo.py
# Requires numpy and matplotlib

"""
Widget to illustrate single-slit, far-field, interference 
due to monochromatic light source of negligible angular extent.
Plots intensity of light versus angle as function
of delta/lambda where delta is slit width,
and lambda is wavelength.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Generate initial plot
t   = np.arange(-0.5,0.5,0.0001)
dd0 = 1.
F1  = np.sinc(dd0*np.sin(t*np.pi))
I   = F1*F1

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.20, bottom=0.30)
l,  = plt.plot(t, I, lw=2, color='red')
l1, = plt.plot([0.,0.], [0.,1.1], lw=2, color='blue', ls='dotted')
plt.axis([-0.5, 0.5, 0., 1.1])
plt.xlabel(r'$\theta/\pi$', size='large')
plt.ylabel('$I$', size='large')

# Generate slider
axcolor = 'lightgoldenrodyellow'
axd     = plt.axes([0.20, 0.15, 0.65, 0.03], axisbg=axcolor)
sdd     = Slider(axd, r'$\delta/\lambda$', 0., 10., valinit=dd0)

# Update plot using slider data
def update(val):
    dd = sdd.val
    F1 = np.sinc(dd*np.sin(t*np.pi))
    l.set_ydata(F1*F1)
    fig.canvas.draw_idle()
sdd.on_changed(update)

# Generate reset button
resetax = plt.axes([0.8, 0.02, 0.1, 0.04])
button  = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sdd.reset()
button.on_clicked(reset)

plt.show()

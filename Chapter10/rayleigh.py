# Author: Richard Fitzpatrick
# Modified from  http://matplotlib.org/examples/widgets/slider_demo.py
# Requires numpy, matplotlib, and scipy

"""
Widget to illustrate Rayleigh criterion for resolving
power of telescope. Plots intensity versus angle in
one dimension as a function of Delta_theta where Delta_theta is
angular distance between two neighboring stars.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import scipy.special as sp

# Generate initial plot
dd0 = 1.22
tt  = np.arange(-8.,8.,0.01)
I   = []
for t in tt:
    F1 = sp.j0(np.pi*(t-dd0/2.)) + sp.jn(2,np.pi*(t-dd0/2.))
    F2 = sp.j0(np.pi*(t+dd0/2.)) + sp.jn(2,np.pi*(t+dd0/2.))
    I.append(F1*F1+F2*F2)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.20, bottom=0.30)
l, = plt.plot(tt, I, lw=2, color='red')
plt.axis([-8., 8., 0., 2.1])
plt.xlabel(r'$D\,\theta/\lambda$', size='large')
plt.ylabel('$I$', size='large')

# Generate slider
axcolor = 'lightgoldenrodyellow'
axd     = plt.axes([0.20, 0.15, 0.65, 0.03], axisbg=axcolor)
sdd     = Slider(axd, r'$D\,\Delta\theta/\lambda$', 0., 8., valinit=dd0)

# Update plot using slider data
def update(val):
    dd = sdd.val
    II  = []
    for t in tt:
        F1 =  sp.j0(np.pi*(t-dd/2.)) + sp.jn(2,np.pi*(t-dd/2.))
        F2 = sp.j0(np.pi*(t+dd/2.)) + sp.jn(2,np.pi*(t+dd/2.))
        II.append(F1*F1+F2*F2)
    l.set_ydata(II)
    fig.canvas.draw_idle()
sdd.on_changed(update)

# Generate reset button
resetax = plt.axes([0.8, 0.02, 0.1, 0.04])
button  = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sdd.reset()
button.on_clicked(reset)

plt.show()

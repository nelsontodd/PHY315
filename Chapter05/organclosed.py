# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Animation to illustate first three normal modes of organ pipe closed at both ends.
Plots pressure. Anti-nodes indicated as dashed lines. Nodes indicated as dotted lines.
Animation freezes on mouse clicks.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors, cm

# Setup plotting space
fig = plt.figure(figsize=(14.,6.))
ax1 = plt.subplot2grid((9,9),(0,1),rowspan=9)
ax2 = plt.subplot2grid((9,9),(0,4),colspan=9)
ax3 = plt.subplot2grid((9,9),(0,7),colspan=9)

# Function to capture mouse clicks
pause = 0
def onClick(event):
    global pause

    if pause == 0:
        pause = 1
    else:
        pause = 0

# Animation function
dt = 0.1
counter = 0.
def animate(i):
    global counter, pause
    ax2.clear()

    #
    # First mode
    #
    plt.subplot2grid((9,9),(0,1), rowspan=9)
    plt.title (r"n = 1", size='large')
    cur_axes = plt.gca()
    cur_axes.axes.get_yaxis().set_visible(False)
    cur_axes.axes.get_xaxis().set_visible(False)
    
    N = 500
    x = np.linspace(0., 1., N)
    y = np.linspace(0., 1., N)
     
    X, Y = np.meshgrid(x, y)

    n = 1.
    F = np.cos(n*np.pi*Y)*np.cos(n*counter)
    plt.axhline(y=1./2., lw=3, color='black', ls='dotted')

    levels = np.arange(-1.1,1.1,0.1)

    plt.contourf(X, Y, F, levels, cmap=cm.bwr)

    plt.plot((0,0,1,1,0),(1,0,0,1,1), color="black", lw=10)

    #
    # Second mode
    #
    plt.subplot2grid((9,9),(0,4),rowspan=9)
    plt.title (r"n = 2", size='large')
    cur_axes = plt.gca()
    cur_axes.axes.get_yaxis().set_visible(False)
    cur_axes.axes.get_xaxis().set_visible(False)

    n = 2.
    F = np.cos(n*np.pi*Y)*np.cos(n*counter)

    plt.contourf(X, Y, F, levels, cmap=cm.bwr)
    plt.axhline(y=1./4., lw=3, color='black', ls='dotted')
    plt.axhline(y=2./4., lw=2, color='black', ls='dashed')
    plt.axhline(y=3./4., lw=3, color='black', ls='dotted')

    plt.plot((0,0,1,1,0),(1,0,0,1,1), color="black", lw=10)

    #
    # Third mode
    #
    plt.subplot2grid((9,9),(0,7),rowspan=9)
    plt.title (r"n = 3", size='large')
    cur_axes = plt.gca()
    cur_axes.axes.get_yaxis().set_visible(False)
    cur_axes.axes.get_xaxis().set_visible(False)

    n = 3.
    F = np.cos(n*np.pi*Y)*np.cos(n*counter)

    plt.contourf(X, Y, F, levels, cmap=cm.bwr)

    plt.plot((0,0,1,1,0),(1,0,0,1,1), color="black", lw=10)
    plt.axhline(y=1./6., lw=3, color='black', ls='dotted')
    plt.axhline(y=2./6., lw=2, color='black', ls='dashed')
    plt.axhline(y=3./6., lw=3, color='black', ls='dotted')
    plt.axhline(y=4./6., lw=2, color='black', ls='dashed')
    plt.axhline(y=5./6., lw=3, color='black', ls='dotted')
    
    #
    # Freeze animation on mouse clicks
    #
    if not pause:
        counter += dt
        
fig.canvas.mpl_connect('button_press_event', onClick)
ani = animation.FuncAnimation(fig, animate, interval=2)
plt.show()



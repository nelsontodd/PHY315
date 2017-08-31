# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Animation to illustrate counterpropagating wavepulses.
Pauses on mouse click.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to capture mouse clicks
pause = 0
def onClick(event):
    global pause

    if pause == 0:
        pause = 1
    else:
        pause = 0
        
# Setup plotting space
fig = plt.figure(figsize=(7,3.5))
ax1 = fig.add_subplot(1,1,1)

# Produce animation
counter = -10.

def animate(i):
    global counter, pause
    ax1.clear()

    # Generate animation plot
    A = 8.
    plt.xlim(-10, 10)
    plt.ylim(0., 2.)
    plt.xlabel(r"$x$", size='large')

    xx = np.arange(-10.,10.,0.01)
    yy = []

    for x in xx:
        if np.abs(x-counter) < 0.5 and np.abs(x+counter) < 0.5:
            yy.append(1. - 2.*np.abs(counter-x) + 1.)
        elif np.abs(x-counter) < 0.5:  
            yy.append(1. - 2.*np.abs(counter-x))
        elif np.abs(x+counter) < 0.5:
            yy.append(1.)
        else:
            yy.append(0.)
            
    plt.plot(xx, yy, color="blue", lw=3)    

    dt = 0.1
    if not pause:
        counter += dt

    if counter > 12.:
        counter = -12.

fig.canvas.mpl_connect('button_press_event', onClick)        
ani = animation.FuncAnimation(fig,animate,interval=2)

plt.show()

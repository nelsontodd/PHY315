# Author: Richard Fitzpatrick
# Adapted from http://firsttimeprogrammer.blogspot.com/2014/12/basic-physics-and-python-simple.html
# Requires numpy and matplotlib

"""
Animation to illustrate relationship between simple harmonic and circular motion. 
Animation freezes on mouse clicks.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse
 
# Set simulation parameters:
#   counter - current time
#   tt      - time array
#   xx      - coordinate of center of mass array

counter =  0
tt      = [0]
xx      = [0]

# Setup plotting space
fig = plt.figure(figsize=(14.,6.))
ax1 = fig.add_subplot(1,1,1)
ax2 = fig.add_subplot(1,2,1)
fig.subplots_adjust(hspace=.45)

# Function to capture mouse clicks
pause = 0
def onClick(event):
    global pause

    if pause == 0:
        pause = 1
    else:
        pause = 0

# Animation function
def animate(i):
    global counter, tt, xx, A, pause
    ax2.clear()

    #
    # Generate circular motion plot
    #
    plt.subplot(121)
    plt.xlim(-1.2, 1.2)
    plt.ylim(-1.2, 1.2)
    plt.xlabel("$x/a$", size="large")
    plt.ylabel("$y/a$", size="large")
    plt.title(R"Polar coordinates: $r=a$, $\theta=\omega\,t-\phi$", size="large")

    # Plot circle
    th = np.arange(0.,2.*np.pi,0.01)
    xc = np.cos(th)
    yc = np.sin(th)
    plt.plot(xc, yc, color="blue", lw=2, ls="dotted")
    
    # Plot mass
    data_x = [np.cos(counter*2.*np.pi)]
    data_y = [np.sin(counter*2.*np.pi)]
    o_x = [0.]
    o_y = [0.]
    plt.plot(data_x, data_y, 'o', color="black", markersize='10')
    plt.plot([o_x,data_x], [o_y,data_y], color="blue", lw=2, ls="solid")
    plt.axhline(y=0., lw=1, color='black', ls='dotted')
    plt.axvline(x=0., lw=1, color='black', ls='dotted')

    # Plot projected mass
    data_xx = data_x
    data_yy = [0.]
    plt.plot(data_xx, data_yy, 'o', color="red", markersize='10', fillstyle='none')
    plt.plot([data_x,data_xx], [data_y,data_yy], color="red", lw=2, ls="dotted")

    #
    # Generate x plot
    #
    plt.subplot(122)
    tt.append(counter)
    xx.append(np.cos(counter*2.*np.pi))
    plt.ylabel("$x/a$", size="large")
    plt.xlabel("$t/T$", size="large")
    plt.title("Cartesian coordinates: $x = a\,\cos(\omega\,t-\phi)$, $y = a\,\cos(\omega\,t-\phi)$")
    plt.xlim(0,5)
    plt.ylim(-1.2, 1.2)
    plt.plot(tt, xx,   lw=1, color="red")
    plt.axhline(y=0.,  lw=1, color='black', ls='dotted')
    plt.axhline(y=-1., lw=1, color='black', ls='dotted')
   
    #
    # Freeze animation on mouse clicks
    #
    dt = 0.02
    if not pause:
        counter += dt
        
fig.canvas.mpl_connect('button_press_event', onClick)
ani = animation.FuncAnimation(fig, animate, interval=2)
plt.show()



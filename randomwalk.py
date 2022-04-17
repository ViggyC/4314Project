from turtle import *
import random
import numpy as np
from scipy.stats import levy_stable
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
line, = ax.plot(0,0)
x = 0
y = 0

x_data=[]
y_data=[]



def animate_rw(i):

    n = 1000         #steps
    alpha = 1       #tuning parameter
    beta = 0      #tuning parameter
    steps = levy_stable.rvs(alpha=alpha, beta=beta, size=n)
    maxstep = 75
    minstep = 5
    for i in range(n):

        if steps[i] > maxstep:
            step = maxstep
        elif abs(steps[i]) < minstep:
            step = minstep
        else:
            step = steps[i]

            
    global x 
    global y
    

    direction = random.randint(1, 4)
    if direction == 1:
        x += 1
    elif direction == 2:
        y += 1
    elif direction == 3:
        x += -1
    elif direction == 4:
        y += -1

    x_data.append(x)
    y_data.append(y)

    line.set_xdata(x_data)
    line.set_ydata(y_data)

    return line,
# Did not write in anything for frames, since it defaults to passing itertools.count
anim = FuncAnimation(fig, animate_rw, interval=600)
plt.show()
# Define parameters for the walk
from importlib.resources import path
from turtle import *
import seaborn as sns
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import levy_stable
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(3,5),dpi=200)

def animate(i):
    dims = 3
    step_n = 1000
    step_set = [-1, 0, 1]
    origin = np.zeros((1,dims))
    # Simulate steps in 3D
    step_shape = (step_n,dims)
    steps = np.random.choice(a=step_set, size=step_shape)
    path = np.concatenate([origin, steps]).cumsum(0)
    start = path[:1]
    stop = path[-1:]
    # Plot the path
    ax = fig.add_subplot(111, projection='3d')
    ax.grid(False)
    ax.xaxis.pane.fill = ax.yaxis.pane.fill = ax.zaxis.pane.fill = False
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # ax.set_xlim([0,0])
    # ax.set_ylim([0,5])
    ax.scatter3D(path[:,0], path[:,1], path[:,2], 
                c='blue', alpha=0.25,s=1)
    ax.plot3D(path[:,0], path[:,1], path[:,2], 
            c='blue', alpha=0.5, lw=0.5)
    ax.plot3D(start[:,0], start[:,1], start[:,2], 
            c='red', marker='+')
    ax.plot3D(stop[:,0], stop[:,1], stop[:,2], 
            c='black', marker='o')

plt.title('3D Random Walk')
ani = FuncAnimation(fig, animate, frames=20, interval=500, repeat=True)

plt.show()
#plt.savefig('plots/random_walk_3d.png',dpi=250)
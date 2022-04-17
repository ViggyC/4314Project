from importlib.resources import path
from turtle import *
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import levy_stable


class patch:

    center = (50,50)
    n = np.random.randint(0,10)

   

    step = [0,1,-1]
    

    p = np.zeros([1, 100])
  
    seascape = np.zeros([5000,2500])
    # plt.imshow(seascape, interpolation='none')
    fig = plt.figure(figsize=(8,8),dpi=200)
    ax = fig.add_subplot(111)
    ax.scatter(path[:,0], path[:,1],c='blue',alpha=0.25,s=0.05);
    ax.plot(path[:,0], path[:,1],c='blue',alpha=0.5,lw=0.25,ls=' — ');
    ax.plot(start[:,0], start[:,1],c='red', marker='+')
    ax.plot(stop[:,0], stop[:,1],c='black', marker='o')
    plt.title('2D Random Walk')
    plt.tight_layout(pad=0)
    plt.savefig('plots/random_walk_2d.png',dpi=250);


 




sim = patch()

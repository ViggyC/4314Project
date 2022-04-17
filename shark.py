from turtle import *
import random
import numpy as np
from scipy.stats import levy_stable

class shark:

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos


    def draw(self):
        turtle = Turtle()
        tp = turtle.position()
        
        n = 1000         #steps
        alpha = 2     #tuning parameter
        beta = 0      #tuning parameter
        steps = levy_stable.rvs(alpha=alpha, beta=beta, size=n)
        maxstep = 100
        minstep = 30

        #getscreen()
        for i in range(n):

            if steps[i] > maxstep:
                step = maxstep
            elif abs(steps[i]) < minstep:
                step = minstep
            else:
                step = steps[i]

            turtle.right(random.randint(0,360))
            turtle.forward(step)




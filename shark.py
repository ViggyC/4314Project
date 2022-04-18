from turtle import *
from turtle import Screen
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
        minstep = 1
        step = -1
        #print(steps)
        #getscreen()
        for i in range(n):

            r = np.random.choice(steps)
     
            if r > maxstep:
                step = maxstep
            elif abs(r) < minstep:
                step = minstep*3
            else:
                scale = np.random.randint(25,50)
                prob = np.random.randint(0, 100)
                if prob <5:
                    step *= scale

     
            turtle.right(random.randint(0,360))
            turtle.forward(step)

            x_flag = abs(turtle.xcor()) > 300
            y_flag = abs(turtle.ycor()) > 300

            if x_flag or y_flag:
              

                x, y = turtle.position()

   
                turtle.setposition(0 if x_flag else x, 0 if y_flag else y)
    

            
           




##################2D - Model of Basking Shark Levy Walk ################
from turtle import *
import random
import numpy as np
from scipy.stats import levy_stable

#TODO:  keep turtle within constraints 
#       figure out alpha/beta 


turtle = Turtle()
tp = turtle.position()
n = 1000         #steps
alpha = 1       #tuning parameter
beta = 0      #tuning parameter
steps = levy_stable.rvs(alpha=alpha, beta=beta, size=n)
maxstep = 75
minstep = 5
getscreen()
for i in range(n):

    if steps[i] > maxstep:
        step = maxstep
    elif abs(steps[i]) < minstep:
        step = minstep
    else:
        step = steps[i]

    turtle.right(random.randint(0,360))
    turtle.forward(step)


'''
color('red', 'yellow')
turtle = Turtle()
tp = turtle.position()

getscreen()

i = 0
#begin_fill()
while i<5:
    turtle.right(90)
    #turtle.right(random.randint(0,360))
    distance = random.randint(25,100)
    # r = random.randint(0,100)
    # if r<1:
    #     distance = random.randint(25,100)
    # else:
    #     distance = 2
    turtle.forward(20)
    #turtle.forward(distance)
    
    
    i += 1

#end_fill()
done()
'''
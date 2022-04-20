from turtle import *
import turtle
import random
import numpy as np
from scipy.stats import levy_stable
import matplotlib.patches as patches
import matplotlib.pyplot as plt

class Patch():

        # import package and making object
    

    def draw(self, x, y):
        req_area = (100**2)
        big_l = int(req_area**.5)
        tr = Turtle()
        tr.penup()
        steps = levy_stable.rvs(alpha=1, beta=0, size=(big_l,2))
        #patch_location = np.random.choice(steps)
        print(steps[0])
        tr.goto(x,y)
        tr.pendown()
        tr.fillcolor('orange')
        tr.begin_fill()
        tr.shape("circle")
        tr.end_fill()
 

    
    

   

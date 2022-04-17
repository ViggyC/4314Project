from turtle import *
import random
import numpy as np
from scipy.stats import levy_stable
import matplotlib.patches as patches
import matplotlib.pyplot as plt

class Patch():

    def __init__(self, start_pos):
     
        # import package and making object
        self.start_pos = start_pos


    def draw(self, space,x, start_pos):
        for i in range(x):
            for j in range(x):
                
                # dot
                pen.dot()
                
                # distance for another dot
                pen.forward(space)
            pen.backward(space*x)
            
            # direction
            pen.right(90)
            pen.forward(space)
            pen.left(90)

        # Main Section
        pen.penup()
    

   

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
        tr = Turtle()
        tr.setpos((x,y))
        tr.pendown()
        tr.goto(x,y)
        tr.fillcolor('orange')
        tr.begin_fill()
        tr.shape("circle")
        tr.end_fill()
        turtle.done()

    
    

   

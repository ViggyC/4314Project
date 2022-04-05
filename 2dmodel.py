##################2D - Model of Basking Shark Levy Walk ################
from turtle import *
import random
import numpy as np
color('red', 'yellow')
turtle = Turtle()
tp = turtle.position()

begin_fill()
while True:
    turtle.right(random.randint(0,360))
    distance = random.randint(25,100)
    # r = random.randint(0,100)
    # if r<1:
    #     distance = random.randint(25,100)
    # else:
    #     distance = 2


    turtle.forward(distance)

end_fill()
done()
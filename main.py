from turtle import Screen
from patch import Patch
from shark import shark
import time


screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("cyan")


s = shark(0,0)
prey = Patch()


sim_on = True
while sim_on:
    screen.update()
    time.sleep(0.1)
    #prey.draw(-100,0)
    s.draw()
    
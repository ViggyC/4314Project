from turtle import Screen
from patch import Patch
from shark import shark


screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("cyan")


s = shark(0,0)
s.draw()
# # ##################2D - Model of Basking Shark Levy Walk ################
# # from turtle import *
# # import random
# # import numpy as np
# # color('red', 'yellow')
# # shark = Turtle()
# # shark_pos = shark.position()

# # begin_fill()
# # while True:
# #     shark.right(random.randint(0,360))
# #     distance = random.randint(25,100)
# #     r = random.randint(0,100)
# #     if r<1:
# #         distance = random.randint(25,100)
# #     else:
# #         distance += 2


# #     shark.forward(distance)

# # end_fill()
# # done()
# import turtle
# import random
# import math

# turtle.setup(1000,1000)
# turtle.title("Levy Walk")
# shark = turtle.Turtle()



# shark.color('blue')


# tlist = []
# tlist.append(shark)


# turtle.tracer(0)
# turtle.hideturtle()
# sum = 0
# count = 0
# for j in range(100):  
#     for i in range(10000):
#         for t in tlist:
#             t.seth(random.randrange(0,360,90))
#             t.fd(10)
#         #turtle.update()
#     for t in tlist:
#         sum += math.sqrt(t.xcor()*t.xcor() + t.ycor()*t.ycor())/10*2*math.sqrt(t.xcor()*t.xcor() + t.ycor()*t.ycor())/10*2/100
#         count += 1
#     for t in tlist:
#         t.clear()
#         t.up()
#         t.goto(0,0)
#         t.down()
#     print(sum/count)

##################2D - Model of Basking Shark Levy Walk ################
from turtle import *
import random
import numpy as np
from scipy.stats import levy_stable
import matplotlib as plt

#TODO:  keep turtle within constraints 
#       figure out alpha/beta 


# turtle = Turtle()
# tp = turtle.position()
# n = 1000         #steps
# alpha = 1       #tuning parameter
# beta = 0      #tuning parameter
# steps = levy_stable.rvs(alpha=alpha, beta=beta, size=n)
# maxstep = 75
# minstep = 5
# getscreen()
# for i in range(n):
#     if steps[i] > maxstep:
#         step = maxstep
#     elif abs(steps[i]) < minstep:
#         step = minstep
#     else:
#         step = steps[i]

#     turtle.right(random.randint(0,360))
#     turtle.forward(step)
#     #TODO: Get plankton in area that the shark has passed through and add reward of some kind



# color('red', 'yellow')
# turtle = Turtle()
# tp = turtle.position()
# getscreen()
# i = 0
# #begin_fill()
# while i<5:
#     turtle.right(90)
#     #turtle.right(random.randint(0,360))
#     distance = random.randint(25,100)
#     # r = random.randint(0,100)
#     # if r<1:
#     #     distance = random.randint(25,100)
#     # else:
#     #     distance = 2
#     turtle.forward(20)
#     #turtle.forward(distance)
    
    
#     i += 1
# #end_fill()
# done()

def generate_patch(patch_length):
    patch = np.zeros((patch_length,patch_length))
    maxstep = 5
    minstep = 1
    req_area = (patch_length**2)
    big_l = int(req_area**.5)
    pos=(50,50)
    hit = 0
    while(hit < req_area):
        l = big_l
        steps = levy_stable.rvs(alpha=1, beta=0, size=(big_l,2))
        for i in range(big_l):
            #print(steps[i])
            if abs(steps[i][0]) > maxstep:
                stepx = maxstep
            elif abs(steps[i][0]) < minstep:
                stepx = minstep
            else:
                stepx = steps[i][0]
            if abs(steps[i][1]) > maxstep:
                stepy = maxstep
            elif abs(steps[i][1]) < minstep:
                stepy = minstep
            else:
                stepy = steps[i][1]
            newposy = int(pos[0] + stepy)
            newposx = int(pos[1] + stepx)
            if(newposy >= 100):
                newposy = newposy - 100
            elif(newposy < 0):
                newposy = newposy + 100
            if(newposx >= 100):
                newposx = newposx - 100
            elif(newposx < 0):
                newposx = newposx + 100
            pos = (newposy, newposx)
            if(patch[pos[0]][pos[1]] == 0):
                patch[pos[0]][pos[1]] = l
                hit += 1
            l -= 1
    return patch

# plt.figure()
patch = generate_patch(100)
print(patch)
# plt.plot(patch)



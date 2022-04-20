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
import matplotlib.pyplot as plt

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

def create_seascape_uniform(patch_length, patch_count, seascape_length, seascape_width):
    if(seascape_length % patch_length != 0 or seascape_width % patch_length !=0):
        raise Exception("Seascape length and width must both be dividable by patch length")
    seascape = np.zeros((seascape_length, seascape_width))
    i = 0
    x = random.randint(0, seascape_width-100)
    y = random.randint(0, seascape_length-100)
    while(i < patch_count):
        patch = generate_patch(100)
        #print(patch.shape, x, y)
        y2 = 0
        for y1 in range(y, y + patch_length): #This is to replace the values with the values generated from the patch generator
            x2 = 0
            for x1 in range(x, x+patch_length):
                if(x1 >= seascape_width): #Torus properties
                    x1 -= seascape_width
                if(y1 >= seascape_length):
                    y1 -= seascape_length
                seascape[y1][x1] = seascape[y1][x1] + patch[y2][x2] #Update cell value
                x2+=1
            y2+=1
        stepx = random.randint(0, seascape_width-100)
        stepy = random.randint(0, seascape_length-100)
        newposy = int(y + stepy)
        newposx = int(x + stepx)
        if(newposy >= seascape_length - 1):
            newposy = newposy - seascape_length - 1
        if(newposy < 0):
            newposy = newposy + seascape_length - 1
        if(newposx >= seascape_width - 1):
            newposx = newposx - seascape_width - 1
        if(newposx < 0):
            newposx = newposx + seascape_width - 1
        y = newposy
        x = newposx
        i += 1
        #print(seascape)
    return seascape

def create_seascape_levy(patch_length, patch_count, seascape_length, seascape_width):
    if(seascape_length % patch_length != 0 or seascape_width % patch_length !=0):
        raise Exception("Seascape length and width must both be dividable by patch length")
    seascape = np.zeros((seascape_length, seascape_width))
    i = 0
    x = random.randint(0, seascape_width-1)
    y = random.randint(0, seascape_length-1)
    a = np.array(np.concatenate((range(-2500,-50), range(50,2500)))) #concat range of min and max values + and -
    prob = levy.levy(a, 1, 0, mu=2) #get probability distribution for walk
    xsteps = [random.choices(a, weights=prob) for x in range(patch_count)]
    ysteps = [random.choices(a, weights=prob) for x in range(patch_count)]
    while(i < patch_count):
        patch = generate_patch(patch_length)
        print(patch.shape, x, y)
        y2 = 0
        for y1 in range(y, y + patch_length): #This is to replace the values with the values generated from the patch generator
            x2 = 0
            for x1 in range(x, x+patch_length):
                if(x1 >= seascape_width): #Torus properties
                    x1 -= seascape_width
                if(y1 >= seascape_length):
                    y1 -= seascape_length
                seascape[y1][x1] = seascape[y1][x1] + patch[y2][x2] #Update cell value
                x2+=1
            y2+=1
        stepx = xsteps[i][0]
        stepy = ysteps[i][0]
        newposy = int(y + stepy)
        newposx = int(x + stepx)
        if(newposy >= seascape_length - 1):
            newposy = newposy - seascape_length - 1
        if(newposy < 0):
            newposy = newposy + seascape_length - 1
        if(newposx >= seascape_width - 1):
            newposx = newposx - seascape_width - 1
        if(newposx < 0):
            newposx = newposx + seascape_width - 1
        y = newposy
        x = newposx
        i += 1
        #print(seascape)
    return seascape
    
def generate_patch(patch_length):
    patch = np.zeros((patch_length,patch_length))
    req_area = (patch_length**2)
    big_l = int(req_area**.5)
    hit = 0
    while(hit < req_area):
        pos=(50,50)
        l = big_l
        a = np.array(np.concatenate((range(int(-patch_length/4),0), range(0,int(patch_length/4))))) #concat range of min and max values + and -
        prob = scipy.stats.norm(0, 7).pdf(np.concatenate((range(int(-patch_length/4),0), range(0,int(patch_length/4))))) #get probability distribution for walk
        xsteps = [random.choices(a, weights=prob) for x in range(big_l)] #get x displacement
        ysteps = [random.choices(a, weights=prob) for y in range(big_l)] #get y displacement
        for i in range(big_l):
            newposy = int(pos[0] + ysteps[i][0])
            newposx = int(pos[1] + xsteps[i][0])
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


def create_seascape(patch_length, patch_count, seascape_length, seascape_width):
    if(seascape_length % patch_length != 0 or seascape_width % patch_length !=0):
        raise Exception("Seascape length and width must both be dividable by patch length")
    seascape = np.zeros((seascape_length, seascape_width))
    i = 0
    x = 0
    y = 0
#     minstep = 1
#     maxstep = 500
#     steps = levy_stable.rvs(alpha=1, beta=0, size=(patch_count,2))
    while(i < patch_count):
        patch = generate_patch(100)
        #print(patch.shape, x, y)
        y2 = 0
        for y1 in range(y, y + patch_length):
            x2 = 0
            for x1 in range(x, x+patch_length):
                if(x1 >= seascape_width):
                    x1 -= seascape_width
                if(y1 >= seascape_length):
                    y1 -= seascape_length
                seascape[y1][x1] = seascape[y1][x1] + patch[y2][x2]
                x2+=1
            y2+=1
        x = random.randint(0, seascape_width-100)
        y = random.randint(0, seascape_length-100)
        i += 1
#         if abs(steps[i][0]) > maxstep:
#             stepx = math.copysign(maxstep, steps[i][0])
#         elif abs(steps[i][0]) < minstep:
#             stepx = math.copysign(minstep, steps[i][0])
#         else:
#             stepx = steps[i][0]
#         if abs(steps[i][1]) > maxstep:
#             stepy = math.copysign(maxstep, steps[i][1])
#         elif abs(steps[i][1]) < minstep:
#             stepy = math.copysign(minstep, steps[i][1])
#         else:
#             stepy = steps[i][1]
#         newposy = int(y + stepy)
#         newposx = int(x + stepx)
#         if(newposy >= 4900):
#             newposy = newposy - 4900
#         elif(newposy < 0):
#             newposy = newposy + 4900
#         if(newposx >= 2400):
#             newposx = newposx - 2400
#         elif(newposx < 0):
#             newposx = newposx + 2400
#         y = newposy + patch.shape[1]
#         x = newposx + patch.shape[0]
        #print(seascape)
    return seascape

sea = create_seascape(100,4, 5000,2500)
plt.plot(sea)
plt.show()
print(sea)


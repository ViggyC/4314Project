from turtle import *
import random
import numpy as np
from scipy.stats import levy_stable
import matplotlib.patches as patches
import matplotlib.pyplot as plt

def seascape():
    grid = np.zeros((5000,2500))

    return grid

path = []
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
        path.append(steps)
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

fig, ax = plt.subplots(1, 1)
alpha, beta = 1.8, -0.5
mean, var, skew, kurt = levy_stable.stats(alpha, beta, moments='mvsk')

# x = np.linspace(levy_stable.ppf(0.01, alpha, beta),
#                 levy_stable.ppf(0.99, alpha, beta), 100)
# ax.plot(x, levy_stable.pdf(x, alpha, beta),
#        'r-', lw=5, alpha=0.6, label='levy_stable pdf')

patch = generate_patch(100)
print(path)
plt.plot(path)
plt.show()

# sea = seascape()
# #ax.add_patch(patches.Polygon(patch))
# ax.plot(patch)
# ax.plot(sea)



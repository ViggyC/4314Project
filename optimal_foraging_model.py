import numpy as np
from scipy.stats import levy_stable
import scipy
import math
import random
import levy
from matplotlib import pyplot

def create_seascape_uniform(patch_length, patch_count, seascape_length, seascape_width):
 
    if(seascape_length % patch_length != 0 or seascape_width % patch_length !=0):
        raise Exception("Seascape length and width must both be dividable by patch length")
    seascape = np.zeros((seascape_length, seascape_width))
    i = 0
    x = random.randint(0, seascape_width-100) #Initial patch placements
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
        ang = random.randint(-360,360)
        step = np.random.uniform(low=-seascape_length, high=seascape_length)
        xstep = int(step * math.cos(math.radians(ang)))
        ystep = int(step * math.sin(math.radians(ang)))
        newposy = int(y + ystep)
        newposx = int(x + xstep)
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
    a = np.array(np.concatenate((range(-2500,-100), range(100,2500)))) #concat range of min and max values + and -
    prob = levy.levy(a, 1, 0) #get probability distribution for walk
    steps = [random.choices(a, weights=prob) for x in range(patch_count)]
    while(i < patch_count):
        patch = generate_patch(patch_length)
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
        ang = random.randint(-360,360)
        xstep = int(steps[i][0] * math.cos(math.radians(ang)))
        ystep = int(steps[i][0] * math.sin(math.radians(ang)))
        newposy = int(y + ystep)
        newposx = int(x + xstep)
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
        
def reward(levy_sea, walk):
    pos=np.random.randint(len(levy_sea))
    reward = 0
    for x in range(len(walk)):
        if(walk[x] < 0):
            for y in range(walk[x], 0):
                reward += levy_sea[pos][x]
                pos-=1
                if(pos<0):
                    pos+=2500
        else:
            for y in range(walk[x]):
                reward += levy_sea[pos][x]
                pos+=1
                if(pos >= 2500):
                    pos-=2500
        
    return reward

def random_walk(N):
    s = np.random.normal(loc=0, scale=30, size=N)
    steps = [int(x) for x in s]
    #print(len(steps))
    return steps
            
def levy_walk(N):
    a = np.array(range(5,2500))
    prob = levy.levy(a, 1, 0)
    stepsorig = [random.choices(a, weights=prob) for x in range(5000)]
    steps = [np.random.choice([1,-1], p=[.5,.5]) * x[0] for x in stepsorig]
    #print(len(steps))
    return  steps
        
def walk_to_position(random_walk): #This function takes a random walk as it's parameter, and returns a torus bouded positon list
    pos=[]
    for i in range(len(random_walk)):
        if(i == 0): #First position is a random depth
            y = random_walk[i]
            while(y >= 2500): #Torus
                y -= 2500
            while(y < 0):#Torus
                y+=2500
            pos.append(y)#Add Initial position
        else:
            y = random_walk[i] + pos[i-1]
            while(y >= 2500):
                y -= 2500
            while(y < 0):
                y+=2500
            pos.append(y)
    return pos
    
def generate_seascapes_random(scope, num_patches):
    seascapes = []
    for i in range(scope):
        seascape_uniform = create_seascape_uniform(100,num_patches,2500,5000)
        seascapes.append(seascape_uniform)
    return seascapes

def generate_seascapes_levy(scope, num_patches):
    seascapes_ll = []
    for i in range(scope):
        seascape_levy = create_seascape_levy(100,num_patches,2500,5000)
        seascapes_ll.append(seascape_levy)
    return seascapes_ll
        
def generate_random_walks(scope, step_count):
    walks = []
    positions = []
    for i in range(scope):
        steps = random_walk(step_count)
        walks.append(steps)
        positions.append(walk_to_position(steps))
    return walks, positions

def generate_levy_walks(scope, step_count):
    walks = []
    positions = []
    for i in range(scope):
        steps = levy_walk(step_count)
        walks.append(steps)
        positions.append(walk_to_position(steps))
    return walks, positions

def get_consumptions(seascapes, walks):
    arr_consumption = []
    for seascape in seascapes:
        for walk in walks:
            consumption = reward(seascape, walk)
            arr_consumption.append(consumption)
    return arr_consumption



if __name__ == "__main__":
    num_levy_seascapes = int(input("Enter number of Levy Seascapes you would like:"))
    num_patches_levy = int(input("Enter number of Levy patches you would like:"))
    levy_seascapes = generate_seascapes_levy(num_levy_seascapes,num_patches_levy )
    
    num_levy_walks = int(input("Enter number of Levy walks you would like:"))
    levy_walks, levy_positions = generate_levy_walks(num_levy_walks,5000)


    num_random_seascapes = int(input("Enter number of random Seascapes you would like:"))
    num_patches_random = int(input("Enter number of random patches you would like:"))

    random_seascapes = generate_seascapes_random(num_random_seascapes, num_patches_random)
    num_random_walks = int(input("Enter number of random walks you would like:"))
    random_walks, random_positions = generate_random_walks(num_random_walks,5000)

    arr_consumption_new_ll = get_consumptions(levy_seascapes, levy_walks)
    arr_consumption_new_lr = get_consumptions(random_seascapes, levy_walks)
    arr_consumption_new_rl = get_consumptions(levy_seascapes, random_walks)
    arr_consumption_new_rr = get_consumptions(random_seascapes, random_walks)
    pyplot.hist(arr_consumption_new_ll)
    
    pyplot.savefig('hist_LL.jpg')
    print(f"mean: {np.mean(arr_consumption_new_ll)}")
    print(f"median: {np.median(arr_consumption_new_ll)}")
    
    pyplot.hist(arr_consumption_new_lr)
    pyplot.savefig('hist_LR.jpg')
    print(f"mean: {np.mean(arr_consumption_new_lr)}")
    print(f"median: {np.median(arr_consumption_new_lr)}")
    
    pyplot.hist(arr_consumption_new_rl)
    pyplot.savefig('hist_RL.jpg')
    print(f"mean: {np.mean(arr_consumption_new_rl)}")
    print(f"median: {np.median(arr_consumption_new_rl)}")
    
    pyplot.hist(arr_consumption_new_rr)
    pyplot.savefig('hist_RR.jpg')
    print(f"mean: {np.mean(arr_consumption_new_rr)}")
    print(f"median: {np.median(arr_consumption_new_rr)}")

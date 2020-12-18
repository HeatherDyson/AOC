import math
import re
import pandas as pd
import numpy as np
import itertools
import time

def find_ternary(num):  #2
    quotient = num/3    #3
    remainder = num%3
    if quotient == 0:   #4
        return ""
    else:
        return find_ternary(int(quotient)) + str(int(remainder))    #5

def getPointName(t):
    return ','.join(str(s) for s in t)

def main():
    
    #read in file
    f = open("Day17.txt",'r')
    START = time.perf_counter_ns()

    initialState = []
    for line in f:
        initialState.append([x for x in line.strip('\n')])
    f.close()

    x_dim = (-1, len(initialState[0])+1)
    y_dim = (-1, len(initialState)+1)
    z_dim = (-1, 2)

    activeCubes = {}
    for i in range(len(initialState)):
        for j in range(len(initialState[0])):
            if initialState[i][j] == '#':
                activeCubes[getPointName((j,i,0))] = (j,i,0)
            
    #create 26 neighbors tuples
    neighbors = []
    for i in range(1,27):
        xyz = find_ternary(i).zfill(3)
        if xyz == '111':
            neighbors.append((-1,-1,-1))
        else:
            neighbors.append((int(xyz[0])-1,
                              int(xyz[1])-1,
                              int(xyz[2])-1))

    for i in range(6):
        x_range = [x for x in range(x_dim[0], x_dim[1])]
        y_range = [x for x in range(y_dim[0], y_dim[1])]
        z_range = [x for x in range(z_dim[0], z_dim[1])]
    
        cube = [(x,y,z) for x in x_range for y in y_range for z in z_range]
        addActive = []
        removeActive = []
        for pt in cube:
            thisPoint = getPointName(pt)
            activeNeighbors = 0
            for t in neighbors: #find number of active neighbors
                newPt = tuple(map(sum,zip(pt, t)))
                ptName = getPointName(newPt)
                if ptName in activeCubes:
                    activeNeighbors += 1
            if thisPoint in activeCubes:
                if activeNeighbors < 2 or activeNeighbors > 3:
                    removeActive.append(thisPoint)
            else:
                if activeNeighbors == 3:
                    addActive.append(pt)
                    
        [activeCubes.pop(key) for key in removeActive]
        for pt in addActive:
            activeCubes[getPointName(pt)] = pt
              
        x_dim = (x_dim[0]-1, x_dim[1]+1)
        y_dim = (y_dim[0]-1, y_dim[1]+1)
        z_dim = (z_dim[0]-1, z_dim[1]+1)

      
    #print(activeCubes)
    ans = len(activeCubes)
    print("Ans = ", ans)
    END = time.perf_counter_ns()
    print(f"Part 1 took {END-START} nanoseconds.")

main()

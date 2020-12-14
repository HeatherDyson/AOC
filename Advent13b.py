import math
import re
import pandas as pd
import functools 

#Got these from stack overflow
def gcd(a, b):
    #Return greatest common divisor using Euclid's Algorithm.
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    #Return lowest common multiple.
    return a * b // gcd(a, b)



def main():
    
    #read in file
    f = open("Day13.txt",'r')

    info = []
    for line in f:
        info.append(line)
    f.close()

    busIds = pd.Series([int(x) for x in info[1].split(',') if x != 'x'])
    l = []
    for x in info[1].split(','):
        if x != 'x':
            l.append(info[1].split(',').index(x))
        
    minuteOfDeparture = pd.Series(l)
    busIdsDF = pd.concat([minuteOfDeparture, busIds], axis =1)
    #busIdsDF.columns = ["t", "Bus ID"] could add columns but have to change
    #code below to reference columns instead of numbers
    print(busIdsDF)
    ans = 0

    # since B1totaltime = (B2Loops*B2) -(t2 - t1) then
    # B2Loops = (B1totalTime + t2 - t1)/B2
    incrementBy = 1
    lcmList = [busIdsDF.loc[0,1]]
    busLoops = 1
    for i in range(len(busIdsDF.loc[:,1])-1):
        x = busIdsDF.loc[i,1]*busLoops
        timeBetween = busIdsDF.loc[i+1,0]-busIdsDF.loc[i,0]
        while (x+timeBetween)%busIdsDF.loc[i+1,1] != 0:
            x += busIdsDF.loc[i,1]*incrementBy
        lcmList.append(busIdsDF.loc[i+1,1])
        #number of loops that next bus can do at a time
        incrementBy = functools.reduce(lcm, lcmList)/busIdsDF.loc[i+1,1]
        busLoops = (x+timeBetween)/busIdsDF.loc[i+1,1]
        ans = x-busIdsDF.loc[i,0]
            
    print("Ans = ", ans)

main()

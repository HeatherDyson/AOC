import math

def main():

    #read in file
    f = open("Day3.txt",'r')
    
    skiSlope = []
    
    for line in f:
        skiSlope.append(line.strip('\n'))
    f.close()

    numTrees = 0
    patternLen = len(skiSlope[0])
    dist = 0
    for x in skiSlope:
        if dist != 0:
            if x[dist%patternLen] == "#":
                numTrees +=1
        dist += 3
      

    print(numTrees)

main()

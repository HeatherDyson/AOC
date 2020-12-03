import math

def main():

    #read in file
    f = open("Day3.txt",'r')
    
    skiSlope = []
    
    for line in f:
        skiSlope.append(line.strip('\n'))
    f.close()

    
    slopesMultiplied = 1
    patternLen = len(skiSlope[0])

    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    for j in range(len(slopes)):
        numTrees = 0
        right = slopes[j][0]
        down = slopes[j][1]
        dist = 0
        for i in range(len(skiSlope)):
            if i == 0:
                continue
            if i%down == 0:
                x = skiSlope[i]
                dist += right
                if x[dist%patternLen] == "#":
                    numTrees +=1
        print(numTrees)
        slopesMultiplied *= numTrees
      

    print(slopesMultiplied)

main()

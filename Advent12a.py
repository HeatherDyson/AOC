import math
import re

def getVal(c, v):
    if c in ["L", "S", "W"]:
        return -v
    else:
        return v
    

def main():
    
    #read in file
    f = open("Day12.txt",'r')

    navigation = []
    for line in f:
        d = {
            "cmd": re.search('^.', line).group(),
            "val": getVal(re.search('^.', line).group(),
                          int(re.search('\d+', line).group()))
        }                      
        navigation.append(d)
    f.close()

    dirList = ["E", "S", "W", "N"]
    xAxis = ["E", "W"]
    yAxis = ["N", "S"]
    xVal = 0
    yVal = 0
    curDir = "E"

    for c in navigation:
        if c["cmd"] in ["L", "R"]:
            curDir = dirList[int(c["val"]/90 + dirList.index(curDir))%4]
            continue
        
        dirToMove = c["cmd"]
        val = c["val"]
        if dirToMove == "F":
            dirToMove = curDir
            val = getVal(dirToMove, val)

        if dirToMove in xAxis:
            xVal += int(val)
        else:
            yVal += int(val)
    
    distance = abs(xVal) + abs(yVal)
    
    print("Distance = ", distance)

main()

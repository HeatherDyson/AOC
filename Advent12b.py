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
    waypoint = {
        "EW": 10,
        "NS": 1
    }

    for c in navigation:
        if c["cmd"] in ["L", "R"]:
            #90 or -270 - NW sign stays same EW sign changes nums swap
            #-90 or 270 - NW sign changes EW stays same nums swap
            #180 or -180 - both signs change nums remain
            ewVal = waypoint["EW"]
            nsVal = waypoint["NS"]
            degrees = c["val"]
            if degrees in [90, -270]:
                waypoint["EW"] = nsVal
                waypoint["NS"] = -ewVal
            elif degrees in [-90, 270]:
                waypoint["EW"] = -nsVal
                waypoint["NS"] = ewVal
            else: #assuming no 360s in data
                waypoint["EW"] = -ewVal
                waypoint["NS"] = -nsVal           
        elif c["cmd"] in dirList:
            if c["cmd"] in xAxis:
                waypoint["EW"] += int(c["val"])
            else:
                waypoint["NS"] += int(c["val"])
        else: #cmd = "F"       
            xVal += int(c["val"]*waypoint["EW"])
            yVal += int(c["val"]*waypoint["NS"])
    
    distance = abs(xVal) + abs(yVal)
    
    print("Distance = ", distance)

main()

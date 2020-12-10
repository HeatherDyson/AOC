import math
import itertools

        
def findTuplesOfThrees(numList):

    listOfEndpoints = [(0,0)]
    for i in range(0,len(numList)-1):
        if abs(numList[i]-numList[i+1]) == 3:
            listOfEndpoints.append((i,i+1))
    return listOfEndpoints


def main():
    
    #read in file
    f = open("Day10.txt",'r')

    intList = []
    for line in f:
        intList.append(int(line))
    f.close()

    intList.append(0) #for the charging outlet
    intList.append(max(intList)+3) #for the built in adapter
    s = set(intList)
    
    endPoints = findTuplesOfThrees(list(s))
    arrangements = 1
    
    for i in range(0, len(endPoints)-1):
        endPointDiff = endPoints[i+1][0]-endPoints[i][1]
        if endPointDiff == 2:
            arrangements *= 2
        elif endPointDiff >= 3:
            arrangements = arrangements*(((endPointDiff-3)*3)+4)

    
    print("arrangements = ", arrangements)

main()

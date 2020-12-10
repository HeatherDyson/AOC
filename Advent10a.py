import math
import itertools

        
def findDiff(numList, diff):

    val = 0
    for i in range(0,len(numList)-1):
        if abs(numList[i]-numList[i+1]) == diff:
            val += 1
    return val


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
    
    joltageOne = findDiff(list(s), 1)
    joltageThree = findDiff(list(s), 3)
    

    joltage = joltageOne * joltageThree   
    
    print("1 joltage x 3 joltage = ", joltage)

main()

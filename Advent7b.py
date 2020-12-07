import math
import re

def numBagsInside(aBag, multiplier, allBags, count):
    for theBag in allBags[aBag]:
        count.append(multiplier*theBag[0])
        if theBag[1] in allBags.keys():
            numBagsInside(theBag[1], multiplier*theBag[0], allBags, count)

    return count

def main():
    
    #read in file
    f = open("Day7.txt",'r')
    
    bags = {}
    contains = []
    for line in f:
        if "no other bags" in line:
            continue
        else:           
            bagList = re.sub('bags', "bag",line).split("contain")
            outerBag = bagList[0].split(" bag")[0]
            innerBags = re.findall('(\w+\s\w+\s\w+)', bagList[1])
            for bag in innerBags:
                bagTuple = (int(re.search('\d+', bag).group()),
                            re.search('(?!\d+)(\w+\s\w+)', bag).group())
                contains.append(bagTuple)
            bags[outerBag] = contains.copy()
            contains.clear()
            
                      
    f.close()

    myBag = "shiny gold"
    
    
    numBags = (sum(numBagsInside(myBag, 1, bags, [])))

    print("Number of bags in Shiny Gold:", numBags)

main()

import math
import re


def main():
    
    #read in file
    f = open("Day7.txt",'r')
    
    bags = {}
    canBeIn = []
    for line in f:
        if "no other bags" in line:
            continue
        else:           
            bagList = re.sub('bags', "bag",line).split("contain")
            outerBag = bagList[0].split(" bag")[0]
            innerBags = re.findall('(?!\d+\s)(\w+\s\w+)(?!bag)', bagList[1])
            for bag in innerBags:
                if bag in bags.keys():
                    bags[bag].append(outerBag)
                else:
                    canBeIn.append(outerBag)
                    bags[bag] = canBeIn.copy()
                    canBeIn.clear()
    f.close()

    myBag = "shiny gold"

    listOfBags = bags[myBag]
    for bag in listOfBags:
        if bag in bags.keys():
            listOfBags.extend(bags[bag])
                              

    numBags = len(set(listOfBags))

    print("Shiny Gold can be in:", numBags)

main()

import math
import re
import pandas as pd
import itertools

def makeListOfNumbers(rule):
    numList = []
    ranges = re.findall('\d+-\d+', rule)
    for r in ranges:
        nums = r.split('-')
        for i in range(int(nums[0]), int(nums[1])+1):
            numList.append(i)
    return numList

def main():
    
    #read in file
    f = open("Day16.txt",'r')

    rules = {}
    fields = []
    myTicket = []
    nearbyTickets = []
    scanning = "rules"
    for line in f:
        if line == '\n':
            continue
        elif line == "your ticket:\n":
            scanning = "myTicket"
            continue
        elif line == "nearby tickets:\n":
            scanning = "nearbyTickets"
            continue
            
        if scanning == "rules":
            fields.append(line.split(':')[0])
            rules[line.split(':')[0]] = makeListOfNumbers(
                line.strip('\n').split(':')[1])
        elif scanning == "myTicket":
            myTicket = [int(x) for x in line.strip('\n').split(',')]
        elif scanning == "nearbyTickets":
            nearbyTickets.append([int(x) for x in (line.strip('\n').split(','))])
        
    f.close()

    #get all possible values
    possibleNums = []
    for key in rules:
        possibleNums.extend(rules[key])

    s = set(possibleNums)
    
    errorRate = 0
    invalidTickets = []
    for t in nearbyTickets:
        for num in t:
            if num not in s:
                errorRate += num
                invalidTickets.append(t)
    for t in invalidTickets:
        nearbyTickets.remove(t)
                
    print("Error Rate = ", errorRate)

    #part b
    fieldOrder = [fields] * len(fields)

    #find possible fields for each number
    for t in nearbyTickets:
        for i in range(len(t)):
            possibleFields = []
            for key in rules:
                if t[i] in rules[key]:
                    possibleFields.append(key)
            fieldOrder[i] = list(set(fieldOrder[i]).intersection(set(possibleFields)))

    #reduce fields to one possibility for each number
    tempFieldOrder = fieldOrder.copy()
    while sum([len(x) for x in fieldOrder]) != len(fieldOrder):
        #find singleton
        s = []
        for f in tempFieldOrder:
            if len(f) == 1:
                s = f
                break
        #remove value from all other lists
        for f in fieldOrder:
            if f == s:
                continue
            elif s[0] in f:
                f.remove(s[0])
        #remove s from tempFieldOrder
        tempFieldOrder.remove(s)

    #find departure multiple
    departureVal = 1
    for i in range(len(fieldOrder)):
        if re.match('departure.*', fieldOrder[i][0]):
            departureVal *= myTicket[i]
        
    print("Departures multiplied = ", departureVal)
     
    

main()

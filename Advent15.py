import math
import re
import pandas as pd


def main():

    #hard coded because so short you would have to edit for your input
    example = [0,3,6]
    myInput = [8,0,17,4,1,12]
    
    numSpoken = 30000000
    game = myInput
   
    gameDict = {}
    for i in range(0,len(game)):
        gameDict[game[i]] = (-1, i) #store last two indexes as tuple
                                    # -1 means it is only there once
        

    count = len(game)
    lastNum = game[-1]
    countFor2020 = 0
    while count < numSpoken:
        if gameDict[lastNum][0] == -1: #num called once
            lastNum = 0
        else:
            lastNum = gameDict[lastNum][1]-gameDict[lastNum][0]

        if lastNum in gameDict: #update the indexes
            gameDict[lastNum] = (gameDict[lastNum][1], count) 
        else: #add it to dictionary
            gameDict[lastNum] = (-1, count)
                                
        count += 1
        if count == 2020:
            countFor2020 = lastNum
        
    
    print("2020th number = ", countFor2020)
    print("30000000th number = ", lastNum)

main()

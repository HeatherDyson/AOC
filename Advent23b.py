import time

def main():

    #after determining my implementation for part 1 would
    #take 55+ hours to run:
    #got this idea from reddit megasolutions thread about
    #linked list using a list then did implementation
    #kudos to jeslinmx for great idea
    
    cupOrderInput = [5,6,2,8,9,3,1,4,7] #my data
    #cupOrderInput = [3,8,9,1,2,5,4,6,7] #example
    cupOrder = [x for x in range(1, 1000001)]
    #cupOrder = cupOrderInput
    linkListCups = cupOrder.copy()
    linkListCups.append(0)
    for i in range(len(cupOrderInput)):
        cupOrder[i] = cupOrderInput[i]

    START = time.perf_counter()
    numMoves = 10000000
    currentCup = cupOrder[0]
    numCups = len(cupOrder)
    for i in range(numCups):
        if i+1 != numCups:
            linkListCups[cupOrder[i]] = cupOrder[(i+1)]
        else:
            linkListCups[cupOrder[i]] = cupOrder[0]
    linkListCups[0] = 0
    for i in range(0,numMoves):
        removedCups = []
        nextCup = currentCup
        for j in range(3):
            removedCups.append(linkListCups[nextCup])
            nextCup = linkListCups[nextCup]
                    
        destination = currentCup-1
        while destination in removedCups:
            destination -= 1            
        if destination == 0:
            destination = max(cupOrder)
            while destination in removedCups:
                destination -= 1            

        newNextCup = linkListCups[removedCups[2]]          
        linkListCups[removedCups[2]] = linkListCups[destination]   
        linkListCups[destination] =  removedCups[0]
        linkListCups[currentCup] =  newNextCup  
        currentCup = newNextCup

    numAfterOne = linkListCups[1]
    numAfterThat = linkListCups[numAfterOne]
    result = numAfterOne * numAfterThat
    
    print("Star Cups Multiplied = ", result)
    END = time.perf_counter()
    print(f"Part 2 took {END-START}.")

main()

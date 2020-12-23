def main():

    cupOrder = [5,6,2,8,9,3,1,4,7] #my data
    #cupOrder = [3,8,9,1,2,5,4,6,7] #example

    numMoves = 10
    currentCup = cupOrder[0]
    numCups = len(cupOrder)
    for i in range(0,numMoves):
        cupIndx = cupOrder.index(currentCup)
        removedCups = [cupOrder[(cupIndx+1)%numCups],
                       cupOrder[(cupIndx+2)%numCups],
                       cupOrder[(cupIndx+3)%numCups]]
        
        cupOrder = [x for x in cupOrder if x not in removedCups]
        
        destination = currentCup-1
        while destination in removedCups:
            destination -= 1            
        if destination == 0:
            destination = max(cupOrder)

        destIndx = cupOrder.index(destination)
        for num in removedCups[::-1]:
            cupOrder.insert(destIndx+1, num)
        
        print(currentCup, '\n', cupOrder, '\n', removedCups, destination)

        cupIndx = cupOrder.index(currentCup)
        currentCup = cupOrder[(cupIndx+1)%numCups]
    
    result = 0

    oneIndx = cupOrder.index(1)
    cupStr = ""
    for i in range(1, numCups):
        cupStr += str(cupOrder[(oneIndx+i)%numCups])
    
    print("cup order = ", cupStr)
    #END = time.perf_counter_ns()
    #print(f"Part 1 took {END-START} nanoseconds.")

main()

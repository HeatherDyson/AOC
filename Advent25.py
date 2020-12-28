
def performHandshake(subjectNum, loopSize):
    eKey = 1
    for i in range(loopSize):
        eKey *= subjectNum
        eKey = eKey%20201227
    return eKey
    
def getLoopSize(subjectNum, publicKey):
    
    loopSize = 0
    value = 1
    while value != publicKey:
        value *= subjectNum
        value = value%20201227
        loopSize += 1
    return loopSize
    

def main():

    cardPublicKey = 18499292  #my data
    doorPublicKey = 8790390
    #cardPublicKey = 5764801     #example
    #doorPublicKey = 17807724

    subjectNum = 7

    cardLoopSize = getLoopSize(7, cardPublicKey)
    doorLoopSize = getLoopSize(7, doorPublicKey)
    print(cardLoopSize, doorLoopSize)

    
    eKey = performHandshake(cardPublicKey, doorLoopSize)
    print("Encryption Key = ", eKey)
    #END = time.perf_counter_ns()
    #print(f"Part 1 took {END-START} nanoseconds.")

main()

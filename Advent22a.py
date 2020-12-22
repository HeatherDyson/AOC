def main():

    fileName = "Day22.txt"
    fileName = "Day22example.txt"
    #read in file
    f = open(fileName,'r')
    #START = time.perf_counter_ns()

    data = f.read().split('\n\n')
    f.close()
    me = [x for x in map(int, data[0].split('\n')[1:len(data[0])])]
    mrCrab = [x for x in map(int, data[1].split('\n')[1:len(data[1])])]

    while len(me) != 0 and len(mrCrab) != 0:
        myCard = me.pop(0)
        mrCrabsCard = mrCrab.pop(0)
        if myCard > mrCrabsCard:
            me.append(myCard)
            me.append(mrCrabsCard)
        else:
            mrCrab.append(mrCrabsCard)
            mrCrab.append(myCard)
            
    if len(me) != 0:
        winner = me
        print("I won!")
    else:
        winner = mrCrab
        print("Mr. Crab won!")
        
    result = 0
    winner = winner[::-1]
    for i in range(len(winner)):
        result += (i+1)*(winner[i])
        
        
    print("Winner Score = ", result)
    #END = time.perf_counter_ns()
    #print(f"Part 1 took {END-START} nanoseconds.")

main()

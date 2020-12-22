
def playRecursiveCombat(me, mrCrab):

    
    while len(me["hand"]) != 0 and len(mrCrab["hand"]) != 0:
        if (me["hand"] in me["allHands"] and
            mrCrab["hand"] in mrCrab["allHands"]):
            return {"name": "me",
                  "hand": me["hand"]}

        if me["hand"] not in me["allHands"]:
            me["allHands"].append(me["hand"].copy())
        if mrCrab["hand"] not in mrCrab["allHands"]:
            mrCrab["allHands"].append(mrCrab["hand"].copy())
                              
        myCard = me["hand"].pop(0)
        mrCrabsCard = mrCrab["hand"].pop(0)

        if len(me["hand"]) >= myCard and len(mrCrab["hand"]) >= mrCrabsCard:
            newMe = {"hand": me["hand"][0:myCard],
                     "allHands": []}
            newMrCrab = {"hand": mrCrab["hand"][0:mrCrabsCard],
                         "allHands": []}
            w = playRecursiveCombat(newMe, newMrCrab)
            if w["name"] == "me":
                me["hand"].append(myCard)
                me["hand"].append(mrCrabsCard)
            else:
                mrCrab["hand"].append(mrCrabsCard)
                mrCrab["hand"].append(myCard)                
        else:          
            if myCard > mrCrabsCard:
                me["hand"].append(myCard)
                me["hand"].append(mrCrabsCard)
            else:
                mrCrab["hand"].append(mrCrabsCard)
                mrCrab["hand"].append(myCard)
            
    if len(me["hand"]) != 0:
        winner = {"name": "me",
                  "hand": me["hand"]}
    else:
        winner = {"name": "Mr. Crab",
                  "hand": mrCrab["hand"]}

    return winner

def main():

    fileName = "Day22.txt"
    fileName = "Day22example.txt"
    #read in file
    f = open(fileName,'r')
    #START = time.perf_counter_ns()

    data = f.read().split('\n\n')
    f.close()
    winner = playRecursiveCombat(
        {"hand":[x for x in map(int, data[0].split('\n')[1:len(data[0])])],
         "allHands":[]},
        {"hand":[x for x in map(int, data[1].split('\n')[1:len(data[1])])],
         "allHands":[]})


        
    result = 0
    hand = winner["hand"][::-1]
    for i in range(len(hand)):
        result += (i+1)*(hand[i])
        
    print("The Winner is", winner["name"])   
    print("Score = ", result)
    #END = time.perf_counter_ns()
    #print(f"Part 1 took {END-START} nanoseconds.")

main()

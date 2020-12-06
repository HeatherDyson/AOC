import math

def main():
    
    #read in file
    f = open("Day6.txt",'r')
    
    answers = []
    group = []
    for line in f:
        if line != "\n":
            group.append(line.strip('\n'))
        else:
            answers.append(group.copy())
            group.clear()
    f.close()

    answers.append(group) #append the last group

    numYesses = 0
    for x in answers:
        ans = [set(a) for a in x]
        if len(ans) == 1:
            numYesses += len(ans[0])
        else:
            sameAns = ans[0].intersection(*ans[1:])
            # note * turns list into individual parameters for a func
            numYesses += len(sameAns) 
        


    print("Total same yes answers:", numYesses)

main()

import math

def main():
    
    #read in file
    f = open("Day6.txt",'r')
    
    answers = []
    for line in f:
        if line != "\n":
            answers.append(line.strip('\n'))
        else:
            answers.append(line)
    f.close()

    #reformat answers
    answers = "".join(answers).split('\n')

    numYesses = 0
    for x in answers:
        numYesses += len("".join(set(x))) #get number of unique letters in str


    print("Total yes answers:", numYesses)

main()

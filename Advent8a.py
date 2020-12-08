import math
import re


def main():
    
    #read in file
    f = open("Day8.txt",'r')

    program = []
    for line in f:
        command = (line.split()[0], int(line.split()[1]))
        program.append(command)
    f.close()

    accumulator = 0
    currentCommand = 0
    commandsPerformed = []
    while True:
        if currentCommand in commandsPerformed:
            break;
        commandsPerformed.append(currentCommand)
        
        operation = program[currentCommand][0]
        arguement = program[currentCommand][1]
        if operation == "acc":
            accumulator += arguement
            currentCommand += 1
        elif operation == "nop":
            currentCommand += 1
        elif operation == "jmp":
            currentCommand += arguement
            

    print("Accumulator = ", accumulator)

main()

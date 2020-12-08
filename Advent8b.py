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

    commandToAlter = -1
    for t in program:
        commandToAlter += 1
        if t[0] == "acc":
            continue
        
        accumulator = 0
        currentCommand = 0
        commandsPerformed = []
        while True:
            if currentCommand in commandsPerformed:
                break
            if (currentCommand >= len(program) or
                currentCommand < 0):
                break
            
            commandsPerformed.append(currentCommand)
        
            operation = program[currentCommand][0]
            arguement = program[currentCommand][1]
            if operation == "acc":
                accumulator += arguement
                currentCommand += 1
            elif operation == "nop":
                if currentCommand == commandToAlter: #do jmp instead
                    currentCommand += arguement
                else:
                    currentCommand += 1
            elif operation == "jmp":
                if currentCommand == commandToAlter: #do nop instead
                    currentCommand += 1
                else:
                    currentCommand += arguement
                    
        if currentCommand == len(program):
            break
        
            

    print("Accumulator = ", accumulator)

main()

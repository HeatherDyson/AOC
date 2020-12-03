import math

def main():

    #read in file
    f = open("Day2.txt",'r')
    
    passwords = []
    
    for line in f:
        passwords.append(line.strip('\n'))
    f.close()

    numValid = 0
    for x in passwords:
        components = x.split(" ")
        ruleRange = components[0].split("-")
        ruleLetter = components[1].strip(":")
        letterCount = components[2].count(ruleLetter)
        if letterCount >= int(ruleRange[0]) and letterCount <= int(ruleRange[1]):
            numValid += 1

    print(numValid)

main()

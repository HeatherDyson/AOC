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
        password = components[2]
        
        if (password[int(ruleRange[0])-1] == ruleLetter and
            password[int(ruleRange[1])-1] != ruleLetter):
            numValid += 1
        elif (password[int(ruleRange[0])-1] != ruleLetter and
                 password[int(ruleRange[1])-1] == ruleLetter):
            numValid += 1

    print(numValid)

main()

import math
import re
import pandas as pd


def main():
    
    #read in file
    f = open("Day14.txt",'r')

    info = []
    for line in f:
        info.append(line.strip('\n'))
    f.close()

    memory = {}
    mask = ""
    
    for x in info:
        if re.search('mask.*',x):
            mask = list(x.split('= ')[1])
        else:
            s = re.findall('\d+', x)
            memLoc = s[0]
            binaryRep = list(("{0:b}".format(int(s[1]))).zfill(len(mask)))
            for i in range(0,len(mask)):
                if mask[i] != 'X':
                    binaryRep[i] = mask[i]
            memory[memLoc] = int("".join(x for x in binaryRep), 2)

    ans = 0       
    for x in memory:
        ans += memory[x]
    
    print("Ans = ", ans)

main()

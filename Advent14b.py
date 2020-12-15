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
    floatIndxList = []
    
    for x in info:
        if re.search('mask.*',x):
            mask = list(x.split('= ')[1])
            s = pd.Series(mask)
            xLocs = s == 'X'
            floatIndxList = xLocs[xLocs].index.tolist()
        else:
            s = re.findall('\d+', x)
            memVal = int(s[1])
            binaryRep = list(("{0:b}".format(int(s[0]))).zfill(len(mask)))
            for i in range(0,len(mask)):
                if mask[i] != '0':
                    binaryRep[i] = mask[i]
            numFloat = len(floatIndxList)
            for i in range(0,2**numFloat):
                xReplace = list(("{0:b}".format(i)).zfill(numFloat))
                for (indx, r) in zip(floatIndxList, xReplace):
                    binaryRep[indx] = r
                memory[int("".join(x for x in binaryRep), 2)] = memVal

    ans = 0       
    for x in memory:
        ans += memory[x]
    
    print("Ans = ", ans)

main()

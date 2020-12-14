import math
import re
import pandas as pd


def main():
    
    #read in file
    f = open("Day13.txt",'r')

    info = []
    for line in f:
        info.append(line)
    f.close()

    myTime = int(info[0])
    busIds = pd.Series([int(x) for x in info[1].split(',') if x != 'x'])
    busIdsDF = pd.concat([busIds, busIds], axis =1)

    busIdsDF.loc[:, 1] = [math.ceil(x) for x in
                          myTime/busIdsDF.loc[:,0]]*busIdsDF.loc[:,0]
       
    s = [x for x in busIdsDF.loc[:,1] - myTime]
    minMin = s.index(min(s))
    ans = busIdsDF.loc[minMin, 0] * s[minMin]
    print("Ans = ", ans)

main()

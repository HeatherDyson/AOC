import math
import re
import pandas as pd
import numpy as np
import itertools
import time

def evaluate(equasion):
    result = 0
    multiplyList = []
    for val in equasion:
        if val.isnumeric():
            result += int(val)
        elif val == "*":
            multiplyList.append(result)
            result = 0
    multiplyList.append(result)    
    result = 1
    for m in multiplyList:
        result *= m          
                
    return result


def main():
    
    #read in file
    f = open("Day18.txt",'r')
    #START = time.perf_counter_ns()

    result = 0
    for line in f:
        eq = line.strip('\n')
        while re.match('.*\(.*', eq):
            eqList = re.findall('\([^()]*\)', eq)
            for e in eqList:
                eq = eq.replace(e, str(evaluate((re.sub('[(){}<>]', '', e)).split(' '))))
            
        result += evaluate(eq.split(' '))
    f.close()

    print("Ans = ", result)
    #END = time.perf_counter_ns()
    #print(f"Part 1 took {END-START} nanoseconds.")

main()

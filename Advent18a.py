import math
import re
import pandas as pd
import numpy as np
import itertools
import time

def evaluate(equasion):
    operation = "add"
    result = 0
    for val in equasion:
        if val.isnumeric():
            if operation == "add":
                result += int(val)
            elif operation == "mult":
                result *= int(val)
        elif val == "+":
            operation = "add"
        elif val == "*":
            operation = "mult"           
                
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

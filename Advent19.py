import math
import re
import pandas as pd
import numpy as np
import itertools
import time

def main():

    fileName = "Day19.txt"
    #fileName = "Day19example.txt"
    #fileName = "Day19example2.txt"
    #read in file
    f = open(fileName,'r')
    #START = time.perf_counter_ns()

    rules = {}
    messages = []
    for line in f:
        if re.match('.*:.*', line):
            line = line.strip('\n')
            s = line.split(':')
            if s[1].lstrip() == '"a"':
                s[1] = 'a'
            elif s[1].lstrip() == '"b"':
                s[1] = 'b'
            elif re.match('.*\|.*', s[1]):
                s[1] = '(' + s[1] + ' )'
            else:
                s[1] = s[1] + ' '
            rules[int(s[0])] = s[1]
        else:
            if line != '\n':
                messages.append(line.strip('\n'))
    f.close()

    ruleregx = rules[0]
    counter = 0
    while re.match('.*\d+.*', ruleregx):
        ruleNums = set(re.findall('\d+', ruleregx))
        for r in ruleNums:
            rule = ruleregx.split()
            for i in range(len(rule)):
                if rule[i] == str(r):
                    rule[i] = rules[int(r)]
            ruleregx = " ".join(rule)
        
        #counter += 1
        #if counter > 10:
            #break

    ruleregx = '^' + ruleregx.replace(' ', '') + '$'
    #print(ruleregx)
    result = 0
    for m in messages:
        if re.search(ruleregx, m):
            result += 1
    print("Ans = ", result)
    #END = time.perf_counter_ns()
    #print(f"Part 1 took {END-START} nanoseconds.")

main()

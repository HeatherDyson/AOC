import math

def main():

    #read in file
    f = open("Day1.txt",'r')
    expenseReport = []
    for line in f:
        expenseReport.append(int(line.strip('\n')))
    f.close()

    numExpenses = len(expenseReport)
    answer = 0
    
    for x in expenseReport:
        for y in expenseReport:
            if x != y:
                for z in expenseReport:
                    if z != x and z != y:
                        if x+y+z == 2020:
                            answer = x*y*z
                            print(answer)
                            break
            if answer != 0:
                break
        if answer != 0:
            break
        else:
            expenseReport.remove(x)
    
    print(answer)

main()

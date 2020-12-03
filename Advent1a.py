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
                if x+y == 2020:
                    answer = x*y
                    print(answer)
                    break
        if answer != 0:
            break;
        else:
            expenseReport.remove(x)
    
    print(answer)

main()

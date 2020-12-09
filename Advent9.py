import itertools

def findSum(val, numList):
    for numbers in itertools.combinations(numList,2):
        if sum(numbers) == val:
            return True
    return False
        


def main():
    
    #read in file
    f = open("Day9.txt",'r')

    intList = []
    for line in f:
        intList.append(int(line))
    f.close()

    preambleSize = 25

    # Part a
    firstInvalidNum = 0
    for i in range(preambleSize, len(intList)):
        if not findSum(intList[i], intList[i-preambleSize:i]):
            firstInvalidNum = intList[i]
            break

    print("Invalid Num = ", firstInvalidNum)

    # Part b
    contSum = intList[0]
    start = 0
    end = 0
    for i in range(1, len(intList)):               
        contSum += intList[i]

        while contSum > firstInvalidNum:
            contSum -= intList[start]
            start += 1

        if contSum == firstInvalidNum:
            end = i
            break

    weakness = min(intList[start:end+1]) + max(intList[start:end+1])
    print("Encryption Weakness = ", weakness)

main()

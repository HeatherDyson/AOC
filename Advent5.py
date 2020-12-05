import math

def main():

    #seatID = row*8 + 5
    
    #read in file
    f = open("Day5.txt",'r')
    
    boardingPasses = []
    for line in f:
        boardingPasses.append(line.strip('\n'))
    f.close()

    highestSeatID = 0
    seatIDList = []
    for x in boardingPasses:
        rowCode = x[0:7]
        columnCode = x[-3:]

        rows = list(range(0,128))
        columns = list(range(0,8))

        for let in rowCode:
            cut = int(len(rows)/2)
            if let == "F":
                rows = rows[:cut]
            elif let == "B":
                rows = rows[-cut:]

        for let in columnCode:
            cut = int(len(columns)/2)
            if let == "L":
                columns = columns[:cut]
            elif let == "R":
                columns = columns[-cut:]
            
        seatID = (rows[0]*8)+columns[0]
        seatIDList.append(seatID)
        if seatID > highestSeatID:
            highestSeatID = seatID

            
    #part a
    print("Highest seat ID:", highestSeatID)

    seatIDList.sort()
    missingNumbers = [x for x in range(seatIDList[0], seatIDList[-1]+1)  
                               if x not in seatIDList]
    #part b
    print("My seat ID:", missingNumbers)

main()

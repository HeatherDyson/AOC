def anyOccupied(rowList, row, rowIncr, col, colIncr):
    row += rowIncr
    col += colIncr
    rowLen = len(rowList)
    colLen = len(rowList[0])
    while row in range(0, rowLen)  and col in range(0, colLen):
        if rowList[row][col] == "#":
            return 1
        elif rowList[row][col] == "L":
            break
        row += rowIncr
        col += colIncr
            
    return 0
    

def main():
    
    #read in file
    f = open("Day11.txt",'r')

    seats = []
    for line in f:
        seats.append(line.strip("\n"))
    f.close()

    occupiedSeats = 0
    colLen = len(seats[0])
    rowLen = len(seats)
    while True:
        newSeatConfig = []
        for i in range(rowLen):
            newRow = ""
            for j in range(colLen):
                occupied = (anyOccupied(seats, i, -1, j, -1) +
                            anyOccupied(seats, i, -1, j, 0) +
                            anyOccupied(seats, i, -1, j, 1) +
                            anyOccupied(seats, i, 0, j, -1) +
                            anyOccupied(seats, i, 0, j, 1) +
                            anyOccupied(seats, i, 1, j, -1) +
                            anyOccupied(seats, i, 1, j, 0) +
                            anyOccupied(seats, i, 1, j, 1) )
                seatVal = seats[i][j]
                if seatVal == "L" and occupied == 0:
                    newRow += "#"
                elif seatVal == "#" and occupied >= 5:
                    newRow += "L"
                else:
                    newRow += seatVal
            newSeatConfig.append(newRow)
        if seats == newSeatConfig:
            break
        else:
            seats = newSeatConfig.copy()

        
    for x in seats:
        occupiedSeats += x.count("#")
    
    
    print("Occupied Seats = ", occupiedSeats)

main()

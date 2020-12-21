import math
import re
import pandas as pd
import numpy as np
import itertools
import time

class Tile:
    top = 0
    topR = 1
    bottom = 2
    bottomR = 3
    left = 4
    leftR = 5
    right = 6
    rightR = 7
    
    def __init__(self, tileInfo):
        self.tile = tileInfo
        self.leftNeighbor = -1
        self.rightNeighbor = -1
        self.topNeighbor = -1
        self.bottomNeighbor = -1
        self.isCorner = False
        self.isEdge = False
        self.pos = (-1,-1)
        self.mySides = self.getAllSides()
        
    def getTop(self):
        return self.tile[0]

    def getBottom(self):
        return self.tile[-1]

    def getLeftSide(self):
        leftSide = ""
        for row in self.tile:
            leftSide += row[0]
        return leftSide

    def getRightSide(self):
        rightSide = ""
        for row in self.tile:
            rightSide += row[-1]
        return rightSide

    def flipTopToBottom(self):
        self.tile = [row for row in self.tile[::-1]]
        temp = self.topNeighbor
        self.topNeighbor = self.bottomNeighbor
        self.bottomNeighbor = temp
        self.mySides = self.getAllSides()
        
    def flipSideToSide(self):
        newTile = []
        for row in self.tile:
            row = row[::-1]
            newTile.append(row)
        self.tile = newTile
        temp = self.rightNeighbor
        self.rightNeighbor = self.leftNeighbor
        self.leftNeighbor = temp
        self.mySides = self.getAllSides()

    def rotateRight(self):
        newTile = []
        for row in range(0,len(self.tile)):
            newTile.append(''.join(col[row] for col in self.tile)[::-1])
        self.tile = newTile
        temp = self.topNeighbor
        self.topNeighbor = self.leftNeighbor
        self.leftNeighbor = self.bottomNeighbor
        self.bottomNeighbor = self.rightNeighbor
        self.rightNeighbor = temp
        self.mySides = self.getAllSides()
        
    def rotateLeft(self):
        newTile = []
        for row in range(len(self.tile)-1, -1, -1):
            newTile.append(''.join(col[row] for col in self.tile))
        self.tile = newTile
        temp = self.topNeighbor
        self.topNeighbor = self.rightNeighbor
        self.rightNeighbor = self.bottomNeighbor
        self.bottomNeighbor = self.leftNeighbor
        self.leftNeighbor = temp
        self.mySides = self.getAllSides()
            

    def getAllSides(self):
        return [self.getTop(), self.getTop()[::-1],
                self.getBottom(), self.getBottom()[::-1],
                self.getLeftSide(), self.getLeftSide()[::-1],
                self.getRightSide(), self.getRightSide()[::-1]]
    
    def getNeighbors(self):
        theNeighbors = []
        if self.topNeighbor != -1:
            theNeighbors.append(self.topNeighbor)
        if self.bottomNeighbor != -1:
            theNeighbors.append(self.bottomNeighbor)
        if self.leftNeighbor != -1:
            theNeighbors.append(self.leftNeighbor)
        if self.rightNeighbor != -1:
            theNeighbors.append(self.rightNeighbor)

        return theNeighbors
        
        
    def stripBorder(self):
        newTile = []
        for i in range(1, len(self.tile)-1):
            newTile.append(self.tile[i][1:-1])
        return newTile

    def rotateNeighbors(self):
        #take care of left neighbor
        if self.leftNeighbor != -1:
            myLeft = self.mySides[self.left]           
            if myLeft != self.leftNeighbor.mySides[self.right]:
                if myLeft == self.leftNeighbor.mySides[self.rightR]:
                    self.leftNeighbor.flipTopToBottom()
                elif myLeft == self.leftNeighbor.mySides[self.top]:
                    self.leftNeighbor.rotateRight()
                elif myLeft == self.leftNeighbor.mySides[self.topR]:
                    self.leftNeighbor.rotateRight()
                    self.leftNeighbor.flipTopToBottom()
                elif myLeft == self.leftNeighbor.mySides[self.left]:
                    self.leftNeighbor.flipSideToSide()
                elif myLeft == self.leftNeighbor.mySides[self.leftR]:
                    self.leftNeighbor.flipSideToSide()
                    self.leftNeighbor.flipTopToBottom()
                elif myLeft == self.leftNeighbor.mySides[self.bottom]:
                    self.leftNeighbor.rotateLeft()
                    self.leftNeighbor.flipTopToBottom()                    
                elif myLeft == self.leftNeighbor.mySides[self.bottomR]:
                    self.leftNeighbor.rotateLeft()
                    
        #take care of right neighbor
        if self.rightNeighbor != -1:
            myRight = self.mySides[self.right]           
            if myRight != self.rightNeighbor.mySides[self.left]:
                if myRight == self.rightNeighbor.mySides[self.rightR]:
                    self.rightNeighbor.flipSideToSide()
                    self.rightNeighbor.flipTopToBottom()
                elif myRight == self.rightNeighbor.mySides[self.top]:
                    self.rightNeighbor.rotateLeft()
                    self.rightNeighbor.flipTopToBottom()
                elif myRight == self.rightNeighbor.mySides[self.topR]:
                    self.rightNeighbor.rotateLeft()
                elif myRight == self.rightNeighbor.mySides[self.right]:
                    self.rightNeighbor.flipSideToSide()
                elif myRight == self.rightNeighbor.mySides[self.leftR]:
                    self.rightNeighbor.flipTopToBottom()
                elif myRight == self.rightNeighbor.mySides[self.bottom]:
                    self.rightNeighbor.rotateRight()
                elif myRight == self.rightNeighbor.mySides[self.bottomR]:
                    self.rightNeighbor.rotateRight()
                    self.rightNeighbor.flipTopToBottom()
            self.rightNeighbor.rotateNeighbors()
            
        #take care of top neighbor
        if self.topNeighbor != -1:
            myTop = self.mySides[self.top]           
            if myTop != self.topNeighbor.mySides[self.bottom]:
                if myTop == self.topNeighbor.mySides[self.rightR]:
                    self.topNeighbor.rotateRight()
                elif myTop == self.topNeighbor.mySides[self.top]:
                    self.topNeighbor.flipTopToBottom()
                elif myTop == self.topNeighbor.mySides[self.topR]:
                    self.topNeighbor.flipTopToBottom()
                    self.topNeighbor.flipSideToSide()
                elif myTop == self.topNeighbor.mySides[self.left]:
                    self.topNeighbor.rotateLeft()
                elif myTop == self.leftNeighbor.mySides[self.leftR]:
                    self.topNeighbor.rotateLeft()
                    self.topNeighbor.flipSideToSide()
                elif myTop == self.topNeighbor.mySides[self.right]:
                    self.topNeighbor.rotateRight()
                    self.topNeighbor.flipSideToSide()                    
                elif myTop == self.topNeighbor.mySides[self.bottomR]:
                    self.topNeighbor.flipSideToSide()
            
        #take care of bottom neighbor
        if self.bottomNeighbor != -1:
            myBottom = self.mySides[self.bottom]           
            if myBottom != self.bottomNeighbor.mySides[self.top]:
                if myBottom == self.bottomNeighbor.mySides[self.rightR]:
                    self.bottomNeighbor.rotateLeft()
                    self.bottomNeighbor.flipSideToSide()
                elif myBottom == self.bottomNeighbor.mySides[self.right]:
                    self.bottomNeighbor.rotateLeft()
                elif myBottom == self.bottomNeighbor.mySides[self.topR]:
                    self.bottomNeighbor.flipSideToSide()
                elif myBottom == self.bottomNeighbor.mySides[self.left]:
                    self.bottomNeighbor.rotateRight()
                    self.bottomNeighbor.flipSideToSide()
                elif myBottom == self.bottomNeighbor.mySides[self.leftR]:
                    self.bottomNeighbor.rotateRight()
                elif myBottom == self.bottomNeighbor.mySides[self.bottom]:
                    self.bottomNeighbor.flipTopToBottom()                    
                elif myBottom == self.bottomNeighbor.mySides[self.bottomR]:
                    self.bottomNeighbor.flipTopToBottom()
                    self.bottomNeighbor.flipSideToSide()
            self.bottomNeighbor.rotateNeighbors()

    def printTile(self):
        for t in self.tile:
            print(t)
        print('\n')
    
def assembleRow(piece):

    row = [piece]
    while piece.rightNeighbor != -1:
        row.append(piece.rightNeighbor)
        piece = piece.rightNeighbor
    return row

def findSeaMonsters(image):
    numSeaMonsters = 0
    body = re.compile('#....##....##....###')
    legs = re.compile('#..#..#..#..#..#')
    for i in range(1,len(image)-1):
        row = image[i]
        if re.search(body, row):
            bodies = [(m.start(0), m.end(0)) for m in re.finditer(body, row)]
            print("row:", i, "bodies:", bodies, "monsters:", numSeaMonsters)
            for b in bodies:
                if (re.search(legs, image[i+1][b[0]+1:b[1]-3]) and
                    image[i-1][b[1]-2] == '#'):
                    numSeaMonsters += 1
            print(numSeaMonsters)
                
    return numSeaMonsters

    
    
def main():

    fileName = "Day20.txt"
    #fileName = "Day20example.txt"
    #fileName = "Day20example2.txt"
    #read in file
    f = open(fileName,'r')
    #START = time.perf_counter_ns()

    tiles = {}
    data = f.read().split('\n\n')
    print(len(data))
    for t in data:
        info = t.split('\n')
        name = re.search('\d+', info[0]).group()
        info.pop(0)
        tiles[name] = Tile(info)
        
    f.close()

    cornersMult = 1
    corners = []
    for k in tiles:        
        numTopMatches = 0
        numBottomMatches = 0
        numLeftMatches = 0
        numRightMatches = 0
        for key in tiles:
            if k != key:
                #print(key)
                sides = tiles[key].mySides
                if tiles[k].getTop() in sides:                    
                    numTopMatches += 1
                    tiles[k].topNeighbor = tiles[key]
                
                if tiles[k].getBottom() in sides:
                    numBottomMatches += 1
                    tiles[k].bottomNeighbor = tiles[key]
                    
                if tiles[k].getRightSide() in sides:
                    numRightMatches += 1
                    tiles[k].rightNeighbor = tiles[key]
                    
                if tiles[k].getLeftSide() in sides:
                    numLeftMatches += 1
                    tiles[k].leftNeighbor = tiles[key]
                       
        matches = [numTopMatches,numBottomMatches,
                   numLeftMatches,numRightMatches]
        
        #print(k, ':', matches, "num 0's:", matches.count(0))
        if matches.count(0) == 2:
            cornersMult *= int(k)
            corners.append(tiles[k])

    
    startingPiece = corners[0]
    #make starting piece top left corner
    while not (startingPiece.topNeighbor == -1 and
               startingPiece.leftNeighbor == -1):
        startingPiece.rotateLeft()
        
    # get pieces in right shape the pieces by rows
    startingPiece.rotateNeighbors()
    startingPiece.pos = (0,0)
    t = startingPiece
    puzzle = []
    while True:
        puzzle.append(assembleRow(t))
        if t.bottomNeighbor != -1:
            t = t.bottomNeighbor
        else:
            break

    puzzleImage = []
    for row in puzzle:
        newRow = []
        for piece in row:
            if len(newRow) == 0:
                newRow = piece.stripBorder()
            else:
                newRow = [m+n for m,n in zip(newRow, piece.stripBorder())]
        if len(puzzleImage) == 0:
            puzzleImage = newRow.copy()
        else:
            for val in newRow:
                puzzleImage.append(val)

    numHashTags = 0                  
    for row in puzzleImage:
        #print(row)
        numHashTags += row.count('#')

    theImage = Tile(puzzleImage)
    monstersFound = 0
    counter = 0
    print(len(puzzleImage))
    while monstersFound == 0:
        print(counter, monstersFound)
        if counter > 20:
            break
        monstersFound = findSeaMonsters(puzzleImage)
        if monstersFound == 0:
            counter += 1
            if counter%4 == 0:
                theImage.flipSideToSide()
                puzzleImage = theImage.tile
            elif counter%4 == 1:
                theImage.flipTopToBottom()
                puzzleImage = theImage.tile
            elif counter%4 == 2:
                theImage.flipSideToSide()
                puzzleImage = theImage.tile
            elif counter%4 == 3:
                theImage.rotateLeft()
                puzzleImage = theImage.tile
            
        
        

    print("Corners Multiplied: ", cornersMult)
    print("Number Of Sea Monsters:", monstersFound)
    print("Number hash tags:", numHashTags)
    print("Water Roughness:", numHashTags - (monstersFound*15))
    #END = time.perf_counter_ns()
    #print(f"Part 1 took {END-START} nanoseconds.")

main()

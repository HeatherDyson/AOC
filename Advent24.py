import math
import re
import pandas as pd
import numpy as np
import itertools
import time


def main():
    
    #read in file
    f = open("Day24.txt",'r')
    #f = open("Day24example.txt",'r')
    #START = time.perf_counter_ns()

    result = 0
    startPos = (0,0)
    minX = maxX = minY = maxY = 0
    tiles = {}
    wasNS = False
    for line in f:
        tile = line.strip('\n')
        commands = []
        for i in range(len(tile)):
            if wasNS:
                wasNS = False
                continue
            c = tile[i]
            if c == 's' or c == 'n':
                commands.append(tile[i] + tile[i+1])
                wasNS = True
            else:
                commands.append(tile[i])
        tilePos = startPos
        for cmd in commands:
            if cmd == 'e':
                tilePos = (tilePos[0]+1, tilePos[1])
            elif cmd == 'w':
                tilePos = (tilePos[0]-1, tilePos[1])
            elif cmd == 'ne':
                tilePos = (tilePos[0]+1, tilePos[1]+1)
            elif cmd == 'nw':
                tilePos = (tilePos[0], tilePos[1]+1)
            elif cmd == 'se':
                tilePos = (tilePos[0], tilePos[1]-1)
            elif cmd == 'sw':
                tilePos = (tilePos[0]-1, tilePos[1]-1)
                
        if tilePos in tiles:
            tiles.pop(tilePos, None)
        else:
            tiles[tilePos] = "black"
            if tilePos[0] < minX:
                minX = tilePos[0]
            if tilePos[0] > maxX:
                maxX = tilePos[0]
            if tilePos[1] < minY:
                minY = tilePos[1]
            if tilePos[1] > maxY:
                maxY = tilePos[1]

        
    f.close()
        
    print("Part 1 = ", len(tiles))

    neighbors= [(1,0), (-1,0), (1,1), (0,1), (0,-1), (-1,-1)]
    for i in range(0, 100):
        tilesToRemove = []
        tilesToAdd = []
        for x in range(minX-1, maxX+2):
            for y in range(minY-1, maxY+2):
                pos = (x,y)
                myNeighbors = [tuple(map(sum,zip(pos, t))) for t in neighbors]
                blackNeighbors = 0
                for n in myNeighbors:
                    if n in tiles:
                        blackNeighbors += 1
                if (pos in tiles and (blackNeighbors == 0 or
                                      blackNeighbors > 2)):
                    tilesToRemove.append(pos)
                elif pos not in tiles and blackNeighbors == 2:
                    tilesToAdd.append(pos)
                    if pos[0] < minX:
                        minX = pos[0]
                    if pos[0] > maxX:
                        maxX = pos[0]
                    if pos[1] < minY:
                        minY = pos[1]
                    if pos[1] > maxY:
                        maxY = pos[1]
        for t in tilesToRemove:
            tiles.pop(t, None)
        for t in tilesToAdd:
            tiles[t] = "black"
        #print('Day', i, ':', len(tiles))

    print("Part 2 = ", len(tiles))
                
            
            

    #END = time.perf_counter_ns()
    #print(f"Part 1 took {END-START} nanoseconds.")

main()

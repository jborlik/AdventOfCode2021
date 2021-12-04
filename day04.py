#import itertools
import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections
#import math
import time
#import pprint

def pushboard(arrboard, aboard):
    if aboard:
        aboard = np.array(aboard)
        arrboard.append(aboard)

def parseInput(inputarr):
    """Returns array of ints (for draws) and array of 5x5 boards"""
    arrdraw = []
    arrboard = []
    aboard = None
    for irow, arow in enumerate(inputarr):
        if irow == 0:
            arrdraw = [int(x) for x in inputarr[0].split(',')]
        else:
            if arow == '':
                pushboard(arrboard,aboard)
                aboard = []
            else:
                aboard.append(np.array([int(x) for x in arow.split()]))

    if aboard:
        pushboard(arrboard,aboard)

    return arrdraw, arrboard


with open('day04.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""".splitlines()]   # 


thedata = testdata
thedata = alldata

arrdraw, arrboard = parseInput(thedata)

#print(arrdraw)
#print(f"{len(arrboard)} boards: {arrboard}")

# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

def checkIfWinner(aboard, checkDiagonals=False):
    """returns true if any row/col or diaganol is marked out"""
    # cols
    cols = np.all(aboard < 0,axis=0)
    if np.any(cols):
        return True
    rows = np.all(aboard < 0, axis=1)
    if np.any(rows):
        return True
    if checkDiagonals:
        diag1 = np.diagonal(aboard < 0)
        if np.all(diag1):
            return True
        diag2 = np.fliplr(aboard < 0).diagonal()
        if np.all(diag2):
            return True



if False:

    START = time.perf_counter()

    for adraw in arrdraw:
        print(f"DRAW {adraw}")
        # flag as drawn
        for aboard in arrboard:
            idx = np.where(aboard == adraw)
            aboard[idx] *= -1
        
        # check if a winner
        winnerboard = None
        for aboard in arrboard:
            if checkIfWinner(aboard):
                winnerboard = aboard
                break
        if winnerboard is not None:
            print(f"Got a winner!!! {winnerboard}")

            idx = winnerboard > 0
            sumval = np.sum(winnerboard[idx])
            print(f"Score = {sumval} x {adraw} = {sumval*adraw}")
            break

    


    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

FAKEVAL = -1000

if True:
    for adraw in arrdraw:
        print(f"DRAW {adraw}")
        # flag as drawn
        for aboard in arrboard:
            idx = np.where(aboard == adraw)
            if adraw == 0:  # special handling!  
                aboard[idx] = FAKEVAL
            else:
                aboard[idx] *= -1
        
        # check if a winner
        iwinners = []
        for iboard,aboard in enumerate(arrboard):
            if checkIfWinner(aboard):
                iwinners.append(iboard)

        if len(iwinners) > 0:
            print(f"Got {len(iwinners)} winners!!! {iwinners}")

            if len(iwinners) > 1:
                # just delete them all?
                for index in sorted(iwinners, reverse=True):
                    del arrboard[index]
            else:
                winnerboard = arrboard[iwinners[0]]
                if len(arrboard)==1:
                    print("This was the last board to win!")
                    winnerboard[ winnerboard==FAKEVAL] = 0

                    idx = winnerboard > 0
                    sumval = np.sum(winnerboard[idx])
                    print(f"Score = {sumval} x {adraw} = {sumval*adraw}")
                    break
                else:
                    # not the last board
                    print(f"removing board, {len(arrboard)-1} will remain")
                    arrboard.pop(iwinners[0])


    



END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")
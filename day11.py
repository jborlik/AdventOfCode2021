#import itertools
import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections
#import math
import time
#import pprint


with open('day11.txt') as datafile:
    alldata = np.array([list(map(int,list(x.strip()))) for x in datafile.readlines()])

testdata = np.array([list(map(int,list(x.strip()))) for x in """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".splitlines()])   # 


thedata = testdata
thedata = alldata

print(thedata)

neighbors = [(-1,-1),(-1,0),(-1,1),
             (0,-1),(0,1),
             (1,-1),(1,0),(1,1)]

def flash(thedata, irow,icol, listflashes):
    for neighbor in neighbors:
        inrow = irow + neighbor[0]
        incol = icol + neighbor[1]
        if (inrow >= 0) and (inrow < thedata.shape[0]) and (incol>=0) and (incol < thedata.shape[1]):
            thedata[inrow,incol] += 1
            if thedata[inrow,incol] == 10:
                listflashes.append( (inrow,incol) )


def step(thedata):
    # everything gains one level
    thedata += 1

    # look for 10's

    idx_10 = np.where( thedata == 10)

    listflashes = [ (irow,icol) for irow,icol in zip(idx_10[0], idx_10[1]) ]

    totalflashes = 0
    while len(listflashes) > 0:
        ifrow,ifcol = listflashes.pop()
        totalflashes += 1
        flash(thedata,ifrow,ifcol, listflashes)  # may append flashes
    
    # now set flashed to 0
    thedata[ thedata >= 10 ] = 0

    return totalflashes


# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if False:

    START = time.perf_counter()

    totalflashes = 0
    for istep in range(1,100+1):
        #print(f"Step {istep}")
        totalflashes += step(thedata)
        #print(thedata)

    print(f"After {istep} steps, totalflashes={totalflashes}")

    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()


totalflashes = 0
istep = 0
while True:
    istep += 1
    stepflashes = step(thedata)
    totalflashes += stepflashes
    if stepflashes == thedata.size:
        break
    #print(thedata)

print(f"All flashed at step {istep}")



END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")
#import itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
import collections   # deque
#import math
import time
#import pprint



with open('day09.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """2199943210
3987894921
9856789892
8767896789
9899965678""".splitlines()]   # 


thedata = testdata
thedata = alldata

WIDTH = len(thedata[0])
HEIGHT = len(thedata)

def value(irow,icol) -> int:
    return int(thedata[irow][icol])

def isInBoundary(irow,icol) -> bool:
    if (irow >= 0) and (irow < HEIGHT) and (icol >= 0) and (icol < WIDTH):
        return True
    return False

checks = [(-1,0),(0,1),(1,0),(0,-1)]
# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

def isLowPoint(irow,icol):
    ival = value(irow,icol)
    for check in checks:
        icrow, iccol = irow+check[0], icol+check[1]
        if isInBoundary(icrow,iccol):
            icheckval = value(icrow,iccol)
            if ival >= icheckval:
                return False
    return True




START = time.perf_counter()

lows = []
lowvals = []
for irow in range(0,HEIGHT):
    for icol in range(0,WIDTH):
        if isLowPoint(irow,icol):
            lows.append((irow,icol))
            lowvals.append( value(irow,icol) )

print(f"Low points: {lows}")
riskvals = [x+1 for x in lowvals]
print(f"Risks: {riskvals}")
print(f"Sum risk={sum(riskvals)}")




END = time.perf_counter()
print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

basins = []   # should result in same array size as lows, corresponding indexes
basincount = []

for lowpt in lows:
    inbasin = [  ]
    considerlist = collections.deque([ lowpt ])
    while len(considerlist) > 0:
        apt = considerlist.pop()
        if value(apt[0],apt[1]) != 9:
            if apt not in inbasin:
                inbasin.append(apt)

                # add in next points
                for check in checks:
                    newpt = (apt[0]+check[0], apt[1]+check[1])
                    if isInBoundary(newpt[0],newpt[1]):
                        if newpt not in inbasin:
                            considerlist.append(newpt)
    basins.append(inbasin)
    basincount.append(len(inbasin))



print("Basins:")
print(basins)
print("Basincount:")
print(basincount)


topthree = sorted(basincount, reverse=True)[0:3]
print(f"Product of top three:  {topthree[0]*topthree[1]*topthree[2]}")




END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")
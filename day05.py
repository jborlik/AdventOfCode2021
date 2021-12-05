#import itertools
#import numpy as np
#import copy
import re   
#import collections
import math
import time
import pprint


with open('day05.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".splitlines()]   # 


thedata = testdata
thedata = alldata

def processInput(arrdata, skipDiags=True):
    """Returns array of tuples( (int,int),(int,int)), for beginning and ending points"""
    r = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
    results = []
    for aline in arrdata:
        m = r.match(aline)
        vals = m.groups()
        if skipDiags:
            if not ( ( vals[0]==vals[2] ) or (vals[1]==vals[3]) ):
                continue
        results.append( ( int(vals[0]), int(vals[1]), int(vals[2]), int(vals[3])   ) )
    return results



sign = lambda x: 0 if x==0 else 1 if x>0 else -1


# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if True:

    START = time.perf_counter()
    
    lines = processInput(thedata, skipDiags=True)


    locs = {}
    for aline in lines:
        xdiff = aline[2] - aline[0]
        ydiff = aline[3] - aline[1]
        xincf = sign(xdiff)
        yincf = sign(ydiff)

        distance = max( abs(xdiff), abs(ydiff) )

        for ialong in range(0, distance+1):
            loc = (aline[0] + ialong*xincf,  aline[1] + ialong*yincf)
            lastval = locs.get(loc,0)
            locs[loc] = lastval+1

#    pprint.pprint(locs)

    def countIntersections(locs,limit=2):
        count = 0
        for k,v in locs.items():
            if v >= limit:
                count += 1
        return count

    count = countIntersections(locs)

    print(f"Number of intersections > 2:  {count}")


    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

lines = processInput(thedata, skipDiags=False)


locs = {}
for aline in lines:
    xdiff = aline[2] - aline[0]
    ydiff = aline[3] - aline[1]
    xincf = sign(xdiff)
    yincf = sign(ydiff)

    distance = max( abs(xdiff), abs(ydiff) )

    for ialong in range(0, distance+1):
        loc = (aline[0] + ialong*xincf,  aline[1] + ialong*yincf)
        lastval = locs.get(loc,0)
        locs[loc] = lastval+1

count = countIntersections(locs)

print(f"Number of intersections > 2:  {count}")



END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")
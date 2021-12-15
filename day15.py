#import itertools
import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field

import astar


with open('day15.txt') as datafile:
    alldata = np.array([list(map(int,x.strip())) for x in datafile.readlines()],dtype=int)

testdata = np.array([list(map(int,x.strip())) for x in """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".splitlines()],dtype=int)   # 


thedata = testdata
thedata = alldata

print(thedata)


# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if False:

    START = time.perf_counter()

    start, goal = (0,0),(thedata.shape[0]-1, thedata.shape[1]-1)
    grid = astar.GridWithWeights(width=thedata.shape[0], height=thedata.shape[1])
    grid.weights = thedata
    came_from, cost_so_far = astar.dijkstra_search(grid,start,goal)

    print(f"Cost so far: {cost_so_far[goal]}")
    
    path = astar.reconstruct_path(came_from, start=start, goal=goal)
    print(path)

    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

wrow = [ thedata + i for i in range(0,5)]
wrow = np.hstack(wrow)
wrow[ wrow >= 10 ] -= 9

allweights = wrow.copy()
for i in range(1,5):
    wnewrow = wrow + i
    wnewrow[ wnewrow >= 10] -= 9
    allweights = np.vstack([allweights,wnewrow])

# okay, got it

start, goal = (0,0),(allweights.shape[0]-1, allweights.shape[1]-1)
grid = astar.GridWithWeights(width=allweights.shape[0], height=allweights.shape[1])
grid.weights = allweights
came_from, cost_so_far = astar.dijkstra_search(grid,start,goal)

print(f"Cost so far: {cost_so_far[goal]}")

path = astar.reconstruct_path(came_from, start=start, goal=goal)
print(path)


END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")
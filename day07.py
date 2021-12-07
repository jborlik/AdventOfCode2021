#import itertools
import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections
#import math
import time
#import pprint


with open('day07.txt') as datafile:
    alldata = [int(x) for x in datafile.readline().split(',')]

testdata = [int(x) for x in """16,1,2,0,4,2,7,1,2,14""".split(',')]   # 


thedata = testdata
thedata = alldata

#print(thedata)

thedata = np.array(thedata)

# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

def getFuelToPos(arrcrab, toloc):
    totalfuel = 0
    for acrab in arrcrab:
        totalfuel += abs(acrab - toloc)
    return totalfuel


if False:

    START = time.perf_counter()

    minloc, minfuel = 0, 10000000000
    for iloc in range(np.min(thedata), np.max(thedata)+1):
        thefuel = getFuelToPos(thedata,iloc)
        if thefuel < minfuel:
            minloc = iloc
            minfuel = thefuel

    print(f"Minfuel = {minfuel} at location {minloc}")

    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

costs = [0]
for i in range(1,5000):
    costs.append(costs[-1] + i)
costs = np.array(costs)

def getFuelToPos2(arrcrab, toloc):
    totalfuel = 0
    for acrab in arrcrab:
        totalfuel += costs[abs(acrab - toloc)]
    return totalfuel


minloc, minfuel = 0, 10000000000
for iloc in range(np.min(thedata), np.max(thedata)+1):
    thefuel = getFuelToPos2(thedata,iloc)
    if thefuel < minfuel:
        minloc = iloc
        minfuel = thefuel

print(f"Minfuel = {minfuel} at location {minloc}")



END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")
#import itertools
#import numpy as np
import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections
#import math
import time
#import pprint


with open('day03.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".splitlines()]   # 


thedata = testdata
thedata = alldata


def countsOfColumn(thedata, icol):
    """Returns the counts of 0 and 1 for all rows, for column icol"""
    counts = [0,0]
    for arow in thedata:
        ival = int(arow[icol])
        counts[ival] += 1
    return counts
    
# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------


START = time.perf_counter()

ilen = len(thedata[0])
gamma = ""
epsilon = ""
for i in range(ilen):
    num0, num1 = countsOfColumn(thedata,i)
    print(i,num0,num1)
    if num0 > num1:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

igamma = int(gamma,base=2)
iepsilon = int(epsilon,base=2)
print(f"gamma={gamma} -> {igamma}")
print(f"epsilon={epsilon} -> {iepsilon}")
print(f"Power consumption result = {iepsilon*igamma}")



END = time.perf_counter()
print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

oxylist = copy.copy(thedata)


for i in range(ilen):
    # oxy
    num0, num1 = countsOfColumn(oxylist,i)
    icommon = 0 if num0 > num1 else 1
    newlist = []
    for arow in oxylist:
        if arow[i] == str(icommon):
            newlist.append(arow)
    oxylist = newlist
    if len(oxylist) == 1:
        break

oxyval = oxylist[0]
ioxyval = int(oxyval,base=2)

print(f"oxyval={oxyval} -> {ioxyval}")

co2list = copy.copy(thedata)

for i in range(ilen):
    # oxy
    num0, num1 = countsOfColumn(co2list,i)
    icommon = 1 if num0 > num1 else 0
    newlist = []
    for arow in co2list:
        if arow[i] == str(icommon):
            newlist.append(arow)
    co2list = newlist
    if len(co2list) == 1:
        break

co2val = co2list[0]
ico2val = int(co2val,base=2)

print(f"co2val={co2val} -> {ico2val}")
print(f"Life support result = {ioxyval*ico2val}")






END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")
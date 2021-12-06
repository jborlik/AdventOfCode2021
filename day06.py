#import itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections
#import math
import time
import pprint
from collections import Counter


with open('day06.txt') as datafile:
    alldata = [int(x) for x in datafile.readline().split(',')]

testdata = [int(x) for x in "3,4,3,1,2".split(',')]   # 


thedata = testdata
thedata = alldata

#print(thedata)
#backup = copy.deepcopy(thedata)

# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if False:

    START = time.perf_counter()
    DAYSPART1 = 80

    days = DAYSPART1



    lastfish = 0
    for iday in range(1,days+1):
        inumadded = 0
        for i,val in enumerate(thedata):
            if val == 0:
                inumadded += 1
                thedata[i] = 6
            else:
                thedata[i] -= 1
        thedata.extend( [8] * inumadded )
        incfrac = 1.0 if lastfish == 0 else (len(thedata) - lastfish)/lastfish
        print(f"day {iday}: fish = {len(thedata)}, delta = {len(thedata)-lastfish}, inc = {incfrac}")
        lastfish = len(thedata)
        #print(f"day {iday}: {thedata}")

    print(f"After {iday} days, number of fishes = {len(thedata)}")


    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

bins = Counter(thedata)
print(bins)

for iday in range(1,256+1):
    newday = {}
    for ikey, ival in bins.items():
        if ikey == 0:
            newday[8] = ival
            newday[6] = ival  + newday.get(6,0)
        else:
            newday[ikey-1] = ival + newday.get(ikey-1,0)  # we might have set 6 already
    print(f"Day {iday}: {sum(newday.values())}: ") #, end='')
    #pprint.pprint(newday)

    bins = newday

print(f"After {iday} days, number of fishes = {sum(bins.values())}")



END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")
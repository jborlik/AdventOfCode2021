#import itertools
#import numpy as np
import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field


with open('day12.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".splitlines()]   # 


thedata = testdata
thedata = alldata


def parseTree(thedata) -> dict:
    nodes = {}
    for aline in thedata:
        vals = aline.split('-')
        nodelist = nodes.get(vals[0], [])
        nodelist.append(vals[1])
        nodes[vals[0]] = nodelist
        nodelist = nodes.get(vals[1], [])
        nodelist.append(vals[0])
        nodes[vals[1]] = nodelist        

    return nodes


nodes = parseTree(thedata)

#print(nodes)

# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------


if True:

    START = time.perf_counter()

    completedpaths = []

    def followpath(apath, thisnode, allowedcave=''):
        apath.append(thisnode)
        potentialpaths = nodes[thisnode]
        for nextnode in potentialpaths:

            if nextnode[0].islower():
                countnext = apath.count(nextnode)
                allowed = 1
                if (nextnode == allowedcave):
                    allowed = 2
                if countnext == allowed:
                    continue  #  if we are already at the limit, don't continue down this branch


            if nextnode == 'end':
                childpath = copy.deepcopy(apath)                    
                childpath.append('end')
                if childpath not in completedpaths:
                    completedpaths.append(childpath)
            else:
                childpath = copy.deepcopy(apath)
                followpath(childpath,nextnode, allowedcave)
        
    
    followpath([],'start')
    print( "\n".join([','.join(arr) for arr in completedpaths]))
#    print(completedpaths)
    print(f"Part 1:  Count of paths = {len(completedpaths)}")





    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

smallcaves = []
for acave in nodes.keys():
    if (acave[0].islower()) and (acave != 'start') and (acave != 'end'):
        smallcaves.append(acave)

completedpaths = []
for doublecave in smallcaves:
    followpath([],'start', doublecave)

# remove potential duplicates
#completedpaths = list(set(completedpaths))
print( "\n".join([','.join(arr) for arr in completedpaths]))
print(f"Part 2:  Count of paths = {len(completedpaths)}")



END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")
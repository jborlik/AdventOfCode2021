#import itertools
import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field


with open('day13.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".splitlines()]   # 


thedata = testdata
thedata = alldata

def parseData(thedata):
    """ Returns (initial) np array of points and list of (x/y, value) folds"""
    # keep a dict[(x,y)]=value
    linebreak = thedata.index('')
    ptlist = np.array([list(map(int,xy.split(','))) for xy in thedata[:linebreak]])

    maxx = np.max(ptlist[:,0])
    maxy = np.max(ptlist[:,1])


    pts = np.zeros( (maxx+1,maxy+1), dtype=int)
    for pt in ptlist:
        pts[pt[0],pt[1]] = 1

    folds = [(s[11],int(s[13:])) for s in thedata[linebreak+1:]]
    
    return pts, folds


pts, folds = parseData(thedata)


def fold(isxy:str, foldpos:int, pts:np.array) -> np.array:
    if isxy=='x':
        newarray = np.copy(pts[:foldpos,:])
        right = np.flipud(pts[foldpos+1:,:])
        xpos = newarray.shape[0] - right.shape[0]
        if xpos < 0:
            print(f"YIKES!  xpos={xpos}")
        newarray[xpos:,:] += right
        return newarray

    else:  #isxy='y'
        newarray = np.copy(pts[:,:foldpos])
        bottom = np.fliplr(pts[:,foldpos+1:])
        ypos = newarray.shape[1] - bottom.shape[1]
        if ypos < 0:
            print(f"YIKES!  ypos={ypos}")
        newarray[:,ypos:] += bottom
        return newarray


# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if True:

    START = time.perf_counter()

    foldins = folds[0]
    newarray = fold( foldins[0], foldins[1], pts)

    count = (newarray.transpose() > 0).sum()

    print(f"Part 1:  Count of dots after first fold = {count}")



    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

import matplotlib.pyplot as plt

newarray = pts
for foldins in folds:
    newarray = fold( foldins[0], foldins[1], newarray)

plt.imshow(newarray.transpose() > 0)
plt.show()

END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")
#import itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections
#import math
import time
#import pprint


with open('day02.txt') as datafile:
    alldata = [x.strip().split(' ') for x in datafile.readlines()]

testdata = [x.strip().split(' ') for x in """forward 5
down 5
forward 8
up 3
down 8
forward 2""".splitlines()]   # 


thedata = testdata
thedata = alldata
#print(thedata)


# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------


START = time.perf_counter()

pos = [0,0]   # forward, depth
for cmd in thedata:
    if cmd[0]=='down':
        pos[1] += int(cmd[1])
    elif cmd[0]=='up':
        pos[1] -= int(cmd[1])
    elif cmd[0]=='forward':
        pos[0] += int(cmd[1])
    else:
        raise f"What is {cmd}???"

print(pos)
print(pos[0]*pos[1])


END = time.perf_counter()
print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()


pos = [0,0,0]   # forward, depth, aim
for cmd in thedata:
    if cmd[0]=='down':
        pos[2] += int(cmd[1])
    elif cmd[0]=='up':
        pos[2] -= int(cmd[1])
    elif cmd[0]=='forward':
        pos[0] += int(cmd[1])
        pos[1] += pos[2] * int(cmd[1])
    else:
        raise f"What is {cmd}???"

print(pos)
print(pos[0]*pos[1])


END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")
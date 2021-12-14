import itertools
from typing import Counter
import more_itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field


with open('day14.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".splitlines()]   # 


thedata = testdata
#thedata = alldata

def parseData(thedata):
    template = thedata[0]
    instructions = { x[0:2]: x[6] for x in thedata[2:]}
    return template, instructions

template, instructions = parseData(thedata)



# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

def applyRules(theline:str) -> str:
    newseq = []
    ifirst = True
    for pair in more_itertools.pairwise(theline):
        key = ''.join(pair)
        toinsert = instructions[key]
        if ifirst:
            newseq.append(pair[0])
            ifirst = False
        newseq.extend([toinsert, pair[1]])
    return ''.join(newseq)


if False:

    START = time.perf_counter()

    theline = template
    print(f"Template:{theline}")
    for i in range(1,10+1):
        theline = applyRules(theline)
        #print(f"After step {i}:{theline}")
        print(f"After step {i}: length={len(theline)}")
    
    c = Counter(theline)
    mostcommon = c.most_common(1)
    leastcommon = c.most_common()[:-2:-1]
    #print(mostcommon,leastcommon)
    print(f"Difference between most common {mostcommon} and least common {leastcommon}:")
    print(mostcommon[0][1] - leastcommon[0][1])

    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------




START = time.perf_counter()

theline = template
print(f"Template:{theline}")
for i in range(1,40+1):
    theline = applyRules(theline)
    #print(f"After step {i}:{theline}")
    print(f"After step {i}: length={len(theline)}")

c = Counter(theline)
mostcommon = c.most_common(1)
leastcommon = c.most_common()[:-2:-1]
#print(mostcommon,leastcommon)
print(f"Difference between most common {mostcommon} and least common {leastcommon}:")
print(mostcommon[0][1] - leastcommon[0][1])

END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")
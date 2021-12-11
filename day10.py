#import itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections
#import math
import time
#import pprint
from dataclasses import dataclass, field


with open('day10.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".splitlines()]   # 

validdata = [x.strip() for x in """()
[]
([])
{()()()}
<([{}])>
[<>({}){}[([])<>]]
(((((((((())))))))))
""".splitlines()]

#thedata = validdata
#thedata = testdata
thedata = alldata

score = {')': 3, ']': 57, '}': 1197, '>': 25137}

@dataclass
class Chunk:
    '''Class representing a chunk, has a start index, operator char, and children list'''
    start: int
    char: str
    children: list = field(default_factory=list)
    end: int = -1
    status: int = 0

    def write(self):
        print(self.char, end='')
        for child in self.children:
            child.write()
        if (self.status == 0) and (self.end > 0) and (self.char != ''):
            print(endchars[self.char], end='')

    def charExpected(self):
        if len(self.children) > 0:
            return self.children[-1].charExpected()
        return endchars[self.char]

    def charToComplete(self):
        retval = ''
        if len(self.children) > 0:
            retval += self.children[-1].charToComplete()
        if (self.char != '') and (self.status == 1):
            retval += endchars[self.char]
        return retval


startchars = '([{<'
chunkstatus = {0: 'ok', 1: 'incomplete', 2: 'error'}
endchars = {'(':')', '[':']', '{':'}', '<':'>'}

# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------
def parseLine(line:str):
    chunk = Chunk(0, '')  # top level holder
    index = 0
    reading = True
    while reading:
        childchunk, index = parseChunk(line, index)
        chunk.children.append(childchunk)
        if childchunk.status != 0:
            # if there is an error, stop
            chunk.status = childchunk.status
            chunk.end = index
            reading = False
        elif index == len(line)-1:
            reading=False
            chunk.end = index
        else:
            index += 1  # advance and read the next
    return chunk, index


def parseChunk(line:str, startindex:int):
    chunk = Chunk(startindex, line[startindex])
    index = startindex
    reading = True
    while reading:
        index += 1
        if index >= len(line):
            # reached end of line before closing
            reading = False
            chunk.end = index
            chunk.status = 1 
        else:
            char = line[index]
            if char in startchars:
                childchunk, index = parseChunk(line, index)
                chunk.children.append(childchunk)
                if childchunk.status != 0:
                    # if there is an error, stop
                    chunk.status = childchunk.status
                    chunk.end = index
                    reading = False
            elif char == endchars[chunk.char]:
                # got the closer
                chunk.end = index
                reading = False
            elif char in endchars.values():
                # closing something else... corrupted!
                reading = False
                chunk.status = 2
                chunk.end = index

    return chunk, index

def scoreString(line):
    compscore = {')': 1, ']': 2, '}': 3, '>': 4}
    score = 0
    for achar in line:
        score *= 5
        score += compscore[achar]
    return score



START = time.perf_counter()

points = 0
incompletes = []

for line in thedata:
    chunk, index = parseLine(line)
    print(f"Made it to pos={index}/{len(line)-1}.  Status={chunkstatus[chunk.status]}")
    print(line)
    chunk.write()
    if chunk.status == 2:
        print(f"\nExpected {chunk.charExpected()}, but found {line[chunk.end]} instead", end='')
        points += score[line[chunk.end]]
    if chunk.status == 1:
        tocomplete = chunk.charToComplete()
        compscore = scoreString(tocomplete)
        incompletes.append( compscore )
        print(f"\nNeeded to complete:{tocomplete} -> score={compscore}", end='')
    print('\n----------------')
#print(chunk)

print(f"Total points = {points}")

END = time.perf_counter()
print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

sortedscores = sorted(incompletes)
print(sortedscores)

imid = int((len(sortedscores)-1)/2)
print(f"Midpoint completion score={sortedscores[imid]}")



END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")
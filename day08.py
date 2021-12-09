import itertools
import numpy as np
import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections
#import math
import time
#import pprint


with open('day08.txt') as datafile:
    alldata = [x.split('|') for x in datafile.readlines()]

testdata = [x.split('|') for x in """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".splitlines()]   # 


thedata = testdata
#thedata = alldata

thedata = np.array(thedata)
signals = [ x.split() for x in thedata[:,0]]
outputs  = [ x.split() for x in thedata[:,1]]

#           0, 1, 2, 3, 4, 5, 6, 7, 8, 0
digcount = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]   # uniques: 1,4,7,8
uniquecounts = {2: 1, 3: 7, 4: 4, 7: 8}

# 0000
#1    2
#1    2
# 3333
#4    5
#4    5
# 6666
digits = {0: [0,1,2,4,5,6],     1:  [2,5],      2: [0,2,3,4,6],
          3: [0,2,3,5,6],       4:  [1,2,3,5],  5: [0,1,3,5,6],
          6: [0,1,3,4,5,6],     7:  [0,2,5],    8: [0,1,2,3,4,5,6],
          9: [0,1,2,3,5,6] }


# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if True:

    START = time.perf_counter()

    uniques = 0
    for adisplay in outputs:
        for aval in adisplay:
            if len(aval) in uniquecounts.keys():
                uniques += 1


    print(f"Number of uniques = {uniques}")

    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

# for test purposes
signals = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'.split()]
outputs = ['cdfeb fcadb cdfeb cdbaf'.split()]

def pruneOptions(letteroptions, letter, knownnumber):
    arroptions = letteroptions[letter]  # these are the available options currently
    digitpositions = digits[knownnumber]

    todelete = []
    for iposition in arroptions:
        if iposition not in digitpositions:
            todelete.append(iposition)
    for delitem in todelete:
        print(f"--pruning {letter} position {delitem}")
        arroptions.remove(delitem)


for arrinput,arroutput in zip(signals,outputs):
    # 10 inputs, 4 outputs
    letteroptions = {letter: list(range(7)) for letter in 'abcdefg'}

    # get the knowns/uniques
    for oneinput in itertools.chain(arrinput,arroutput):
        gotnum = uniquecounts.get(len(oneinput),-1)
        if gotnum >= 0:
            print(f"{oneinput}={gotnum}.")
            for aletter in oneinput:
                pruneOptions(letteroptions,aletter,gotnum)

    print(letteroptions)



#    for ainput




END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")
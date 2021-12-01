import itertools
import numpy as np

with open('day01.txt') as datafile:
    alldata = [int(x.strip()) for x in datafile.readlines()]

testdata = [199,
200,
208,
210,
200,
207,
240,
269,
260,
263]   

#alldata = testdata

TARGET = 7

diff = np.diff(alldata)
diffg0 = diff > 0
#print(alldata)
#print(diff)
#print(diffg0)
print("PART 1")
print(np.count_nonzero(diffg0))


#----------------------
print("PART 2")
def sliding_window(arr, window=3):
    i = iter(arr)
    a = []
    for e in range(0, window): a.append(next(i))
    yield a
    for e in i:
        a = a[1:] + [e]
        yield a

windows = sliding_window(alldata, window=3)
winvals = []
for win in windows:
    winvals.append(sum(win))

winvals = np.array(winvals)
diff = np.diff(winvals)
diffg0 = diff > 0
print(np.count_nonzero(diffg0))
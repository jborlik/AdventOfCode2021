# AdventOfCode2021

Python code to solve daily puzzles of http://adventofcode.com/2021

Code is tested with Python 3.9.7 (Anaconda distribution) on Win10. Developed with VSCode.

## Days

* Day 1:  Numpy functions for computing array differences.  Stumbled a bit with a sliding array on part 2.  I got to it late, but it took only a couple of minutes.
* Day 2:  Simple command processor.  Finished  part 1 in 00:06:12, rank 4197, and part 2 in 00:08:58, rank 3473.
* Day 3:  Iterate through a list to compare bits.  Gosh a lot of code (straightforward), but I suspect that the people who did it in 10 minutes had some insight.  Part 1:  00:15:32, rank 5439.  Part 2: 00:32:18, rank 2813.
* Day 4:  Bingo!  I used numpy for row/col comparisons, but there was still a lot of code.  Part 1: 00:44:55, rank  4466.  Part 2: 01:05:44, rank 4869.
* Day 5:  Counting the times that a line enters into a cell.  Straightforward using the trick of tracking a dict of tuple(x,y) points for keys and number of times referenced as values.  Part 1:  00:39:29, rank 5363.  Part 2: 00:47:59, rank  3980.
* Day 6:  Growth/doubling cycles.  Did it the naive way (modeling each item/fish separately in the manner described in the instructions) for part 1, but that was not nearly fast enough as the number of items grew.  The trick was to bin the items (using collections.Counter/dict) and manage them as groups.    Part 1: 00:11:41, rank 3861.  Part 2: 00:44:57, rank 5412.
* Day 7:  Find point that has the minimum distance to all datapoints.  Part 2 had a stranger distance function, but precomputed some distance values.  (No time/rank due to the page being disabled!  Finished in about 30 min, though.)
* TODO Day 8:  Got part 1, didn't get part 2!!!  Have to deduce numbers represented by 7-line shapes.
* Day 9:  Finding the low points given a 2D array of heights, and then (part 2) find the basins that surround the low points.  Did it with just basic python, but a numpy solution would maybe have been nicer (+ visualization would be easier).  Finished in about 45 minutes.
* Day 10:  Parse a tree of open/close markup, and find errors and incompleteness.  Used dataclass for the tree node (Chunk). It took me almost two hours, and I am amazed that some did it in about ten minutes.  Looking at some of the other solutions on Reddit, a much easier implementation would have been to use a single stack rather than developing the entire parse tree.
* Day 11:  Integer np matrix to track "energy levels" at positions, with rules to propagate to neighbors after they reached a certain level.  Part 2 was continuing the process until they all blinked at the same time.



## See previous work at:
* https://github.com/jborlik/AdventOfCode2015
* https://github.com/jborlik/AdventOfCode2016
* https://github.com/jborlik/AdventOfCode2017
* https://github.com/jborlik/AdventOfCode2018
* https://github.com/jborlik/AdventOfCode2019
* https://github.com/jborlik/AdventOfCode2020
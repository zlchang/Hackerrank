#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track
#

def gridlandMetro(n, m, k, track):
    # Write your code here
    f = {}
    for i in range(k):
        r = track[i][0]-1
        c1 = track[i][1]-1
        c2 = track[i][2]
        f.setdefault(r, []).append([c1, c2])
    cntr = 0
    for v in f.values():
        v.sort(key=lambda x: x[0])
        start = v[0][0]
        end = v[0][1]
        l = len(v)
        j = 1
        while j < l:
            if v[j][0] >= end:
                cntr += end-start
                start = v[j][0]
                end = v[j][1]
            else:
                end = max(v[j][1], end)
            j += 1
        cntr += end-start
    return n*m-cntr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()

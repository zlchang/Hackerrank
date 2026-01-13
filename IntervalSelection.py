#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'intervalSelection' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def intervalSelection(intervals):
    # Write your code here
    intervals.sort(key=lambda x: x[1])
    prev, limit = 0, 0
    res = 0
    for a, b in intervals:
        if a > prev:
            res += 1
            prev = b
        else:
            if a > limit:
                res += 1
                limit = prev
                prev = b
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        intervals = []

        for _ in range(n):
            intervals.append(list(map(int, input().rstrip().split())))

        result = intervalSelection(intervals)

        fptr.write(str(result) + '\n')

    fptr.close()

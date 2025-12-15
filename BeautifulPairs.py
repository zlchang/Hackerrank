#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#

def beautifulPairs(A, B):
    # Write your code here
    ta = {}
    for aa in A:
        if ta.get(aa) != None:
            ta[aa] += 1
        else:
            ta[aa] = 1
    cntr = 0
    for bb in B:
        if ta.get(bb) != None and ta[bb] > 0:
            cntr += 1
            ta[bb] -= 1
        else:
            ta[bb] = -1
    fa = False
    fb = False
    for vv in ta.values():
        if vv == 1:
            fa = True
        if vv < 0:
            fb = True
    if fa and fb:
        cntr += 1
    else:
        cntr -= 1
    return cntr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()

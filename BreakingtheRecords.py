#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mm = scores[0]
    nn = scores[0]
    cm = 0
    cn = 0
    for ii in range(len(scores)-1):
        jj = ii+1
        ss = scores[jj]
        if ss > mm:
            mm = ss
            cm += 1
        if ss < nn:
            nn = ss
            cn += 1
    return [cm, cn]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

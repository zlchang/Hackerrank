#!/bin/python3

import math
import os
import random
import re
import sys
def binarySearch(v, a, s, e):
    if e < s:
        return s
    m = (s+e)//2
    #print(m)
    if v > a[m]:
        return binarySearch(v, a, s, m-1)
    elif v < a[m]:
        return binarySearch(v, a, m+1, e)
    else:
        return m



# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    ladder = []
    rr = 1
    i = len(alice) - 1
    j = 0
    while i >= 0:
        if j == len(scores) or alice[i] >=scores[j]:
            ladder.append(rr)
            i -= 1
        else:
            if j == 0 or scores[j] < scores[j-1]:
                rr += 1
            j += 1

    return reversed(ladder)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

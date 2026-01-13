#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoRobots' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. 2D_INTEGER_ARRAY queries
#

def twoRobots(m, queries):
    # Write your code here
    n = len(queries)
    save = [0]*(m+1)
    msave = 0
    total = abs(queries[0][0]-queries[0][1])
    for i in range(1, n):
        prev = queries[i-1][1]
        ai, bi = queries[i]
        di = abs(bi-ai)
  
        dp = abs(prev-ai)+di
        for j in range(0, m+1):
            dj = di 
            if j > 0:
                dj += abs(j-ai)
            save[prev] = max(save[prev], save[j]+dp-dj)
        msave = max(msave, save[prev])
        total +=  dp
        #print(save)
    res = total - msave
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for _ in range(t):
        first_multiple_input = input().rstrip().split()

        m = int(first_multiple_input[0])

        n = int(first_multiple_input[1])

        queries = []

        for _ in range(n):
            queries.append(list(map(int, input().rstrip().split())))
        
        result = twoRobots(m, queries)
        fptr.write(str(result) + '\n')

    fptr.close()

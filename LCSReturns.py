#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'tutzkiAndLcs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def tutzkiAndLcs(a, b):
    # Write your code here
    n = len(a)
    m = len(b)
    #normal
    cntr = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                cntr[i][j] = cntr[i-1][j-1]+1
            else:
                cntr[i][j] = max(cntr[i-1][j], cntr[i][j-1])
    lcs = cntr[n][m]
    #print(lcs)
    #reverse
    rcntr = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if a[i] == b[j]:
                rcntr[i][j] = rcntr[i+1][j+1]+1
            else:
                rcntr[i][j] = max(rcntr[i+1][j], rcntr[i][j+1])
    rlcs = rcntr[0][0]
    #print(rlcs)
    res = 0
    for i in range(n+1):
        temp = set()
        for j in range(m):
            if b[j] in temp:
                continue
            if cntr[i][j]+rcntr[i][j+1] == lcs:
                temp.add(b[j])
                res += 1
    #res = cntr[m]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    result = tutzkiAndLcs(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()

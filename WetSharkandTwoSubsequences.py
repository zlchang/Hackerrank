#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoSubsequences' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER r
#  3. INTEGER s
#

def twoSubsequences(x, r, s):
    # Write your code here
    mod = 1000000007
    m = len(x)
    mr = r+1
    xsum = [[0 for i in range(mr)] for j in range(m)]
    for i in range(m):
        for j in range(i, 0, -1):
            for k in range(mr):
                if k+x[i] < mr:
                    xsum[j][k+x[i]] = (xsum[j][k+x[i]] + xsum[j-1][k]) % mod
                    if i == 1 and j==1 and xsum[j-1][k] != 0:
                        print(i, x[i], j, k, k+x[i], xsum[j-1][k])
        if x[i] < mr:
            xsum[0][x[i]] += 1
    sa = (r+s) // 2
    sb = (r-s) // 2
    print(sa, sb)
    res = 0
    if (r+s) % 2 or r < s or (r-s) % 2:
        return res
    for i in range(m):
        na = xsum[i][sa]
        nb = xsum[i][sb]
        #print(i, na, nb)
        if sb == 0:
            res = (res + na*na) % mod
        else:
            res = (res + na*nb) % mod
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    r = int(first_multiple_input[1])

    s = int(first_multiple_input[2])

    x = list(map(int, input().rstrip().split()))

    result = twoSubsequences(x, r, s)

    fptr.write(str(result) + '\n')

    fptr.close()

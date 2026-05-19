#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
nmax = 10**5+1
dvs = [[] for i in range(nmax)]
memo = [-1]*nmax
def grundy(x):
    if x == 0:
        memo[0] = 0
        return 0
    if x == 1:
        memo[1] = 0
        return 0
    if memo[x] != -1:
        return memo[x]
    mex = set()
    for i in dvs[x]:
        if x % i != 0:
            continue
        j = x // i
        gr = 0
        if i % 2 != 0:
            gr = grundy(j)
        mex.add(gr)
    r = 0
    while r in mex:
        r = r+1
    memo[x] = r
    return r

def towerBreakers(arr):
    #print(nfactor(9))
    # Write your code here
    res = 0
    for a in arr:
        b = grundy(a)
        #print(a, b)
        #print(dvs[a])
        res = res ^ b
    if res == 0:
        return 2
    return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for i in range(2, nmax):
        j = i
        while j < nmax:
            dvs[j].append(i)
            j += i
    grundy(nmax-1)
    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = towerBreakers(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'candlesCounting' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY candles
#
mod = 10**9+7
def update(num, tree, index, val):
    i = index + 1
    while i <= num:
        tree[i] = (tree[i]+val) % mod
        #print(i, color, tree[i][color])
        i += i & (-i)
def getSum(num, tree, index):
    s = 0
    i = index + 1
    while i > 0:
        s = (s + tree[i]) % mod
        i -= i & (-i)
    return s
def candlesCounting(k, candles):
    # Write your code here
    m = 1 << k
    n = len(candles)
    h = max([i[0] for i in candles])
    #print(m, n, h)
    cntr = [0 for i in range(h+1)]
    res = 0
    for l in range(m):
        sl = 0
        for i in range(n):
            hi = candles[i][0]-1
            ci = candles[i][1]-1
            if l >> ci & 0x1:
                temp = getSum(h, cntr, hi-1)
                sl += 1+temp
                update(h, cntr, hi, 1+temp)
        #sl = getSum(h, cntr, h-1)
        for i in range(h+1):
            cntr[i] = 0
        #print(sl, l.bit_count())
        if (k - l.bit_count()) % 2:
            res = (res+mod-sl) % mod
        else:
            res = (res+sl) % mod           
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    candles = []

    for _ in range(n):
        candles.append(list(map(int, input().rstrip().split())))

    result = candlesCounting(k, candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extremumPermutations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#
mod = 10**9+7

def extremumPermutations(n, a, b):
    # Write your code here
    fa = [0 for i in range(n)]
    for i in a:
        fa[i-1] = 1
    fb = [0 for i in range(n)]
    for i in b:
        fb[i-1] = 1
    pm = [0 for i in range(n)]
    spm = [0 for i in range(n+1)]
    pm[0] = 1
    spm[0] = 0
    spm[1] = 1
    for i in range(1, n):
        if (fa[i] and fb[i]) or (fa[i] and fa[i-1]) or (fb[i] and fb[i-1]):
            return 0
        for j in range(i+1):
            if fa[i] or fb[i-1]:
                pm[j] = spm[j]
            elif fa[i-1] or fb[i]:
                pm[j] = (spm[i]-spm[j]) % mod
            else:
                pm[j] = spm[i]
        #calculate sum for i-1
        #print(pm)
        #spm[0] = 0
        for j in range(1, i+2):
            spm[j] = (spm[j-1]+pm[j-1]) % mod
        #print(spm)
    res = spm[n]
    return res        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    l = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = extremumPermutations(n, a, b)

    fptr.write(str(result) + '\n')

    fptr.close()

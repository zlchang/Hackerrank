#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonetrousle' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. LONG_INTEGER n
#  2. LONG_INTEGER k
#  3. INTEGER b
#

def bonetrousle(n, k, b):
    # Write your code here
    m = n - (1+b)*b//2
    c = k - b
    res = [0]*b
    if m < 0 or m > b*c:
        return [-1]
    elif m == 0:
        for i in range(b):
            res[i] = i+1
    elif m == b*c:
        for i in range(b):
            res[i] = k-b+i+1
    else:
        q = m // c
        r = m % c
        #print(f'm={m} c={c}, q={q}, r={r}')
        for i in range(b):
            if i < b-q-1:
                res[i] = i+1
            elif i > b-q-1:
                res[i] = i+1+c
            else:
                res[i] = i+1+r
    return res

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        b = int(first_multiple_input[2])

        result = bonetrousle(n, k, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

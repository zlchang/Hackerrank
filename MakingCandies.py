#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumPasses' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER m
#  2. LONG_INTEGER w
#  3. LONG_INTEGER p
#  4. LONG_INTEGER n
#

def minimumPasses(m, w, p, n):
    # Write your code here
    if p > n:
        return math.ceil(n/(m*w))
    cntr = 0
    total = 0
    while total < n:
        temp = math.ceil((n-total) / (m*w))
        if total < p:
            tp = math.ceil((p-total)/(m*w))
            total += tp*(m*w)
            cntr += tp
            continue
        x = total // p
        r = total % p
        b = max((x+m-w)//2, 0)
        a = x-b
        if a < 0:
            a = 0
            b = x
        mp = m+a
        wp = w+b
        #print(m, w, total)
        if temp < math.ceil((n-r) / (mp*wp)):
            return cntr+temp
        total = mp*wp+r
        m = mp
        w = wp
        cntr += 1
    return cntr
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    p = int(first_multiple_input[2])

    n = int(first_multiple_input[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()

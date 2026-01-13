#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):
    # Write your code here
    n = len(arr)
    cntr = 0
    i = 0
    while i < n:
        pos = -1
        a = max(0, i-k+1)
        b = min(i+k-1, n-1)
        for j in range(b, a-1, -1):
            if arr[j] == 1:
                pos = j
                break
        if pos == -1:
            return -1
        cntr += 1
        i = pos + k
    return cntr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

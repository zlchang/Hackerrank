#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    mm = max(a)
    nn = min(b)
    ff = nn//mm

    counter = 0
    for i in range(ff):
        flag = 0
        tt = mm*(i+1)
        for aa in a:
            if tt%aa != 0:
                flag = 1
                break
        for bb in b:
            if bb%tt != 0:
                flag = 1
                break
        if flag == 0:
            counter += 1

    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

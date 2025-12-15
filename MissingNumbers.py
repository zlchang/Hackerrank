#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Write your code here
    flag = {}
    crr = []
    for aa in arr:
        if aa in flag.keys():
            flag[aa] += 1
        else:
            flag[aa] = 1
    for bb in brr:
        if bb in flag.keys():
            flag[bb] -= 1
        else:
            crr.append(bb)
    for kk in flag.keys():
        if flag[kk] != 0:
            crr.append(kk)
    crr.sort()
    return crr
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

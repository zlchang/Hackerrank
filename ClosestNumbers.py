#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def sortSecond(val):
    return val[1] 
def closestNumbers(arr):
    # Write your code here
    arr.sort()
    n = len(arr)
    diff = [0]*(n-1)
    for i in range(1, n):
        diff[i-1] = arr[i]-arr[i-1]
    pair = list(zip(arr[:-1], diff))
    pair.sort(key=sortSecond)
    pmin = pair[0][1]
    res = [];
    for i in range(0,n-1):
        dd = pair[i][1]
        aa = pair[i][0]
        bb = aa+dd
        if dd == pmin:
            res.append(aa)
            res.append(bb)
        else:
            break
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

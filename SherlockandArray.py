#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    n = len(arr)
    lsum = [0]*n
    rsum = [0]*n
    for ii in range(1,n):
        lsum[ii] = lsum[ii-1]+arr[ii-1]
    for jj in range(1, n):
        rsum[n-jj-1] = rsum[n-jj]+arr[n-jj]
    for ii in range(0,n):
        if lsum[ii] == rsum[ii]:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()

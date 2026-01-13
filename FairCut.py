#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairCut' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def fairCut(k, arr):
    # Write your code here
    n = len(arr)
    arr.sort()
    
    sarr = [[0 for i in range(k+1)] for j in range(n+1)]
    sarr[0][0] = 0
    for i in range(1, n+1):
        ai  = arr[i-1]
        sarr[i][0] = sarr[i-1][0] - k*ai
    for i in range(1, n+1):
        ai = arr[i-1]
        for j in range(1, k+1):
            if j > i:
                continue
            x = sarr[i-1][j-1] + (i-j)*ai - (n-k-i+j)*ai #include
            if i == j:
                sarr[i][j] = x
            else:
                y = sarr[i-1][j] + j*ai - (k-j)*ai #exclude     
                sarr[i][j] = min(x, y)
    
    return sarr[n][k]
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = fairCut(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

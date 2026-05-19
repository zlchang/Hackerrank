#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):
    # Write your code here
    n = len(arr)
    dp = [0]*n
    tmax = arr[0]
    for i in range(1, n):
        if arr[i] > tmax:
            tmax = arr[i]
            dp[i] = i
        else:
            dp[i] = dp[i-1]
    cntr = 0
    i = n-1
    while dp[i] != 0:
        i = dp[i]-1
        cntr += 1        
    if cntr % 2 == 1:
        return 'ANDY'
    return 'BOB'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()

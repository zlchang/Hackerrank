#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(1000000)
#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#

def maximumSum(a, m):
    # Write your code here
    prefix = []
    prefix_sum = 0
    max_sum = 0
    n = len(a)
    for i in range(n):
        prefix_sum = (prefix_sum + a[i]) % m
        prefix.append((prefix_sum, i))
        max_sum = max(max_sum, prefix_sum)
    prefix.sort(key=lambda x: x[0])
    for i in range(n-1):
        if prefix[i+1][1] < prefix[i][1]:
            max_sum = max(max_sum, prefix[i][0]-prefix[i+1][0]+m)
            
    return max_sum
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()

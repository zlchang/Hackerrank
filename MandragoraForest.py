#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'mandragora' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY H as parameter.
#

def mandragora(H):
    # Write your code here
    n = len(H)
    msum = [0]*(n+1) 
    H.sort(reverse=True)
    for i in range(n):
        msum[i+1] = msum[i]+H[i] 
    res = 0
    for i in range(1, n+1):
        res = max(res, msum[i]*(n-i+1))
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        H = list(map(int, input().rstrip().split()))

        result = mandragora(H)

        fptr.write(str(result) + '\n')

    fptr.close()

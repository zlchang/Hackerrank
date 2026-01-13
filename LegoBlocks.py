#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    # Write your code here
    mod = 1000000007
    counter = [0]*(m+1)
    counter[0] = 1
    counter[1] = 1
    for i in range(2, m+1):
        if i < 5:
            counter[i] = 2*counter[i-1]
        else:
            counter[i] = 2*counter[i-1]-counter[i-5]
            counter[i] %= mod
    #print(counter)
    
    for i in range(m+1):
        counter[i] = pow(counter[i], n, mod)
    #print(counter)
    cgood = [0]*(m+1)
    cgood[0] = 0
    cgood[1] = counter[1]- cgood[0]*counter[1]
    for i in range(2, m+1):
        cgood[i] = counter[i]
        for j in range(1, i):
            cgood[i] = (cgood[i] - cgood[j]*counter[i-j]) % mod
    res = cgood[m]
    #print(cgood)
    return res
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

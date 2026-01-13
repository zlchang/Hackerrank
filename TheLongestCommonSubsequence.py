#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestCommonSubsequence' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def longestCommonSubsequence(a, b):
    # Write your code here
    n = len(a)
    m = len(b)
    
    cntr = [0]*(m+1)
    lcs = [[] for _ in range(m+1)]
    for i in range(1, n+1):
        prev = cntr[0]
        plcs = list(lcs[0])
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                temp = cntr[j]
                tlcs = list(lcs[j])
                cntr[j] = prev+1
                plcs.append(a[i-1])
                lcs[j] = list(plcs)
                #print(i,j,temp[j],lcs[j-1], curr[j])
                prev = temp
                plcs = list(tlcs)
            else:
                plcs = list(lcs[j])
                if cntr[j] <= cntr[j-1]:
                    lcs[j]= list(lcs[j-1])
                prev = cntr[j]
                cntr[j] = max(cntr[j], cntr[j-1])
            #print(lcs)
    res = cntr[m]
    print(res)
    return lcs[m]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = longestCommonSubsequence(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

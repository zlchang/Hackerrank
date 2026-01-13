#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#
mod = 10**9+7
def swapPermutation(n, k):
    # Write your code here
    padj = [[0 for i in range(k+1)] for j in range(n+1)]
    sadj = [0 for i in range(k+1)]
    for i in range(1, n+1):
        padj[i][0] = 1
        for j in range(1, k+1):
            if j < i:
                padj[i][j] = sadj[j]
            else:
                padj[i][j] = (sadj[j] - sadj[j-i]) % mod
        sadj[0] = padj[i][0]
        for j in range(1, k+1):
            sadj[j] = (sadj[j-1] + padj[i][j]) % mod 
    #print(padj)
    #print(sadj)
    s1 = 0
    for i in range(k, -1, -2):
        s1 = (s1 + padj[n][i]) % mod
    ####
    pswp = [[0 for i in range(k+1)] for j in range(n+1)]
    for i in range(1, n+1):
        pswp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):   
            pswp[i][j] = (pswp[i-1][j]+(i-1)*pswp[i-1][j-1]) % mod
    s2 = 0
    for i in range(k+1):
        s2 = (s2+pswp[n][i]) % mod
    return (s1, s2)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    result = swapPermutation(n, k)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

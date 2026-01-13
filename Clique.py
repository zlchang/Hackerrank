#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'clique' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
#Turan's Theorem, n vertices without a k (>=2) clique, edge counts = (1 - 1/k)*(n**2-s**2)/2 + s*(s-1)/2 where n = qk+s

def clique(n, m):
    # Write your code here
    k = n 
    f = n**2/2
    l = n*(n-1)/2
    if m > l:
        return n+1
    while k >= 2:
        t = n%(k-1)
        e = (1-1/(k-1))*(f-t*t/2)+ (t-1)*t/2
        if m > e:      
            return k
        k -= 1
    
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = clique(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

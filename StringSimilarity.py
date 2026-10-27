#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringSimilarity' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringSimilarity(s):
    # Write your code here
    n = len(s)
    z = [0 for _ in range(n)]
    z[0] = n
    l = 0
    r = 0
    for i in range(1, n):
        if r > i:
            z[i] = min(z[i-l], r-i+1)
        while i+z[i] < n and s[i+z[i]] == s[z[i]]:
            z[i] += 1
        if i+z[i]-1 > r:
            r = i+z[i]-1
            l = i
        print(i, z[i], l, r)
    res = sum(z)
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = stringSimilarity(s)

        fptr.write(str(result) + '\n')

    fptr.close()

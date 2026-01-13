#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
def lowercase(ch):
    if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
        return 1
    return 0
    
def abbreviation(a, b):
    # Write your code here
    na = len(a)
    nb = len(b)
    
    arr = [[0 for i in range(nb+1)] for j in range(na+1)]
    arr[0][0] = 1
    for i in range(1, na):
        arr[i][0] = (arr[i-1][0] and lowercase(a[i-1]))
        
    for i in range(1, nb+1):
        cb = b[i-1]
        for j in range(1, na+1):
            ca = a[j-1]
            if lowercase(ca):
                arr[j][i] = arr[j-1][i] or (arr[j-1][i-1] and (ord(ca)-ord('a') == ord(cb) - ord('A')))
            else:
                arr[j][i] = (cb == ca) and arr[j-1][i-1]
    if arr[na][nb] == 1:
        return 'YES'
    return 'NO'
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()

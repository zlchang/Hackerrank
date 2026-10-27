#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def merge(sa, sb):
    na = len(sa)
    nb = len(sb)
    nc = na+nb
    c = []
    i = 0
    j = 0
    cntr = 0
    for _ in range(nc):
        if j < nb and ((i < na and sa[i] > sb[j]) or i == na):
            cntr += na-i
            c.append(sb[j])
            j += 1
        elif i < na:
            c.append(sa[i])
            i += 1           
    return c, cntr

def shift(a):
    n = len(a)
    if n == 1:
        return a, 0
    nb = n//2
    la = a[0:nb]
    ra = a[nb:n]
    sa, ca = shift(la)
    sb, cb = shift(ra)
    sc, cc = merge(sa, sb)
    return sc, ca+cb+cc
def insertionSort(arr):
    # Write your code here
    sarr, result = shift(arr)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

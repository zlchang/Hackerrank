#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatsNext' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def whatsNext(arr):
    # Write your code here
    n = len(arr)
    if n == 1:
        if arr[0] == 1:
            return [1, 1]
        return [1, 1, arr[0]-1]
    if n == 2:
        if arr[0] == 1:
            return [1, 1+arr[1]]
        return [1, 1+arr[1], arr[0]-1]
    l = n-1
    if l % 2 == 1:
        l = l - 1
    #print(l)
    m = l+3
    brr = [0]*m
    for i in range(0, l-1):
        brr[i] = arr[i]
    if arr[l-1] == 1:
        brr[l-2] += 1
        brr[l-1] = 1 #1->0
        if arr[l] == 1:
            brr.pop(l+2)
            brr.pop(l+1)
            brr.pop(l)
        else:
            brr[l] = arr[l] - 1
            brr.pop(l+2)
            brr.pop(l+1)
        if l < n-1:
            brr[l-1] += arr[n-1]
    else:
        brr[l-1] = arr[l-1]-1
        brr[l] = 1
        if arr[l] == 1:
            brr[l+1] += 1
            brr.pop(l+2)
        else:
            brr[l+1] = 1
            brr[l+2] = arr[l]-1
        if l < n-1:
            brr[l+1] += arr[n-1]
    return brr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = whatsNext(arr)
        fptr.write('{:d}\n'.format(len(result)))
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()

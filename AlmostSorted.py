#!/bin/python3

import math
import os
import random
import re
import sys

def check(dd, arr, sarr):
    n = len(dd)
    for i in range(n):
        if arr[dd[i]] == sarr[dd[n-1-i]]:
            continue
        else:
            return False
    return True
# Complete the almostSorted function below.
def almostSorted(arr):

    sarr = sorted(arr)
    dd = []
    for i in range(len(arr)):
        if arr[i] != sarr[i]:
            dd.append(i)
    #print(dd)
    if len(dd) == 0:
        print("yes")
    elif len(dd) == 2:
        print("yes")
        print("swap {:d} {:d}".format(dd[0]+1, dd[1]+1))
    elif check(dd, arr, sarr):
        print("yes")
        print("reverse {:d} {:d}".format(dd[0]+1, dd[-1]+1))
    else:
        print('no')



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)

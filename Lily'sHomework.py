#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def numSwap(ixa):
    n = len(ixa)
    ff = [0]*n
    pa = [0]*n
    for i in range(n):
        pa[ixa[i]] = i
    #print(pa)
    cc = 0
    for i in range(n):
        j = i
        if ff[j] == 0: 
            cc += 1
            ff[j] = 1
            while pa[j] != i:
                j = pa[j]; 
                ff[j] = 1
    #print(pa)
    #print(ff)
    return n-cc
def lilysHomework(arr):
    # Write your code here
    n = len(arr)
    ixa = [i for i in range(n)]
    ixb = [i for i in range(n)]
    #print(ixa)
    ixa.sort(key=lambda a: arr[a], )
    ixb.sort(key=lambda a: arr[a], reverse=True)
    #print(ixa)
    na = numSwap(ixa)
    nb = numSwap(ixb)
    return na if na < nb else nb
 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

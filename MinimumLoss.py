#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    # Write your code here
    arr = []
    n = len(price)
    for ii in range(n):
        arr.append([price[ii], ii])
    arr.sort(key=lambda x: x[0])
    
    res = arr[0][0]-arr[1][0]
    for ii in range(1, n):
        ll = arr[ii-1][0]-arr[ii][0]
        if ll > res and arr[ii-1][1] > arr[ii][1]:
            res = ll
    return -res
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()

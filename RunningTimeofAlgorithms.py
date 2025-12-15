#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    n = len(arr)
    cntr = 0
    for i in range(n):
        a = arr[i]
        j = i-1
        while j >= 0 and a < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            cntr += 1
        arr[j+1] = a
        #print(cntr)
    return cntr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

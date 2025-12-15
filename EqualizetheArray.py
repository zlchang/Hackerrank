#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):

    count = {}
    for a in arr:
        if a not in count:
            count[a] = 1
        else:
            count[a] += 1
    mv = 0
    mk = 0
    for k, v in count.items():
        if v > mv:
            mv = v
            mk = k
    return len(arr)-mv

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

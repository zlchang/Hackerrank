#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    counter = {}
    for v in arr:
        if v in counter:
            counter[v] += 1
        else:
            counter[v] = 1
    mm = 0
    mid = 6
    for k, c in counter.items():
        #print (k,c, mm, mid)
        if c > mm:
            mm = c
            mid = k
        elif c == mm and k < mid:
                mid = k
    return mid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

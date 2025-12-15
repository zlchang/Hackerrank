#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    nc = len(c)
    step = [0]*nc

    step[0] = 0
    if c[1] == 0:
        step[1] = 1
    else:
     c[1] = 101
    for i in range(2, nc):
        if c[i] == 1:
            step[i] = 101
        else:
            step[i] = min(step[i-1], step[i-2])+1
        #print(step[i])
    return step[nc-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

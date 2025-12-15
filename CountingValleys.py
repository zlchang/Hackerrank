#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    total = 0
    counter = 0
    for ii in s:
        vv = 0
        if ii == 'U':
            vv = 1
        else:
            vv = -1
        total += vv
        if total == 0 and vv == 1:
            counter += 1
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

def reverse (n):
    q = n
    res = 0
    while q > 0:
        r = q % 10
        res = res*10 + r
        q = q//10
    return res
# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    good = 0
    for x in range(i, j+1):

        rx = reverse(x)
        d = abs(rx-x)
        if d % k == 0:
            good += 1
    return good

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()

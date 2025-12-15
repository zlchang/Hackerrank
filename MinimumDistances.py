#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    ra = {}
    n = len(a)
    res = []
    for i in range(n):
        v = a[i]
        if v not in ra:
            ra[v] = i
        else:
            d = i - ra[v]
            res.append(d)
    if len(res) == 0:
        return -1
    else:
        return min(res)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

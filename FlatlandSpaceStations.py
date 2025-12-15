#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    d = []
    s = sorted(c)
    a = s[0]
    for i in range(1, len(s)):
        d.append(s[i]-s[i-1])
    b = n-1-s[-1]

    m = 0
    if len(d) > 0:
        m = max(d) // 2

    return max(m, a, b)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()

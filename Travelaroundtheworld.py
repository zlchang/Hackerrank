#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'travelAroundTheWorld' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#  3. LONG_INTEGER c
#

def travelAroundTheWorld(a, b, c):
    # Write your code here
    n = len(a)
    d = [0]*n 
    # check if a city can be a start city
    s = 0
    tank = 0
    for i in range(2*n):
        tank += a[i%n]
        tank = min(tank, c)
        tank -= b[i%n]
        print(s, tank)
        if tank < 0:
            s = i+1
            tank = 0
    if s >= n:
        return 0
    res = 1
    need = [0]*n
    need[s] = 0
    for i in range(1, n):
        j = s-i
        if j < 0:
            j = (j+n)%n
        need[j] = max(0, need[(j+1)%n]+b[j]- min(c, a[j]))
        if need[j] == 0:
            res += 1
    return res
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = travelAroundTheWorld(a, b, c)

    fptr.write(str(result) + '\n')

    fptr.close()

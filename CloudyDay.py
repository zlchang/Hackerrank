#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

def maximumPeople(p, x, y, r):
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.
    n = len(p)
    m = len(y)
    city = []
    for i in range(n):
        city.append([x[i], p[i]])
    start_cloud = []
    end_cloud = []
    for i in range(m):
        l = max(1, y[i]-r[i])
        h = y[i]+r[i]
        start_cloud.append([i, l])
        end_cloud.append([i, h])
    start_cloud.sort(key=lambda x: x[1])
    end_cloud.sort(key=lambda x: x[1])
    city.sort(key=lambda x: x[0])
    sunny = 0
    cloudy = [0]*m
    candidate = set()
    i_start = 0
    i_end = 0
    for i in range(n):
        cc = city[i]
        while i_start < m:
            c_start = start_cloud[i_start]
            if cc[0] >= c_start[1]:
                candidate.add(c_start[0])
                i_start += 1
            else:
                break
        while i_end < m:
            c_end = end_cloud[i_end]
            if cc[0] > c_end[1]:
                candidate.discard(c_end[0])
                i_end += 1
            else:
                break
        nc = len(candidate)
        if nc == 0:
            sunny += cc[1]
        elif nc == 1:
            ic = next(iter(candidate))
            cloudy[ic] += cc[1]
    nmax = max(cloudy, default=0)
    res = sunny+nmax
    return res
    
    
    

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()

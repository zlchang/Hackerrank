#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'specialSubCubes' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY cube as parameter.
#
def index(x, y, z, n):
    return x*n*n + y*n + z
def specialSubCubes(n, cube):
    # Write your code here
    m = len(cube)
    cmax = [[0]*m for i in range(n)]
    res = []
    for i in range(m):
        cmax[0][i] = cube[i]
    cntr = 0
    for i in range(m):
        if cmax[0][i] == 1:
            cntr += 1
    res.append(cntr)
    steps = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1 ,1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
    for k in range(1, n):
        cntr = 0
        for x in range(n-k):
            for y in range(n-k):
                for z in range(n-k):
                    i = index(x, y, z, n)
                    for s in steps:
                        xs = x + s[0]
                        ys = y + s[1]
                        zs = z + s[2]
                        j = index(xs, ys, zs, n)
                        cmax[k][i] = max(cmax[k][i], cmax[k-1][j])
                    if cmax[k][i] == k+1:
                        cntr += 1
        res.append(cntr)
        #print(cntr)
    return res
                    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        cube = list(map(int, input().rstrip().split()))

        result = specialSubCubes(n, cube)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squareBoard' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY board as parameter.
#
m = 30
primes = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0]
memo = [[[[-1 for ia in range(m)] for ib in range(m)] for ja in range(m)] for jb in range(m)]
cntr = [[0 for i in range(m+1)] for j in range(m+1)]
def grundy(rmin, rmax, cmin, cmax):
    #print(b, nr, nc)
    nr = rmax - rmin
    nc = cmax - cmin
    if nr == 1 and nc == 1:
        memo[rmin][rmax-1][cmin][cmax-1] = 0
        return 0
    if memo[rmin][rmax-1][cmin][cmax-1] != -1:
        return memo[rmin][rmax-1][cmin][cmax-1]
    cc = cntr[rmax][cmax] - cntr[rmin][cmax] - cntr[rmax][cmin] + cntr[rmin][cmin]
    if cc == 0:
        memo[rmin][rmax-1][cmin][cmax-1] = 0
        return 0
    gn = set()
    for i in range(rmin, rmax-1):
        ga = grundy(rmin, i+1, cmin, cmax) 
        gb = grundy(i+1, rmax, cmin, cmax)
        gn.add(ga^gb)
    for i in range(cmin, cmax-1):
        ga = grundy(rmin, rmax, cmin, i+1)
        gb = grundy(rmin, rmax, i+1, cmax)
        gn.add(ga^gb)
    i = 0
    while i in gn:
        i += 1
    memo[rmin][rmax-1][cmin][cmax-1] = i
    #print(rmin, rmax, cmin, cmax, i)
    return i
    
        
def squareBoard(n):
    # Write your code here
    for ia in range(n):
        for ib in range(n):
            for ja in range(n):
                for jb in range(n):
                    memo[ia][ib][ja][jb] = -1
    #colp = [0]*n
    for i in range(1, n+1):
        for j in range(1, n+1):
            cntr[i][j] += cntr[i-1][j]
    for i in range(1, n+1):
        for j in range(1, n+1):
            cntr[i][j] += cntr[i][j-1]
            
    res = grundy(0, n, 0, n)
    if res == 0:
        return 'Second'
    return 'First'
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        for i in range(n):
            j = 0
            for a in list(map(int, input().rstrip().split())):
                cntr[i+1][j+1] = (primes[a] == 0)
                j += 1
        result = squareBoard(n)

        fptr.write(result + '\n')

    fptr.close()

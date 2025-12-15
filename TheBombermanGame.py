#!/bin/python3

import math
import os
import random
import re
import sys
def neighbor(a, b, grid):
    p = len(grid)
    q = len(grid[0])
    if a-1 >=0 and grid[a-1][b] == 'O':
        return 'O'
    if a+1 < p and grid[a+1][b] == 'O':
        return 'O'
    if b-1 >= 0 and grid[a][b-1] == 'O':
        return 'O'
    if b+1 < q and grid[a][b+1] == 'O':
        return 'O'
    return '.'

        

# Complete the bomberMan function below.
def bomberMan(n, grid):
    if n == 1:
        return grid
    l = len(grid)
    m = len(grid[0])
    s1 = []
    for i in range(l):
        arr = ''
        for j in range(m):
            arr += 'O'
        s1.append(arr)
    if n == 2:
        return s1
    s2 =[]
    for i in range(l):
        arr =''
        for j in range(m):
            s = grid[i][j]
            u = neighbor(i, j, grid)
            if s == 'O' or u == 'O':
                arr += '.'
            else:
                arr += 'O'
        s2.append(arr)
    if n == 3:
        return s2
    s3 = []
    for i in range(l):
        arr = ''
        for j in range(m):
            s = s2[i][j]
            u = neighbor(i,j, s2)
            v = '.'
            if s == 'O': #and u == 'O':
                if (n+1)%4 != 2:
                    v = 'O'
            #elif s == 'O' and u == '.':
            #    if (n+1)%4 != 2:
            #        v = 'O'
            elif s == '.' and u == 'O':
                if (n+1)%4 == 1 or (n+1)%4 == 3:
                    v = 'O'
            else:
                if (n+1)%4 != 0:
                    v = 'O'
            arr += v
        s3.append(arr)
    #print(state)
    return s3


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

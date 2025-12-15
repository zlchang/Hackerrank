#!/bin/python3

import math
import os
import random
import re
import sys
def up(a, b, grid):
    cntr = 0
    while a >= 0 and grid[a][b] == 'G':
        cntr += 1
        a -= 1
    return cntr

def down(a, b, grid):
    cntr = 0
    while a < len(grid) and grid[a][b] == 'G':
        cntr += 1
        a += 1
    return cntr

def right(a, b, grid):
    cntr = 0
    while b < len(grid[0]) and grid[a][b] == 'G':
        cntr += 1
        b += 1
    return cntr
def left(a, b, grid):
    cntr = 0
    while b >= 0 and grid[a][b] == 'G':
        cntr += 1
        b -= 1
    return cntr

def overlap(a, b, x, c, d, y):
    if (b == d and abs(a-c) < x+y-1) or (a == c and abs(b-d) < x+y-1):
        return True
    elif (abs(c-a) < y and abs(b-d) < x) or (abs(c-a) < x and abs(b-d) < y):
        return True
    return False
# Complete the twoPluses function below.
def twoPluses(grid):
    area =[]
    n =len(grid)
    m = len(grid[0])

    for i in range(n):
        col = []
        for j in range(m):
            ll = left(i, j, grid)
            rr = right(i, j, grid)
            uu = up(i, j, grid)
            dd = down(i, j, grid)
            aa = min(ll, rr, uu, dd)
            #vv = 0
            #if aa > 0:
            #    vv = 4*aa-3
            #if i == 1: print(ll, rr, uu, dd)
            col.append(aa)
        area.append(col)
    #print(area)
    result = 0
    for i in range(n*m):
        ri = i//m
        ci = i%m
        ai = area[ri][ci]
        if ai == 0: continue
        for j in range(i+1, n*m):
            rj = j//m
            cj = j%m
            #print(rj,cj)
            aj = area[rj][cj]
            if aj == 0: continue
            for p in range(1, ai+1):
                for q in range(1, aj+1): 
                    if not overlap(ri, ci, p, rj, cj, q):
                        result = max(result, (4*p-3)*(4*q-3))
    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()

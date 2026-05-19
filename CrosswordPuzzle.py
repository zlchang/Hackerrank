#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'crosswordPuzzle' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY crossword
#  2. STRING words
#
def row(g, r, i, j):
    s = ''
    for k in range(i, min(j, 10)):
        s += g[r][k]
    return s   
def col(g, i, j, c):
    s = ''
    for k in range(i, min(j, 10)):
        s += g[k][c]
    return s
def mrow(g, r, i, j, s):
    for k in range(i,j):
        g[r][k] = s[k-i]   
def mcol(g, i, j, c, s):
    for k in range(i, j):
        g[k][c] = s[k-i]
def compare(a, b):
    n = len(a)
    m = len(b)
    if n != m:
        return False
    for i in range(n):
        if a[i] == '+' or (a[i] != '-' and a[i] != b[i]): 
            return False
    return True
                        
def crosswordPuzzle(crossword, words):
    # Write your code here
    n = 10
    grid = [[] for i in range(n)]
    for i in range(n):
        for rr in crossword[i]:
            grid[i].append(rr) 
    places = words.split(';')
    
    def solve(wrds):
        if len(wrds) == 0:
            return 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '+':
                    continue
                for ww in wrds:
                    wl = len(ww)
                    sr = row(grid, i, j, j+wl)
                    ff = compare(sr, ww)
                    if ff:
                        mrow(grid, i, j, j+wl, ww)
                        cwrds = list(wrds)
                        cwrds.remove(ww)
                        if solve(cwrds) == 1:
                            return 1
                        mrow(grid, i, j, j+wl, sr)
                    sc = col(grid, i, i+wl, j)
                    ff = compare(sc, ww)
                    if ff:
                        mcol(grid, i, i+wl, j, ww)
                        cwrds = list(wrds)
                        cwrds.remove(ww)
                        if solve(cwrds) == 1:
                            return 1
                        mcol(grid, i, i+wl, j, sc)
        return 0
    solve(places)
    res = []
    for i in range(n):
        res.append(''.join(grid[i]))
    return res
                
                        
                        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

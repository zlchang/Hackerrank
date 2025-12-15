#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#
def dfs(start, moves, visited, matrix, res):
    x = start[0]
    y = start[1]
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    if visited[x][y] == 1 or matrix[x][y] == 'X':
        return 0
    if matrix[x][y] == '*':
        return 1
    visited[x][y] = 1  
    cntr = 0  
    for mv in moves:
        x1 = x+mv[0]
        y1 = y+mv[1]
        if x1 >= 0 and x1 < n and y1 >=0 and y1 < m and visited[x1][y1] == 0 and matrix[x1][y1] != 'X':
            cntr += 1
    if cntr > 1:
        res[0] += 1
    for mv in moves:
        x1 = x+mv[0]
        y1 = y+mv[1]
        if dfs([x1,y1], moves, visited, matrix, res) == 1:
            return 1
    return 0
        
    
def countLuck(matrix, k):
    # Write your code here
    n = len(matrix)
    m = len(matrix[0])
    start = [0]*2
    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    visited = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'M':
                start = [i, j]
    res = [0]
    dfs(start, moves, visited, matrix, res)
    #print(res)
    if res[0] == k:
        return 'Impressed'
    return 'Oops!'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    # Write your code here
    n = len(matrix)
    m = len(matrix[0])
    moves = [[1, -1], [0, -1], [-1, -1], [1, 0], [-1, 0], [1, 1], [0, 1], [-1, 1]]
    l = len(moves)
    visited = [[0 for i in range(m)] for j in range(n)]
    res = 0
    for i in range(n):
        for j in range(m):
            cntr = 0
            qq = []
            if matrix[i][j] == 1 and visited[i][j] == 0:
                qq.append([i, j])
                cntr += 1
                visited[i][j] = 1
            while qq != []:
                p = qq.pop(0)
                #print(len(qq))
                for k in range(l):
                    x = p[0]+moves[k][0]
                    y = p[1]+moves[k][1]
                    if x >= 0 and x < n and y >= 0 and y < m and matrix[x][y] == 1 and visited[x][y] == 0:
                        qq.append([x,y])
                        cntr += 1
                        visited[x][y] = 1
                        #print(x, y, cntr)
            res = max(res, cntr)
    return res
                        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()

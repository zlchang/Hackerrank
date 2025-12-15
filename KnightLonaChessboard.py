#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#
def steps(n, x, y):
    visited = [[-1 for i in range(n)] for j in range(n)]
    moves = [[x,y], [x,-y], [-x,y], [-x,-y], [y,x], [y,-x], [-y,x], [-y,-x]]
    m = len(moves)
    knights = []
    knights.append([0, 0])
    visited[0][0] = 0
    head = 0
    tail = 1
    while head < tail:
        pp = knights[head]
        head += 1
        for i in range(m):
            xx = pp[0]+moves[i][0]
            yy = pp[1]+moves[i][1]
            if xx >= 0 and xx < n and yy >= 0 and yy < n and visited[xx][yy] == -1:
                visited[xx][yy] = visited[pp[0]][pp[1]]+1
                knights.append([xx, yy])
                tail += 1
    
    return visited[n-1][n-1]
            
        
def knightlOnAChessboard(n):
    # Write your code here
    res = [[ 0 for j in range(n-1)] for i in range(n-1)]
    for i in range(1, n):
        for j in range(1, n):
            res[i-1][j-1] = steps(n, i, j)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

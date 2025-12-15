#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'printShortestPath' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER i_start
#  3. INTEGER j_start
#  4. INTEGER i_end
#  5. INTEGER j_end
#

def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Print the distance along with the sequence of moves.  
    # UL, UR, R, LR, LL, L.
    moves = {'UL': [-2, -1], 'UR': [-2, 1], 'R': [0, 2], 'LR': [2, 1], 'LL': [2, -1], 'L': [0, -2]}
    visited = [[0]*n for i in range(n)]
    steps = [[0]*n for i in range(n)]
    tracks = [[[] for j in range(n)] for i in range(n)]
    start = [i_start, j_start]
    end = [i_end, j_end]
    qq = []
    qq.append(start)
    visited[start[0]][start[1]] = 1
    while qq != []:
        q = qq.pop(0)
        x = q[0]
        y = q[1]
        
        for mk in moves.keys():
            mx = moves[mk][0]
            my = moves[mk][1]
            x1 = x + mx
            y1 = y + my
            if x1 >= 0 and x1 < n and y1 >= 0 and y1 < n and visited[x1][y1] == 0:
                #print(mx, my, x1, y1)
                steps[x1][y1] = steps[x][y]+1
                if tracks[x][y] != []:
                    for tt in tracks[x][y]:
                        tracks[x1][y1].append(tt)
                        #print(tt)
                #if x1 == end[0] and y1 == end[1]:
                    #print (x1, y1, mk)
                tracks[x1][y1].append(mk)
                qq.append([x1, y1])
                visited[x1][y1] = 1

    res = steps[end[0]][end[1]]
    trk = tracks[end[0]][end[1]]
    
    if res == 0:
        print('Impossible')
    else:
        print(res)
        print(' '.join(trk))
    #print(visited)
    #print(steps)
    return res
if __name__ == '__main__':
    n = int(input().strip())

    first_multiple_input = input().rstrip().split()

    i_start = int(first_multiple_input[0])

    j_start = int(first_multiple_input[1])

    i_end = int(first_multiple_input[2])

    j_end = int(first_multiple_input[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)

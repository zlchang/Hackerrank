#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#

def quickestWayUp(ladders, snakes):
    # Write your code here
    v = 100
    visited = [0]*v
    rolls = [0]*v
    dices = list(range(7))
    edges = {}
    for f, t in ladders:
        edges[f-1] = t-1
    for f, t in snakes:
        edges[f-1] = t-1
        
    qq = deque([0])
    visited[0] = 1
 
    while qq:

        p = qq.popleft()
        if p == 99:
            break
        if edges.get(p) != None:
            q = edges[p]
            if visited[q] == 0:
                rolls[q] = rolls[p]
                qq.append(q)
                visited[q] = 1
        else:   
            for d in dices:
                q = p+d
                if q < 100 and visited[q] == 0:
                    rolls[q] = rolls[p]+1
                    qq.append(q)
                    visited[q] = 1

    if visited[99] == 0:
        return -1
    return rolls[99]
                    
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()

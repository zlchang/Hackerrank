#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
#
# Complete the 'beautifulPath' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY edges
#  2. INTEGER A
#  3. INTEGER B
#

def beautifulPath(n, edges, A, B):
    # Write your code here
    l = 1024
    adj = [[] for i in range(n)]
    for u,v,w in edges:
        adj[u-1].append([v-1, w])
        adj[v-1].append([u-1, w])
    start = A-1
    end = B-1
    dist = [[0 for i in range(l)] for j in range(n)]
    
    qq = deque()
    dist[start][0] = 1
    qq.append([start, 0])
    while qq:
        q, d = qq.popleft()
        for e,w in adj[q]:
            h = d | w
            if dist[e][h] == 0:
                qq.append([e,h])
                dist[e][h] = 1
    for i in range(l):
        if dist[end][i] == 1:
            return i
    return -1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    second_multiple_input = input().rstrip().split()

    A = int(second_multiple_input[0])

    B = int(second_multiple_input[1])

    result = beautifulPath(n, edges, A, B)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
#
# Complete the 'shortestReach' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER s
#

def shortestReach(n, edges, s):
    # Write your code here
    gr = [[] for _ in range(n)]
    weights = [[-1 for _ in range(n)] for _ in range(n)]
    for u, v, w in edges:
        if weights[u-1][v-1] == -1:
            gr[u-1].append(v-1)
            gr[v-1].append(u-1)
            weights[u-1][v-1] = w
            weights[v-1][u-1] = weights[u-1][v-1]
        elif w < weights[u-1][v-1]:
            weights[u-1][v-1] = w
            weights[v-1][u-1] = weights[u-1][v-1]
            
        
    dist = [-1 for _ in range(n)]
    visited = [0 for _ in range(n)]
    pq = []
    heapq.heappush(pq, (0, s-1))
    dist[s-1] = 0
    while pq:
        d, p = heapq.heappop(pq)
        if visited[p] == 1:
            continue
        visited[p] = 1
        dist[p] = d
    
        for q in gr[p]:
            if visited[q] == 0:
                heapq.heappush(pq, (d+weights[p][q], q))
    res = []
    for i in range(n):
        if i != s-1:
            res.append(dist[i])
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

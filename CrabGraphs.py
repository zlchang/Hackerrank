#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'crabGraphs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER t
#  3. 2D_INTEGER_ARRAY graph
#   
def crabGraphs(n, t, graph):
    # Write your code here
    m = 2*n+2
    edges = [[0 for j in range(m)] for i in range(m)]
    for u, v in graph:
        a = u+n
        b = v+n
        edges[u][b] = 1
        edges[v][a] = 1 
    for i in range(1, n+1):
        edges[0][i] = 1
        edges[n+i][m-1] = t
    parent = [-1]*m
    
    def bfs(start, end):
        visited = [0]*m
        pp = deque()
        pp.append(start)
        visited[start] = 1
        parent[start] = start
        while pp:
            p = pp.popleft()
            for i in range(m):
                if visited[i] == 0 and edges[p][i] > 0:
                    pp.append(i)
                    visited[i] = 1
                    parent[i] = p
        return visited[end]
    res = 0
    while bfs(0, m-1):
        flow = t
        c = m-1
        while c != 0:
            p = parent[c]
            flow = min(t, edges[p][c])
            c = p
        c = m-1
        while c != 0:
            p = parent[c]
            edges[p][c] -= flow
            edges[c][p] += flow
            c = p
            
        res += flow
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    c = int(input().strip())

    for c_itr in range(c):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        t = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        graph = []

        for _ in range(m):
            graph.append(list(map(int, input().rstrip().split())))

        result = crabGraphs(n, t, graph)

        fptr.write(str(result) + '\n')

    fptr.close()

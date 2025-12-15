#!/bin/python3

import math
import os
import random
import re
import sys

def dfs(x, edges, visited):
    visited[x] = 1
    for e in edges[x]:
        if visited[e] == 0:
            dfs(e, edges, visited)
            visited[x] += visited[e]
    
# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    n = t_nodes
    m = t_edges
    edges = [[] for i in range(n)]
    
    for i in range(m):
        a = t_from[i]-1
        b = t_to[i]-1
        edges[a].append(b)
        edges[b].append(a)
        
    visited = [0]*n
    
    dfs(0, edges, visited)
    #print(visited)
    res = 0
    for i in range(1, n):
        if visited[i] % 2 == 0:
            res += 1
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()

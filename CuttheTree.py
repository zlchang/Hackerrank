#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(10**9)
#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#
def dfs(data, start, gr, visited, sm):
    q = start
    visited[q] = 1
    ss = data[q]
    for e in gr[q]:
        if visited[e] == 0:
            ss += dfs(data, e, gr, visited, sm)
    sm[q] = ss
    return ss
    
def cutTheTree(data, edges):
    # Write your code here
    n = len(data)
    gr = [[] for i in range(n)]
    sm = [0]*n
    visited = [0]*n
    
    for n1, n2 in edges:
        gr[n1-1].append(n2-1)
        gr[n2-1].append(n1-1)

    dfs(data, 0, gr, visited, sm)
    total = sum(data)
    res = total
    for i in range(1,n):
        df = abs(total-sm[i]*2)
        res = min(res, df) 
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()

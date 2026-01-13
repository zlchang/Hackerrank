#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsInHackerland' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY roads
#

def roadsInHackerland(n, m, roads):
    # Write your code here
    
    edges = []
            
    for a, b, c in roads:
        edges.append([a-1, b-1, c])
        
    
    edges.sort(key=lambda x: x[2])
    
    parent = [i for i in range(n)]
    
    def find(node):
        pn = parent[node]
        if pn != node:
            parent[node] = find(pn)
            return parent[node]
        return node
    def union(u, v):
        pu = find(u)
        pv = find(v)
        parent[pv] = pu

    mst = [[] for i in range(n)]
    for a, b, w in edges:
        #pa = find(a)
        #pb = find(b)
        #print(a, b, pa, pb)
        if find(a) != find(b):
            union(a, b)
            mst[a].append([b, w])
            mst[b].append([a, w])
            #print(find(a), find(b))
    #print(mst)
    uses = [0]*m
    def dfs(u, p):
        nchild = 0
        for e,w in mst[u]:
            if e != p:
                ne = 1+dfs(e, u) 
                uses[w] += ne*(n-ne)
                nchild += ne
        return nchild
    dfs(0,0)
    res = 0
    for i in range(m):
        res += uses[i] * (1 << i)
    return f'{res:b}'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    result = roadsInHackerland(n, m, roads)

    fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

def prims(n, edges, start):
    # Write your code here
    m = len(edges)
    max_cost = 2*10**5
    adj = [[] for i in range(m)]
    for u, v, w in edges:
        adj[u-1].append([v-1, w])
        adj[v-1].append([u-1, w])
    cost = [max_cost]*n
    visited = [0]*n
    prev = [0]*n
    
    pq = []
    cost[start-1] = 0
    visited[start-1] = 1
    heapq.heappush(pq, (cost[start-1], start-1))
    
    while pq:
        cc, q = heapq.heappop(pq)
        visited[q] = 1
        for p, w in adj[q]:
            cp = w
            if cp < cost[p] and visited[p] == 0:
                cost[p] = cp
                heapq.heappush(pq, (cp, p)) 
                prev[p] = q  
    #print(cost)   
    #print(prev)
    return sum(cost) 
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()

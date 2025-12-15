#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'shop' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. STRING_ARRAY centers
#  4. 2D_INTEGER_ARRAY roads
#

def shop(n, k, centers, roads):
    # Write your code here
    MAX = 2*10**7
    kinds = [0]*n
    for i in range(n):
        ic = centers[i].rstrip().split()
        nk = int(ic[0])
        for j in range(1, nk+1):
            jk = int(ic[j])
            kinds[i] |= 1 << (jk-1)
    mk = 1 << k
    
    edges = [[] for i in range(n)]
    for u, v, w in roads:
        edges[u-1].append([v-1, w])
        edges[v-1].append([u-1, w])
    #print(edges)   
    dist = [[MAX for i in range(mk)] for j in range(n)]
    
    pq = []
    dist[0][kinds[0]] = 0
    heapq.heappush(pq, (0, 0, kinds[0]))
    
    while pq != []:
        d, q, t = heapq.heappop(pq)
        if d > dist[q][t]:
            continue
        for e, w in edges[q]:
            de = dist[q][t]+w
            te = kinds[e] | t
            if dist[e][te] > de:
                dist[e][te] = de
                heapq.heappush(pq, (de, e, te))
                #print(e, w, te, de)
    
    res = MAX
    for i in range(mk):
        for j in range(i, mk):
            if i | j == mk-1:
                res2 = max(dist[n-1][i], dist[n-1][j])
                res = min(res, res2)
    return res
        
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    centers = []

    for _ in range(n):
        centers_item = input()
        centers.append(centers_item)

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    res = shop(n, k, centers, roads)

    fptr.write(str(res) + '\n')

    fptr.close()

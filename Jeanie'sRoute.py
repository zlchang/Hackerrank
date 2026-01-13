#!/bin/python3

import os
import sys
sys.setrecursionlimit(1000000)
#
# Complete the jeanisRoute function below.
#
def jeanisRoute(n, city, roads):
    #
    # Write your code here.
    #
    edges = [[] for i in range(n)]
    
    for u, v, w in roads:
        edges[u-1].append([v-1, w])
        edges[v-1].append([u-1, w])

    good = [0]*n
    for c in city:
        good[c-1] = 1
    #print(edges)
    dist = [0]*n
    diam = [0, 0, 0]
    def dfs(s, p):
        #print(s)
        for e,w in edges[s]:
            if e != p:
                dist[e] = dist[s]+w
                #print(s, e, w, dist[e])
                dfs(e,s)
                good[s] += good[e]
                #print(s, e, re)
                if good[e] != 0: 
                    diam[2] += w          
                    #print(e, dist[e])
                    if dist[e] > diam[1]:
                        diam[1] = dist[e]
                        diam[0] = e

    start = city[0]-1
    dfs(start, start)
    for i in range(n):
        dist[i] = 0
    diam[1] = 0
    diam[2] = 0
    start = diam[0]
    #print(f'start:{start}')
    dfs(start, start)
    #print(diam)
    total = diam[2]
    res = 2*total - diam[1]
    return res
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    city = list(map(int, input().rstrip().split()))

    roads = []

    for _ in range(n-1):
        roads.append(list(map(int, input().rstrip().split())))

    result = jeanisRoute(n, city, roads)

    fptr.write(str(result) + '\n')

    fptr.close()

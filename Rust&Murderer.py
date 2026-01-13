#!/bin/python3

import os
import sys
from collections import deque

#
# Complete the rustMurdered function below.
#
def rustMurderer(n, roads, s):
    #
    # Write your code here.
    #
    edges = [set() for i in range(n)]
    for u, v in roads:
        edges[u-1].add(v-1)
        edges[v-1].add(u-1)
    qq = deque()
    start = s-1
    dist = [-1]*n
    qq.append(start)
    dist[start] = 0
    
    while qq:
        p = qq.popleft()
        sr = 0
        for i in range(n):
            if i in edges[p]:
                continue
            if i == p:
                continue
            if dist[i] == -1:
                dist[i] = dist[p]+1
                print(p, i, dist[p], dist[i])
                qq.append(i)
            sr += 1
        if sr == n-1:
            qq.clear()
    res = [0]*(n-1)
    j = 0
    for i in range(n):
        if i == start:
            continue
        res[j] = dist[i]
        j += 1
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        roads = []

        for _ in range(m):
            roads.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = rustMurderer(n, roads, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankCity' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY A as parameter.
#
def base(w = 1):
    ng = 6
    edges = [(1,5), (5,1), (5,2), (5, 6), (2, 5), (3,6), (6,3), (6,5), (6,4), (4,6)]
    adj = [[] for _ in range(ng)]
    for a, b in edges:
        adj[a-1].append(b-1)
    dist = [0]*ng
    child = [0]*ng
    def dfs_a(q, p):
        for e in adj[q]:
            if e != p:
                dist[e] = dist[q]+w
                dfs_a(e, q)
                child[q] += 1+child[e]
    def dfs_b(q, p):
        for e in adj[q]:
            if e != p:
                dist[e] = dist[q] - child[e] + (ng-child[e]-2)
                dfs_b(e, q)
    dfs_a(0, -1)
    res = list(dist)
    dist[0] = sum(dist)
    dfs_b(0, -1)
    #print(dist)
    #print(sum(dist))
    return res
def hackerrankCity(A):
    # Write your code here
    mod = 1000000007
    dist = base()
    #print(dist)
    ne = len(dist)
    #print(ne)
    n = len(A)
    curr = [0, 0, 0, 1]
    for i in range(n):
        ai, ti, si, ni = curr
        al = [ai, ai, ai, ai, 0, 0]
        nl = [ni, ni, ni, ni, 1, 1]
        wi = A[i]
        aj = 0
        tj = 0
        #print(ai, si)
        #for j in range(1, ne):
            #aj += si*nl[j]+dist[j]*wi*nl[j]+al[j]
            #tj += nl[j]*al[0]+dist[j]*wi*nl[0]*nl[j]+al[j]*nl[0]
        aj = (2*si+(3*ni*si)%mod+3*wi+8*wi*ni+4*ai)%mod
        tj = (2*(2*ai+(6*ai*ni)%mod+3*wi*ni+(8*wi*ni*ni)%mod) + (2*(wi*ni+ai)+2*(2*wi*ni+ai)+wi) + 4*ti)%mod
        sj = (3*wi+si+si)%mod
        nj = (4*ni+2)%mod
        curr = [aj, tj, sj, nj]
        #print(curr)
    res = curr[1]
    return res
                
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    A_count = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    result = hackerrankCity(A)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'storyOfATree' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY guesses
#
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)
def storyOfATree(n, edges, k, guesses):
    # Write your code here
    adj = [[] for i in range(n)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    gm = set((u-1, v-1) for u, v in guesses)
 
    visited = [0]*n
    na = [0]*n
    nc = [0]
    def dfs(i):
        if visited[i] == 1:
            return 0
        visited[i] = 1
        for e in adj[i]:
            if visited[e] == 0:
                na[e] = na[i]
                #nb[e] = nb[i]
                if (e, i) in gm:
                    na[e] += 1
                if (i, e) in gm:
                    nc[0] += 1
                    na[e] -= 1
                dfs(e)
        return 1
    dfs(0)
    res = 0
    for i in range(n):
        if na[i]+nc[0] >= k:
            res += 1
    if res == 0:
        return f'0/1'
    if res == n:
        return f'1/1'
    f = gcd(res, n)
    fa = res//f
    fb = n//f
    return f'{fa:d}/{fb:d}'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        first_multiple_input = input().rstrip().split()

        g = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        guesses = []

        for _ in range(g):
            guesses.append(list(map(int, input().rstrip().split())))

        result = storyOfATree(n, edges, k, guesses)

        fptr.write(result + '\n')

    fptr.close()

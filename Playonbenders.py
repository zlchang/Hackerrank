#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bendersPlay' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY paths
#  3. INTEGER_ARRAY query
#

def bendersPlay(memo, query):
    # Write your code here
    
    res = 0
    for q in query:
        res ^= memo[q-1]
    if res == 0:
        return 'Iroh'
    return 'Bumi'
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    paths = []

    for _ in range(m):
        paths.append(list(map(int, input().rstrip().split())))

    edges = [[] for i in range(n)]  
    for u, v in paths:
        edges[u-1].append(v-1)
    memo = [-1]*n
    def dfs(r):
        if memo[r] != -1:
            return memo[r]
        gr = set()
        for e in edges[r]:
            gr.add(dfs(e))
        g = 0
        while g in gr:
            g += 1
        memo[r] = g
        return g
    for i in range(n):
        dfs(i)
    
    q = int(input().strip())

    for q_itr in range(q):
        query_count = int(input().strip())

        query = list(map(int, input().rstrip().split()))

        result = bendersPlay(memo, query)

        fptr.write(result + '\n')

    fptr.close()

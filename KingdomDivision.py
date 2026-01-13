#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(100000)
#
# Complete the 'kingdomDivision' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY roads
#
mod = 1000000007
def kingdomDivision(n, roads):
    # Write your code here
    edges = [[] for i in range(n)]
    for u, v in roads:
        edges[u-1].append(v-1)
        edges[v-1].append(u-1)
    def dfs(curr, prev):
        total = 1
        lonely = 1
        for e in edges[curr]:
            if e == prev: 
                continue
            comb = dfs(e, curr) 
            lonely = lonely*comb[0]
            lonely %= mod
            total = total*(comb[0]+comb[1])
            total %= mod
        return [(total-lonely+mod)%mod, total]
    res = dfs(0, 0)
    return (res[0]*2)%mod

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    result = kingdomDivision(n, roads)

    fptr.write(str(result) + '\n')

    fptr.close()

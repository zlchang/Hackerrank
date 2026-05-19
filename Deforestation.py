#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'deforestation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY tree
#

def deforestation(n, tree):
    # Write your code here
    edges = [[] for _ in range(n)]
    for u, v in tree:
        edges[u-1].append(v-1)
        edges[v-1].append(u-1)
    child = [0]*n
    def dfs(node, parent):
        for e in edges[node]:
            if e != parent:
                dfs(e, node)
                child[node] ^= 1+child[e]
    dfs(0, 0)
    #print(child)

    if child[0] == 0:
        return 'Bob'
    return 'Alice'
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        tree = []

        for _ in range(n - 1):
            tree.append(list(map(int, input().rstrip().split())))

        result = deforestation(n, tree)

        fptr.write(result + '\n')

    fptr.close()

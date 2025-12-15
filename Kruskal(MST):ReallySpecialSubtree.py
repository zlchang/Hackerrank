#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#
def find(x, parent):
    pn = parent[x]
    if x != pn:
        return find(pn, parent)
    return pn
def union(x, y, parent):
    fx = find(x, parent)   
    fy = find(y, parent)
    parent[fy] = fx
    
def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    n = g_nodes
    m = len(g_from)
    edges = []
    for i in range(m):
        a = g_from[i]-1
        b = g_to[i]-1
        w = g_weight[i]
        edges.append([a, b, w])
    edges.sort(key=lambda x : x[2])
    #print(edges)
    parent = list(range(n))
    #print(parent)
    
    res = 0
    for a, b, w in edges:
        pa = find(a, parent)
        pb = find(b, parent)
        #print(a, b, pa, pb)
        if pa != pb:
            union(a, b, parent)
            res += w
            #print(a, b, w)
            #print(parent)
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    fptr.write(str(res))
    fptr.close()
